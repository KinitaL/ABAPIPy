def binary_search(numbers, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            return binary_search(numbers, target, mid + 1, high)
        else:
            return binary_search(numbers, target, low, mid - 1)
    else:
        return -1