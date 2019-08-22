from json_logic import jsonLogic

jsonLogic({"==": [1, 1]})
# True

jsonLogic(
    {"and": [
        {">": [3, 1]},
        {"<": [1, 3]}
    ]}
)

rules = {"and": [
    {"<": [{"var": "temp"}, 110]},
    {"==": [{"var": "pie.filling"}, "apple"]}
]}

data = {"temp": 100, "pie": {"filling": "apple"}}

print("result: {}".format(jsonLogic(rules, data)))
# True
