# Find Duplicate Elements in a List

def find_duplicates(nums):

    seen = []
    dup = []

    for n in nums:

        if n in seen and n not in dup:
            dup.append(n)

        else:
            seen.append(n)

    return dup

print(find_duplicates([1, 1, 4, 4, 6, 6, 8, 9]))
