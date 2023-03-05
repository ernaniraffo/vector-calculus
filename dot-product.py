#!/bin/python3

dimension = int(input("Enter dimension: "))
a = tuple(map(int, input("Enter vector a components: ").split()))
b = tuple(map(int, input("Enter vector b components: ").split()))

res = 0
for i in range(dimension):
    res += a[i] * b[i]

print(a, "·", b, "=", res)
