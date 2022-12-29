"""
Sorting Method
"""

def find_smallest(arr):
    """
    find smallest index
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    """
    sorting function
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# fruits = ["orange", "watermelon", "apple", "kiwi", "pear", "cherry"]
numbers = [77, 90, 3, 5, 66, 1, 786, 55, 11]
# print(find_smallest(numbers))
print(selection_sort(numbers))
