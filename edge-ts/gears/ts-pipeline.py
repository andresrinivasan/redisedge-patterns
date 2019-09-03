def addToTS(r):
    if r["device"] == 'TemperatureHumiditySensor' and r["name"] == 'Temperature':
        execute("TS.ADD", "temp:raw", "*", r["value"])
        return r

def calcSMA(r):
    avgs = execute("TS.RANGE", "temp:avg:1s", 0, -1)
    execute("XADD", "log", "*", "f", "calcSMA", "avgs", avgs, "sa len", len(avgs))

    sma = sum([int(x[1]) for x in avgs]) / len(avgs)
    execute("XADD", "log", "*", "f", "calcSMA", "sma", sma)

    return sma

def publish(r):
    execute("XADD", "event-egress-stream", "*", "sma", r)

gb = gearsCtx('StreamReader') \
    .map(addToTS) \
    .map(calcSMA) \
    .map(publish)

gb.register('event-ingress-stream')

execute("hmset", "gears-status", "name", "ts-pipeline", "status", "loaded")

