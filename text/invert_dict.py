def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted


c = invert_dict({"a": 1, "b": 2})
print(c)
