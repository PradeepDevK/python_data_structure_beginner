num_lists = (1,2,3,4,5,6,7,8,9,10)
print(num_lists)
print(num_lists[0])
print(len(num_lists))

num_lists=([1,2,3],[4,5,6])
print(num_lists[0])
# change value of list inside the tuple
num_lists[0][0] += 5
print(num_lists)


#search
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("London" in cities) # True
print("Mumbai" in cities) # False