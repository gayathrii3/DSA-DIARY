# While loop
# --------------------------------

# count = 1
# while count <= 5:
#     print("Gayathri")
#     count += 1

# -----------------------------------

# n = int(input())

# i = 1
# while i <= n:
#     print(i, "Gayathri")   #----------> ( i ) is for checking teh no. of times the loop is running
#     i += 1

# -----------------------------------
# print num from 1 to n

# n = int(input())

# i = 1
# while i <= n:
#     print(i)
#     i += 1

# -----------------------------------
# print num from 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# -----------------------------------
# from 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# ------------------------------------
# multiplication table of n

# n = int(input("Enter a num: "))

# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i+=1

# ------------------------------------
# print the numbers in the list using loop

# num = [1, 4, 6, 8, 2, 0, 7]

# for i in num:
#     print(i)

# ------------------------------------
# search for x in the list using loop

# n = int(input("Enter range: "))
# nums = list(map(int, input().split()))

# x = int(input("Enter x :"))

# for i in nums:
#     if i == x:
#         print(f"{x} found at index {nums.index(i)}")
#         break
# else:
#     print(f"{x} not in the list")

# ------------------------------------
# Reverse a number (using while loop)

# num = int(input("Enter a number : "))
# reverse = 0

# while num > 0:
#     last_digit = num % 10
#     reverse = reverse * 10 + last_digit
#     num //= 10

# print(reverse)

# -------------------------------------
# Check if number is palindrome

# n = int(input())
# orginal = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# if orginal == rev:
#     print(f"{orginal} is palindrome")
# else:
#     print(f"{orginal} is not a palindrome")

# ---------------------------------------------
# Find largest digit in a number

# n = int(input())
# largest = 0

# while n > 0:
#     digit = n % 10

#     if digit > largest:
#         largest = digit

#     n //= 10

# print(largest)

# -----------------------------------------------
# Armstrong number

# n = 153
# orginal = n
# sum = 0

# if n < 0:
#     print("Invalid input")
# else:
#     while n > 0:
#         digit = n % 10
#         sum += digit ** len(str(orginal))
#         n //= 10

#     print("ARMSTROMG" if sum == orginal else "not armstrong")

# -----------------------------------------------------------------
# Count frequency of a digit

# n = int(input("Enter number: "))
# freq = {}

# while n > 0:
#     digit = n % 10
#     if digit in freq:
#         freq[digit] += 1
#     else:
#         freq[digit] = 1

#     n //= 10

# print(freq)

