# RedisEdge Patterns

For IoT/Edge, use patterns have emerged around data ingress, processing, event detection, data egress. The intent here is to share example(s) of those patterns

## Data Ingress

We usually use one or Streams for ingress. This makes it easier to connect the data to other data structures via a Gear. See [Anti Patterns](#anti-patterns) for additional scenarios.

## Data Orchestration

RedisGears registers for events (new data) on Streams and then takes appropriate action. This could be something entirely covered by the Gear or it could be a handoff to another data structure.

### IFTTT

Techncially you can do anything in a Gear that you can do in Python. But do you really want to write all those conditions. Something like [JSONLogic](jsonlogic.com) makes an excellent engine for this kind of business logic.

## Anti Patterns

1. If all the data is time series, RedisTimeSeries effectively acts as a data/sample stream. Of course a Gear can't react to it directly though data traditional Redis events can be used as triggers or the app can invoke a Gear. Typically the app is interacting directly with one or more time series.
