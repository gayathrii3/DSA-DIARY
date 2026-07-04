# 26 Remove Duplicates from Sorted Array

def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0
    for num in nums[1:]:
        if num != nums[i]:
            i += 1
            nums[i] = num

    return i + 1


nums = [1, 1, 2, 2, 3, 4, 4]

length = remove_duplicates(nums)

print("Length:", length)
print("Unique elements:", nums[:length])

# ------------------------------------------------------ TC = O(n)

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         if not nums:
#             return 0
#         i = 0 
#         for j in range(1, len(nums)):
#             if nums[j] != nums[i]:
#                 i += 1
#                 nums[i] = nums[j]

#         return i + 1
