def print_area(width = 1, height = 2):
       area = width * height
       print(area)

def box(width= 1, height =2, symbol = "*"):
    box = ""
    for i in range(width):
        for j in range(height):
            box += symbol
        box += "\n"

    return box

def main():
    print_area()
    print(box())

    print_area(4, 3)
    print(box(4, 3))

    print_area(height = 5, width = 3)
    print(box(height = 5, width = 3, symbol="?"))

    print_area(width = 2)
    print(box(width = 2))

    print_area(height = 6)
    print(box(6))
main()
