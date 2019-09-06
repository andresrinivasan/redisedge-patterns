.PHONY: no-default all setup start start-redis-edge stop-redis-edge clean clean-db

PYTHON = python3

no-default:

all:

setup:
	docker pull redislabs/redisedge

start: start-redis-edge
	cd gears && $(PYTHON) ts-init.py init
	cd gears && $(PYTHON) ts-init.py load

start-redis-edge:
	--mkdir data 2>/dev/null
	docker run --name RedisEdge --user $(shell id -u) -d --rm -p 6379:6379 \
	--mount type=bind,src=$(CURDIR)/ts.conf,dst=/etc/ts.conf,readonly \
	--mount type=bind,src=$(CURDIR)/data,dst=/data \
	redislabs/redisedge /etc/ts.conf

stop-redis-edge:
	docker stop RedisEdge

test:
	tools/add-random-data

clean: clean-db stop-redis-edge
	rm -rf data

clean-db:
	cd gears && $(PYTHON) ts-init.py clean

