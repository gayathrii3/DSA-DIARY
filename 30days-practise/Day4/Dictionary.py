# ------------------------------------------------------
# *******************dictionary*************************
# ------------------------------------------------------

# dic = {"Name" : "Gayathri",
#        "Age": 20,
#        "marks" : {"english" : 23,
#                   "maths" : 43,
#                   "HINDI" : 21}
# }

# dic["Name"] = "Govind"
# dic["Hobby"] = "video games"
# dic

# print(dic.get("Hobby"))

# --------------------------------------------------------
# Frequency of elements

# nums = [1,2,2,3,1,1]
# dict = {}

# for n in nums:
#     if n in dict:
#         dict[n] += 1
#     else:
#         dict[n] = 1

# print(dict)

# --------------------------------------------------------
# First non-repeating character

# word = "swiss"

# for ch in word:
#     if word.count(ch) == 1:
#         print(ch)
#         break

# --------------------------------------------------------
# create dictionary from two lists

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]

# dict = {}

# for i in range(len(keys)):
#     dict[keys[i]] = values[i]

# print(dict)

# --------------------------------------------------------
# Group elements by frequency

# nums = [1, 2, 2, 3, 3, 3]

# dict = {}

# for i in nums:
#     if i not in dict:
#         dict[i] = [i]
#     else:
#         dict[i].append(i)

# print(dict)

# ---------------------------------------------------------
# Find element with highest frequency

# num  = [2, 2, 2, 3, 1, 1]
# freq = {}

# for i in num:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# max_count = 0
# answer = None

# for key in freq:
#     if freq[i] > max_count:
#         max_count = freq[i]
#         answer = key

# print(answer)

# -----------------------------------------------------
# Remove duplicates but keep order

# nums = [4, 2, 4, 1, 2, 5]
# dup = []

# for n in nums:
#     if n not in dup:
#         dup.append(n)
#         dup.sort()

# print(dup)

# ------------------------------------------------------
# Find common elements in two lists

# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6]

# common = []

# for i in a:
#     if i in b and i not in common:
#         common.append(i)

# print(common)

# -------------------------------------------------------
# Group words by length

# words = ["hi", "cat", "dog", "hello", "sun"]
# group = {}

# for word in words:
#     length = len(word)

#     if length not in group:
#         group[length] = [word]
#     else:
#         group[length].append(word)

# print(group)

# ----------------------------------------------------------
# Find second largest unique number

# nums = [10, 20, 20, 5, 30, 30]
# largest = sec_largest = float('-inf')

# for n in nums:
#     if n > largest:
#         sec_largest = largest
#         largest = n

#     elif n > sec_largest and n != largest:
#         sec_largest = n

# print(sec_largest)

# ---------------------------------------------------
# Count vowels in each word

# words = ["apple", "sky", "orange"]
# vowels = {}

# for word in words:
#     count = 0

#     for ch in word:
#         if ch.lower() in 'aeiou':
#             count += 1

#     vowels[word] = count

# print(vowels)

# -----------------------------------------------------
