def armstrong(n):
    original = n
    digits = len(str(n))
    sum = 0
    
    while n > 0:
        last_digit = n % 10
        sum += last_digit ** digits
        n //= 10

    if sum == original:
        return "Armstrong"
    
    else:
        return "Not Armstrong"
    
print(armstrong(157))