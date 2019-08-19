# Edge IFTTT

## Dependencies

* [JSONLogic](jsonlogic.com)
* RedisEdge

## Install

`pip install json-logic-qubit`
`docker pull redislabs/redisedge`

## Start

`docker run --rm -p 6379:6379 \
        --mount type=bind,src=$(pwd)/ifttt.conf,dst=/etc/ifttt.conf \
        --mount type=bind,src=$(pwd)/gears,dst=/etc/gears \
        --mount type=bind,src=$(pwd)/,dst=/data/ \
        redislabs/redisedge /etc/ifttt.conf
