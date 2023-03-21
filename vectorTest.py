from vector import Vector3D
from typing import List, Callable
from colorama import Fore, Style


def vec_create_test() -> int:
    a = Vector3D(2, 4, 6)
    b = Vector3D(5, 2, 1)
    if (a.x != 2 or a.y != 4 or a.z != 6):
        return 1
    if (b.x != 5 or b.y != 2 or b.z != 1):
        return 2
    return 0

def vec_add_test() -> int:
    a = Vector3D(-2, 4, -90)
    b = Vector3D(18, 2, -2)
    c = a + b
    if (c.x != 16 or c.y != 6 or c.z != -92):
        return 1
    a += b
    if (a.x != c.x or a.y != c.y or a.z != c.z):
        return 2
    return 0

def vec_dot_test() -> int:
    a = Vector3D(1, 1, 1)
    b = Vector3D(2, 2, 2)
    res = a.dot(b)
    if (res != 6):
        return 1
    a.x, a.y, a.z = 80, 20, 100
    res = a * b
    if (res != 400):
        return 2
    b.x, b.y, b.z = -1, -1, -1
    res = a * b
    if (res != -200):
        return 3
    return 0

def vec_cross_test() -> int:
    a = Vector3D(50, 50, 50)
    b = Vector3D(-100, 2, 0)
    c = a.cross(b)
    if (c.x != -100 or c.y != -5000 or c.z != 5100):
        return 1
    a.x, a.y, a.z = -50, -50, -50
    c = a.cross(b)
    if (c.x != 100 or c.y != 5000 or c.z != -5100):
        return 2
    c = b.cross(a)
    if (c.x != -100 or c.y != -5000 or c.z != 5100):
        return 3
    c = a.cross(a)
    if (c.x != 0 or c.y != 0 or c.z != 0):
        return 4
    c = b.cross(b)
    if (c.x != 0 or c.y != 0 or c.z != 0):
        return 5
    return 0

def test(functions: List[Callable]) -> None:
    for f in functions:
        try:
            test_case = f()
            if (test_case):
                raise RuntimeError("Test " + str(test_case))
            print(f.__name__ + ":", Fore.GREEN + "PASSED")
        except Exception as e:
            print("Error in", f.__name__ + ":", str(e) + ":", Fore.RED + "FAIL")
        print(Style.RESET_ALL, end='')
            
def main():
    print("Starting tests...")
    functions = [vec_add_test, vec_create_test, vec_dot_test, vec_cross_test]
    test(functions)
    print("Finished")

if __name__ == "__main__":
    main()
