userId = {
    "100": "Pradeep",
    "120": "John",
    "130": "Mary"
}

print(userId)
print(len(userId))
print(userId["100"])


userId = {
    "100": "Pradeep",
    "120": "John",
    "130": "Mary"
}

userId["150"] = "Wick" # add new entry
userId["100"] = "Pradeep Raj"
print(userId)

userId = {
    "100": "Pradeep",
    "120": "John",
    "130": "Mary"
}

removedItem = userId.pop("100")
lastItem = userId.popitem()
print(removedItem)
print(lastItem)

userId = {
    "100": "Pradeep",
    "120": "John",
    "130": "Mary"
}

print("100" in userId) # True
print("500" in userId) # False