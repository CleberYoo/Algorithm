A, B = input().split()

A = int(A)
B = int(B)

print(A * (B % 10))
print(A * (B % 100 // 10))
print(A * (B // 100))
print(A * B)