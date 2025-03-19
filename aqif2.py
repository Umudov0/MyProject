def second_largest(lst):
    largest = second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest number"

    return second_largest

lst = [1, 2, 3, 3, 4, 5]
print("Second largest number:", second_largest(lst))
