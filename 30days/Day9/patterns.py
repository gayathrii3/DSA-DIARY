# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# for i in range(4):             # i tells which num needs to be printed
#     for j in range(5):         # j tells how many times the num needs to be printed
#         print("*",end=" ")
#     print()

# ------------------------------------------------------------------
# right triangle pattern

# * 
# * * 
# * * * 
# * * * * 

# for i in range(4):
#     for j in range(i+1):
#         print('*', end=" ")
#     print()

# -------------------------------------------------------------------
# inverted triangle

# * * * * 
# * * * 
# * * 
# * 

# n = int(input())

# for i in range(n):
#     for j in range(n-i):
#         print('*', end=" ")
#     print()

# ------------------------------------------------------------------
# number square

# 1 2 3 
# 1 2 3 
# 1 2 3 

# n = int(input())

# for i in range(n):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()

# -------------------------------------------------------------------
# increasing triangle  ( 1 ----> i+1)

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 

# n = int(input())

# for i in range(1, n):
#     for j in range(1, i+1):
#         print(j,end=" ")
#     print()

# ------------------------------------------------------------------
# same number triangle (print i times)

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 

# n = int(input())

# for i in range(1, n):
#     for j in range(1, i+1):
#         print(i,end=" ")
#     print()

# -------------------------------------------------------
# 