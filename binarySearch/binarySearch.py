def binarySearch(list, item):
    low =0
    high = len(list)-1

    while(low<=high):
        mid = low + high
        guess = list[mid]
        if (guess == item):
            return mid
        elif (guess > item):
            high = mid -1
        else:
            low = mid +1
        return None
test_list = [1,6,55,34,29,89]
print(binarySearch(test_list,89))
print(binarySearch(test_list,55))

