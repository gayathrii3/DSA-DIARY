# Find Missing Number in a List(only one number)

def missing_num(nums):

    n = len(nums) + 1

    expected_sum = n * (n + 1)//2

    actual_sum = 0

    for num in nums:
        actual_sum += num

    return expected_sum - actual_sum

print(f"missing number = {missing_num([1, 3, 4, 5, 6, 7])}")
    

