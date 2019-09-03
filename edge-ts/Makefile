.PHONY: no-default all setup start start-redis-edge clean

no-default:

all:

setup:
	docker pull redislabs/redisedge

start: start-redis-edge
	cd gears && python3 ts-init.py

start-redis-edge:
	docker run -d --rm -p 6379:6379 \
	--mount type=bind,src=$(CURDIR)/ts.conf,dst=/etc/ts.conf \
	--mount type=bind,src=$(CURDIR)/gears,dst=/etc/gears \
	--mount type=bind,src=$(CURDIR),dst=/data \
	redislabs/redisedge /etc/ts.conf

test:
	tools/add-random-data

clean:
	redis-cli flushall
