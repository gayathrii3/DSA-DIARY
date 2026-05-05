# num = [1, 8, 0, 9, 0, 0, 6, 7]
# result = []

# for n in num:
#     if n != 0:
#         result.append(n)

# result = result + [0] * num.count(0)
# print(result)

# -----------------------------------------------
# sum of First N Natural numbers

# n = int(input())
# sum = 0

# for i in range(1,n+1):
#     sum += i

# print(sum)

# ------------------------------------------------
# sum of digits in a num

# num = int(input())
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum += digit
#     num //= 10

# print(sum)

# --------------------------------------------------
# Harshad number      (A Number that is divisible by the sum of it's digits is known as a Harshad number.)

# n = int(input())
# original = n
# sum = 0

# while n > 0:
#     digits = n % 10
#     sum += digits
#     n //= 10

# if n % sum == 0:
#     print(original, "is a harshad number")
# else:
#     print(original, " not harshad")

# --------------------------------------------------
# abundunt number  (A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.)

# num = int(input())
# sum_fact = 0

# for i in range(2,num):
#     if num % i == 0:
#         sum_fact += i

# if sum_fact > num:
#     print(num, "is an abundant number")
# else:
#     print(num, "not a AN")

# .-------------------------------------------------

