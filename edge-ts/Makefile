.PHONY: all init start pull clean

all: start

pull:
	docker pull redislabs/redisedge

init:
	./init-redisedge.sh

start:
	docker run --rm -p 6379:6379 \
	--mount type=bind,src=$(CURDIR)/ts.conf,dst=/etc/ts.conf \
	--mount type=bind,src=$(CURDIR)/ts-gears,dst=/etc/ts-gears \
	--mount type=bind,src=/Users/andresrinivasan/.local/share/virtualenvs/redisedge-patterns-l-jFYGhY/lib/python3.7/site-packages,dst=/lib/python/site-packages \
	--mount type=bind,src=/tmp/lib/python3.7/site-packages,dst=/data \
	redislabs/redisedge /etc/ts.conf

clean:
	redis-cli flushall