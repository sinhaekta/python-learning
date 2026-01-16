# input: [10, 5, 20, 8, 15]


def second_largest_element(arr):
    if len(arr) < 2:
        return None  # Not enough elements
    first = second = float('-inf')  # Initialize to negative infinity
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None


# example
input_list = [10, 5, 20, 8, 15]
result = second_largest_element(input_list)
print(result)  # Output: 15