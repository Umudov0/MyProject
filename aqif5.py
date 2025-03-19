def rotate_list(lst, k):
    if not lst or k == 0:
        return lst

    k = k % len(lst)

    rotated = lst[-k:] + lst[:-k]

    return rotated

print(rotate_list([1, 2, 3, 4, 5], 2))
