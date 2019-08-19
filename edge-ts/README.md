# Edge TS

Redis Streams gives us a useful tool to ingest data associated with time. RedisTimeSeries gives us more power to deal with time series samples. The challenge is how to create an architecture that restrict the solution to the current set of solutions. We do that by decoupling how the data is manipulated from how the data is ingested. In other words, create an ingress stream, manipulate the data, then expose the results.

If we assume the data is noisy, we can use time series to reduce the noise before we apply event detection. For data that is generally moving up or down, a simple moving average should reduce the noise.

## Dependencies

* RedisEdge

## Install

``` sh
docker pull redislabs/redisedge
```

## Start

``` sh
docker run --rm -p 6379:6379 \
        --mount type=bind,src=$(pwd)/ts.conf,dst=/etc/ts.conf \
        --mount type=bind,src=$(pwd)/ts-gears,dst=/etc/ts-gears \
        --mount type=bind,src=/Users/andresrinivasan/.local/share/virtualenvs/redisedge-patterns-l-jFYGhY/lib/python3.7/site-packages,dst=/lib/python/site-packages \
        --mount type=bind,src=$(pwd)/,dst=/data/ \
        redislabs/redisedge /etc/ts.conf
```

## PoC

``` sh
TS.CREATE temp:raw RETENTION 5000
TS.CREATE temp:avg:1s RETENTION 300000
TS.CREATERULE temp:raw temp:avg:1s AGGREGATION avg 1000
```

``` sh
while :; do redis-cli XADD ingress '*' MAXLEN ~ 1000 t $RANDOM; done
```
