def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

elem = 18
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

print("Searching for {}".format(elem))
print("Index of {}: {}".format(elem, binary_search_recursive(array, elem, 0, len(array))))
