# Check if a string is a valid palindrome ignoring case.

s = input().lower()

if s == s[::-1]:
    print("palindrome")

else:
    print("Not palindrome")