def sum_loop(numbers):
    total = 0
    for number in numbers:
        total += number
    
    return total


def sum_recurrency(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers.pop() + sum_recurrency(numbers)


def count_elements(numbers):
    if not numbers:
        return 0
    else:
        return 1 + count_elements(numbers[1:])
    

def max_value(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 2:
        return numbers[0] if numbers[0] > numbers[1] else numbers[1]
    
    minor_max = max_value(numbers[1:])            
    return numbers[0] if numbers[0] > numbers[1] else minor_max


print(sum_recurrency([1, 2, 3, 4, 5]))
print(count_elements([1, 2, 3, 4, 5]))
print(max_value([1, 2, 3, 4, 5, 6]))
print(sum_recurrency([]))
print(max_value([]))