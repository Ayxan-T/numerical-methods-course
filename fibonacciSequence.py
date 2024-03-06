# prints n first elements of fibonacci sequence
n = int(input())
a = 0
b = 1
for i in range(0, n):
    print(a, end=' ')
    temp = a + b
    a = b
    b = temp
