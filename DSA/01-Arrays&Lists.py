# array: a collection of items stored at contiguous memory locations
# list: a collection of items which are not stored at contiguous memory locations (more flexible than arrays)
list = [20, 40, 10, 56]

print(list[0])  # Accessing first element

for i in range(len(list)):
    print(list[i])  # Accessing each element using index -> O(1) time complexity

for i in list:
    print(i)  # Accessing each element directly

list.append(70)  # Adding an element at the end
print(list)

list.insert(2, 30)  # Inserting 30 at index 2
print(list)

list.remove(10)  # Removing element 10
print(list)

list.pop()  # Removing last element
print(list)

list.sort()  # Sorting the list
print(list)

# searching in a list
target = 40
for i in  range(len(list)):
    if list[i] == target:
        print(f"Element {target} found at index {i}")

# Reverse the list
rev = []
for i in range(len(list)-1, -1, -1): # range(start, stop, step)
    rev.append(list[i])
print(rev)

