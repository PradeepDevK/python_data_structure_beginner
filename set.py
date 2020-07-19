test_set = {1,2,3,"Pradeep", (1.5,2.5)}
print(test_set)
print(len(test_set))  # Length of the set

new_set = {1,2,3}
new_set.add(10)
print(new_set)

new_set.update([20, 30, 40])
print(new_set)

new_set = {1,2,3,4,5}
print(new_set)

new_set.remove(5)
print(new_set)

new_set = {1,2,3,4,5}

for set_value in new_set:
    print(set_value)