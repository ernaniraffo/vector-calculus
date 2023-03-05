from math import sqrt

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return self + other

    def sub(self, other):
        return self - other

    def dot(self, other):
        return self * other

    def cross(self, other):
        i = self.y * other.z - self.z * other.y
        j = self.z * other.x - self.x * other.z
        k = self.x * other.y - self.y * other.x
        return Vector3D(i, j, k)
    
    def length(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        length = self.length()
        self /= length
        
    def projection(self, other):
        scalar = (other * self) / other.length()**2
        return Vector3D(other.x * scalar, other.y * scalar, other.z * scalar)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __truediv__(self, num):
        return Vector3D(self.x / num, self.y / num, self.z / num)
    
    def __itruediv__(self, num):
        self.x /= num
        self.y /= num
        self.z /= num

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
