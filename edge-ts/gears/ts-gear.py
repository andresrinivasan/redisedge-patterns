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

execute("flushall")
execute("TS.CREATE", "temp:raw", "RETENTION", 5000)
execute("TS.CREATE", "temp:avg:1s", "RETENTION", 300000)
execute("TS.CREATERULE", "temp:raw", "temp:avg:1s", "AGGREGATION", "avg", 1000)

gb = gearsCtx('StreamReader') \
    .map(addToTS) \
    .map(calcSMA) \
    .map(publish)

gb.register('event-ingress-stream')

# ## Do I really need foreach when map() + return does the same thing and is more consistent with OPP
# ## How do I test outside of Gears?
