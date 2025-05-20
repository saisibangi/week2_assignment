# empty list
my_list = []

# Appending elements 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Inserting 15 at the second position (index 1)
my_list.insert(1, 15)

# Extending my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# Sorting the list in ascending order
my_list.sort()

# Finding and printing the index of the value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)
