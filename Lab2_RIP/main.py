from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синий", 15, 15)
    c = Circle("зеленый", 15)
    s = Square("красный", 15)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
