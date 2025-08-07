#!/usr/bin/env python3
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))


# by Juan

for i in range(100001):
    print(i)