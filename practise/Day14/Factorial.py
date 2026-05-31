def find_factorial(n):

    fact = 1
    for i in range(1, n+1):
        # print(i)
        fact *= i
    return fact

print(find_factorial(5))