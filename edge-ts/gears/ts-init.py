import sys
import redis


def clean(conn):
    print("Cleaning keys...")

    try:
        conn.execute_command("TS.DELETERULE", "temp:raw", "temp:avg:1s")
        conn.delete("temp:raw", "temp:avg:1s")
        conn.delete("gears-status")
    except:
        None


def load(conn):
    print("Loading gear...")

    with open('ts-pipeline.py', 'rb') as f:
        gear = f.read()
        res = conn.execute_command('RG.PYEXECUTE', gear)


def init(conn):
    try:
        conn.execute_command("TS.INFO", "temp:raw")
        return
    except:
        None

    clean(conn)
    print("Setting up time series keys...")

    conn.execute_command("TS.CREATE", "temp:raw", "RETENTION", 5000)
    conn.execute_command("TS.CREATE", "temp:avg:1s", "RETENTION", 300000)
    conn.execute_command("TS.CREATERULE", "temp:raw",
                         "temp:avg:1s", "AGGREGATION", "avg", 1000)


def usage():
    print("Usage: {} [init | clean]".format(sys.argv[0]))


if __name__ == "__main__":
    argvHandlers = {
        'init': init,
        'clean': clean,
        'load': load
    }

    if len(sys.argv) > 1:
        if sys.argv[1] in argvHandlers:
            h = argvHandlers[sys.argv[1]]
        else:
            print("Unknown command line argument: {}".format(sys.argv[1]))
            usage()
            sys.exit(-1)

    conn = redis.Redis(host="localhost", port=6379)

    h(conn)
