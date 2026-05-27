# Given a binary array nums and an int k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's
# i/p: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2(flips)
# o/p: 6
# -------------------------------------------------------------------[ Sliding window technique ]

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

def max_consecutive_ones(nums, k):

    left = 0
    zeros = 0
    maximum = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            zeros += 1

        while zeros > k:

            if nums[left] == 0:
                zeros -= 1

            left += 1

        maximum = max(maximum, right - left + 1)

    print(maximum)

max_consecutive_ones(nums, k)