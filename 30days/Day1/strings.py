# Print length of a string

# name = "Gayathri"

# print(len(name))

# ------------------------------------------------------------
# Convert string to uppercase and lowercase

# name = "gayathri"

# upper = name.upper()
# lower = name.lower()

# print("Uppercase =", upper)
# print("Lowercase =", lower)

# -----------------------------------------------------------
# Check if a string starts with "A"

# word = str(input())

# if word.startswith("A"):
#     print(word, "starts with A")
# else:
#     print(word, "doesn't start with A")

# -----------------------------------------------------------
# Reverse a string

# name = "Gayathri"
# reverse = ""

# for ch in range(len(name)-1, -1, -1):
#     reverse += name[ch]

# print(reverse)

# ------------------------------------------------------------
# Count number of vowels in a string

# name = "gayathri"
# count = 0

# for ch in name:
#     if ch in "aeiou":
#         count += 1

# print(count)

# -------------------------------------------------------------
# Check if a string is palindrome

# word = "pop"
# reverse = ""

# for ch in range(len(word)-1, -1, -1):
#     reverse += word[ch]
# if reverse == word:
#     print(word, "is palindrome")
# else:
#     print("not palindrome")

# -------------------------------------------------------------
# Count words in a sentence

# words = "I need the whole stadium to jump put your phones down and get all the fun"
# word = words.split()

# count = 0

# for w in word:
#     count += 1

# print(count)

# ---------------------------------------------------------------
# Remove spaces from a string

# words = "I need the whole stadium to jump put your phones down and get all the fun"

# words = words.replace(" ", "")
# print(words)

# ----------------------------------------------------------------
# Find first non-repeating character

# name = "gayatthrii"

# for ch in name:
#     if name.count(ch) == 1:

#         print("first non-repeating characters", ch)
#         break

# ----------------------------------------------------------------
# Replace all vowels with *

# word = "lollapaloza"
# vowels = "aeiou"
# result = ""

# for ch in word:
#     if ch in vowels:
#         result += "*"
#     else:
#         result += ch

# print(result)
# ---------------------------------
# for ch in "aeiouAEIOU":
#     word = word.replace(ch,"*")
# print(word)


# -------------------------------------------------------------
# ************************Conditionals*************************
# -------------------------------------------------------------

# Check if a number is even or odd

# n = int(input("Enter num ="))

# if n % 2 == 0:
#     print(n, "is an even number")
# else:
#     print(n, "is an odd number")

# -------------------------------------------------------------
# Check if a number is positive, negative, or zero

# n = float(input())

# if n > 0:
#     print(n, "is a positive number")
# elif n < 0:
#     print(n, "is a negative number")
# else:
#     print("zero")

# -------------------------------------------------------------
# Find largest of two numbers

# a = int(input())
# b = int(input())

# print(a if a > b else b)

# -------------------------------------------------------------
# Check if a person is eligible to vote (age ≥ 18)

# age = int(input("Enter age : "))

# if age < 18:
#     print("Not eleigible to vote")
# elif age >= 18:
#     print("eligible to vote")

# -------------------------------------------------------------
# Check if a number is divisible by 5

# num = int(input("Enter a number: "))

# if num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 5")