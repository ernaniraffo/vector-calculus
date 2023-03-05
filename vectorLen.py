from math import sqrt
a = list(map(int, input("Enter components of a: ").split()))
res = 0
for n in a:
    res += n**2
print(f"√{res} = {sqrt(res)}")
