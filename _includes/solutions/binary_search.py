def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        middle = (low + high) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
