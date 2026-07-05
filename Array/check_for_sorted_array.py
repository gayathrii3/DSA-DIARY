num = list(map(int, input().split()))
n = len(num)

for i in range(n-1):
    if num[i] > num[i + 1]:
        print(False)
        break
else:
    print(True)