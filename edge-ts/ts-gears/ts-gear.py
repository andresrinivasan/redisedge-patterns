from gearsclient import GearsBuilder as GB
import redis    

def addToTS(r):
    GB.execute("TS.ADD", "*", r["t"])       ## Intellicode doesn't know about execute
    return r

def calcSMA(r):
    sa = GB.execute("TS.RANGE", "temp:avg:1s", 0, -1)
    print(sa)
    return r  ## XXX

def publish(r):
    pass

## Rather than use the redis module, I believe it would look more pleasing to have a one time GB
## based expression
conn = redis.Redis(host='localhost', port=6379)

conn.flushall()
conn.execute_command("TS.CREATE", "temp:raw", "RETENTION", 5000)
conn.execute_command("TS.CREATE", "temp:avg:1s", "RETENTION", 300000)
conn.execute_command("TS.CREATERULE", "temp:raw", "temp:avg:1s", "AGGREGATION", "avg", 1000)

GB('StreamReader') \
    .map(addToTS) \
    .map(calcSMA) \
    .map(publish)

GB.register('ingress')

## How come gearsclient isn't part of the module install?
## Do I really need foreach when map() + return does the same thing and is more consistent with OPP
## How do I test outside of Gears?
