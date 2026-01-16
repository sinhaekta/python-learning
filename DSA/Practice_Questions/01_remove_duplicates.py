# Input:  [1, 2, 2, 3, 1]
# Output: [1, 2, 3]

def remove_duplicates(list):
    unique_elements = []
    for item in list:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements


# example
input_list = [1, 2, 2, 3, 1]
result = remove_duplicates(input_list)
print(result)  # Output: [1, 2, 3]