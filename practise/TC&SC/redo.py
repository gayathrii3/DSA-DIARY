# Extraction of digits using loop

# num = 56789

# while num > 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10
    
# ------------------------------------------
# Count the number of digits                   --> log10(456343) = 5.6593 + 1 = 6 (count = 6)
# if the iteration is based on a SPECIFIC num  --> TC = O(log10(N)) , SC = O(1)

# num = 456343
# count = 0

# while num > 0:
#     digit = num % 10
#     count += 1
#     num = num // 10

# print(count)

# ------------------------------------------
# check PALINDROME ----> TC = O(log10(N))

# n = 131
# original = n
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = (reverse * 10) + digit
#     n = n // 10

# print(reverse == original)

# --------------------------------------------
# armstrong   TC = O(log10(N))

# n = 1634
# original = n
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit ** len(str(original))
#     n = n // 10
# print(total == original)

# ---------------------------------------------
# factors of the number    TC = O(sqrtN) + O(NlogN)  , SC = O(k) --> k = total no.of factors

# import math

# num = int(input())
# result = []

# for i in range(1, int(math.sqrt(num))+1):  
#     if num % i == 0:
#         result.append(i) 
#         if num // i != i:
#             result.append(num // i)

# result.sort() #O(nlogn)
# print(result)

# -----------------------------------------------
# store freq in dict

num = [1, 2, 1, 2, 3, 4, 5, 3]
freq = {}

for i in range(len(num)):
    # if num[i] in freq:
    #     freq[num[i]] += 1
    # else:
    #      freq[num[i]] = 1

    freq[num[i]] = freq.get(num[i], 0) + 1
     
print(freq)



