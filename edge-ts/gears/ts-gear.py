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

execute("flushall")
execute("TS.CREATE", "temp:raw", "RETENTION", 5000)
execute("TS.CREATE", "temp:avg:1s", "RETENTION", 300000)
execute("TS.CREATERULE", "temp:raw", "temp:avg:1s", "AGGREGATION", "avg", 1000)

gb = gearsCtx('StreamReader') \
    .map(addToTS) \
    .map(calcSMA) \
    .map(publish)

gb.register('ingress')

# ## Do I really need foreach when map() + return does the same thing and is more consistent with OPP
# ## How do I test outside of Gears?
