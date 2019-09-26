def addToTS(r):
    execute("xadd", "log", "*", "f", "addToTS", "enter", r)

    execute("TS.ADD", "temp:raw", "*", r["t"])
    return r


def calcSMA(ignore):
    try:
        execute("xadd", "log", "*", "f", "calcSMA", "enter", ignore)

        avgs = execute("TS.RANGE", "temp:avg:1s", 0, -1)

        execute("xadd", "log", "*", "f", "calcSMA", "avgs", avgs, "sa len", len(avgs))

        sma = -1
        if len(avgs) > 0:
            sma = sum([float(x[1]) for x in avgs]) / len(avgs)

        execute("xadd", "log", "*", "f", "calcSMA", "sma", sma)

    except Exception as e:
        execute("xadd", "log", "*", "f", "calcSMA", "EXCEPTION", e)

    return sma


def noValue(sma):
    execute("xadd", "log", "*", "f", "noValue", "enter", sma)

    return sma > -1


def publish(sma):
    execute("xadd", "log", "*", "f", "publish", "enter", sma)

    execute("xadd", "egress", "*", "sma", sma)


gb = GearsBuilder("StreamReader").map(addToTS).map(calcSMA).filter(noValue).map(publish)
gb.register("ingress")

execute("hmset", "gears-status", "name", "ts-pipeline", "status", "loaded")


# Questions
# Can I have a redis symbol so I can use redis.hmset directly?
# Can I have a GearsBuilder symbol...
