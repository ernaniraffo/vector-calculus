from vector import Vector3D
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

def main():
    print("Starting tests...")
    
    try:
        t = vec_create_test()
        if (t != 0):
            raise RuntimeError("Test " + str(t))
        print("vec_create_test:", Fore.GREEN + "PASSED" + Style.RESET_ALL)
    except Exception as e:
        print("Error in vec_create_test:", str(e) + ":", Fore.RED + "FAIL")
    
    try:
        t = vec_add_test()
        if (t != 0):
            raise RuntimeError("Test " + str(t))
        print("vec_add_test:", Fore.GREEN + "PASSED")
    except Exception as e:
        print("Error in vec_add_test:", str(e) + ":", Fore.RED, "FAIL" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
