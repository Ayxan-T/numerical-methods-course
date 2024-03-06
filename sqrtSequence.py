# sqrt(5 + sqrt(10 + sqrt(15 + sqrt(20 + ... + sqrt(95)))..))
from math import sqrt
a = 95
res = 95
while (a != 0):
    res = a - 5 + sqrt(res)
    a = a - 5
print(res)
