from vector import Vector3D

a = Vector3D(2, 4, 6)
print("a:", a)

b = Vector3D(5, 2, 1)
print("b:", b)

a = a + b
print("a = a + b =", a)

print("b · a =", b * a)
print("b - a=", b - a)

print("a.length() =", a.length())
a.normalize()
print("normalize(a) =", a)

c = a.projection(b)
print("c = a.projection(b) =", c)

