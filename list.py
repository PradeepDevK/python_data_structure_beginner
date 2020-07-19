lists = ["Codeforgeek", "Courses", "Lessons", 130]
print(lists)

# Indexing
print(lists[0])

# Length
print(len(lists))

# Change the value
lists[3] += 5
print(lists)

num_seq = range(0, 10)
num_list = list(num_seq)
print(num_list)

num = [[1,2],[3,4],[5,6,7,8,9,10],[0.5]]
print(num[0][1]) #prints 2

num_list = [1,2]
num_list.append(3) # add 3 at the end of the list
print(num_list)
num_list.insert(3, 40)  # Inserting 40 at the 3rd index and shifts the index of the list
print(num_list)


num_list = [1,2,3,4,5]
num_list.pop()
print(num_list)
num_list.remove(3)  # removes 3 from the list
print(num_list)

num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)