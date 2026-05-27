# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def single_number(nums):
    single = 0

    for n in nums:
        single = single ^ n

    return single

nums = [2, 2, 1, 7, 1]

print(single_number(nums))

