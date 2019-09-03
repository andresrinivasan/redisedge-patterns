def addToTS(r):
    execute("TS.ADD", "temp:raw", "*", r["t"])       ## Intellicode doesn't know about execute
    return r

def calcSMA(r):
    avgs = execute("TS.RANGE", "temp:avg:1s", 0, -1)
    execute("XADD", "log", "*", "f", "calcSMA", "avgs", avgs, "sa len", len(avgs))

    sma = sum([int(x[1]) for x in avgs]) / len(avgs)
    execute("XADD", "log", "*", "f", "calcSMA", "sma", sma)

    return sma

def publish(r):
    execute("XADD", "egress", "*", "sma", r)

gb = gearsCtx('StreamReader') \
    .map(addToTS) \
    .map(calcSMA) \
    .map(publish)

gb.register('ingress')

execute("hmset", "gears-status", "name", "ts-pipeline", "status", "loaded")

