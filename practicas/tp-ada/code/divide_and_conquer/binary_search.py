def binary_search(array, value):
    # O(log(n))
    
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2

        if array[middle] == value:
            return True
        
        if array[middle] > value:
            end = middle - 1
        else:
            start = middle + 1

    return False

