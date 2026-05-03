# Check if a number is prime

# n = int(input())

# if n > 1:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             print(n, "not prime")
#             break
#         else:
#             print(n, "is prime")
# else:
#     print(n, "not prime")

# -----------------------------------------------------
# Find factorial using conditions (no loops if possible)

# n = int(input())
# fact = 1

# for i in range(1,n+1):
#     fact *= i

# print(fact)

# -----------------------------------------------------
# Check if string contains only digits

# n = "12ab4c5"
# n2 = ""

# for i in n:
#     if i.isdigit():
#         n2 += i
#     else:
#         n2 += "$"

# print(n2)       

# ------------------------------------------------------
# Count uppercase, lowercase, digits in string

# n = "GayaThRii3300"
# upper = 0
# lower = 0
# digit = 0

# for ch in n:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     elif ch.isdigit():
#         digit += 1
# print(f"lower = {lower}, upper = {upper}, digits = {digit}")

# ----------------------------------------------------------------
# Find second largest number

# n = [12, 6, 35, 78]
# largest = sec_largest = float('-inf') 
#       #n[0]  starts with lowest value
# for i in n:
#     if i > largest:
#         sec_largest = largest
#         largest = i

#     elif i > sec_largest and i != largest:
#         sec_largest = i

# print(sec_largest)
