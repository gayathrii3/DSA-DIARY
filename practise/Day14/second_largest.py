arr = list(set(map(int, input().split())))

largest = sec_largest = float('-inf')

for n in arr:
    if n > largest:
        sec_largest = largest
        largest = n

    elif n > sec_largest and n != largest:
        sec_largest = n

print(sec_largest)