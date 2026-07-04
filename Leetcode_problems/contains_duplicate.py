# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

nums = [1,2,3,1]

def duplicate(nums):

    for n in nums:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
    
print(duplicate(nums))
