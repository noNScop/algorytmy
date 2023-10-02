def find_smallest(list):
    smallest = list[0]
    index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            index = i

    return index

def selection_sort(list):
    sorted = []
    while len(list) > 0:
        smallest = find_smallest(list)
        sorted.append(list.pop(smallest))

    return sorted
    

print(selection_sort([5, 3, 6, 2, 10]))