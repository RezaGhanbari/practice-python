def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    test = [1, 2, 43, 1, 135, 3, 1324, 65, 35, 13, 646, 2, 4, 5, 6, 71, 1, 42, 24, 24]
    print quick_sort(test)
