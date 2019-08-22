# Edge TS

Redis Streams gives us a useful tool to ingest data associated with time. RedisTimeSeries gives us more power to deal with time series samples. The challenge is how to create an architecture that restrict the solution to the current set of solutions. We do that by decoupling how the data is manipulated from how the data is ingested. In other words, create an ingress stream, manipulate the data, then expose the results.

If we assume the data is noisy, we can use time series to reduce the noise before we apply event detection. For data that is generally moving up or down, a simple moving average should reduce the noise.

## Dependencies

* Redis 5 (for redis-cli command)
* RedisEdge
* Python 3

Note this is coded against RedisGears 0.3.1 which is part of RedisEdge as of this writing.

## Setup

``` sh
make setup
```

## Start

``` sh
make start
```

## Test

``` sh
make test
```
