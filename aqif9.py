def majority_element(nums):
    n = len(nums)
    for num in set(nums):
        if nums.count(num) > n // 2:
            return num
    return None

print(majority_element([3, 3, 4, 2, 2, 2, 2]))
