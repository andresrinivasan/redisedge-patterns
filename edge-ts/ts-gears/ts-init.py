import redis

if __name__ == '__main__':
    conn = redis.Redis(host="localhost", port=6379)
   
    print('Loading gear - ', end='')
    with open('ts-gear.py', 'rb') as f:
        gear = f.read()
        res = conn.execute_command('RG.PYEXECUTE', gear)
        print(res)

## I want to be able to set PythonHomeDir via code. Consider pipenv...