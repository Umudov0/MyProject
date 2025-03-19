def most_frequent_element(lst):
    frequency = {}

    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    most_frequent = None
    max_count = 0

    for num in frequency:
        if frequency[num] > max_count:
            most_frequent = num
            max_count = frequency[num]

    return most_frequent

lst = [1, 2, 3, 3, 2, 2, 1, 3, 4, 5]
print("Most frequent element:", most_frequent_element(lst))
