def binary_search (list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    
    return None


list = [1, 3, 5, 7, 9]
print (binary_search(list, 7))
print (binary_search(list, 4))