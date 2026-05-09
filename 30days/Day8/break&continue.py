# -------------------break & continue----------------------

# print even numbers in range 

# i = 1
# while i <= 10:
#     if i % 2 != 0:
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

# -----------------------------------------------------------
# Stop when negative number appears

# n = int(input())
# nums = list(map(int, input().split()))

# for i in nums:
#     if i < 0:
#         break

#     print(i)

# ---------------------------------------------------------
# Skip multiples of 3

# n = 0

# while n <= 10:
#     n += 1
#     if n % 3 == 0:
#         continue

#     print(n)

# ---------------------------------------------------------
# First vowel in a string (break)

# word ="paranomal"

# for ch in word:
#     if ch in 'aeiou':
#         break

#     print(ch)

# --------------------------------------------------------
# Password checker (break + continue)

# while True:

#     password = input("Enter password : ")

#     if password == "":
#         continue

#     elif password == "gaya3":
#         print("Access granted")
#         break

#     else:
#         print("wrong password")

# -----------------------------------------------
# Skip spaces while printing characters

# word = "paranomal activities"

# for ch in word:
#     if ch == " ":
#         continue

#     print(ch,end="")

# -----------------------------------------------
# ATM PIN attempts

# correct_pin = '2345'
# attempts = 0

# while attempts < 3:

#     pin = input("Enter your pin : ")

#     if pin == correct_pin:
#         print("Access granted")
#         break

#     else:
#         print("wrong pin")
#         attempts += 1

# if attempts == 3:
#     print("Access denied")

# -------------------------------------------------
# Find first prime number in list

# nums = [4, 8, 9, 11, 15]

# for n in nums:
#     is_prime = True

#     if n < 2:
#         is_prime = False

#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 is_prime = False
#                 break
            
#     if is_prime:
#         print(n)
#         break




