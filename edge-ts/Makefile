.PHONY: all init start pull clean

all: pull start init

pull:
	docker pull redislabs/redisedge

init:
	./init-redisedge.sh

start:
	docker run --rm -p 6379:6379 \
		--mount type=bind,src=$(pwd)/ts.conf,dst=/etc/ts.conf \
    --mount type=bind,src=$(pwd)/gears,dst=/etc/gears \
    --mount type=bind,src=$(pwd)/,dst=/data/ \
    redislabs/redisedge /etc/ts.conf

clean:
	redis-cli flushall