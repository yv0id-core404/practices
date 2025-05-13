# Radian-Degree Converter
# made by Yair Thura Linn

from math import pi

# pi value = 3.1415... written
PI = pi

def r2d(): # Radian to degree
    # Write your code here
    rad_value = 0
    degree_value = 0
    rad_value = float(input("Enter the radian value to convert to degree value: "))
    degree_value = rad_value * (180 / PI)
    print("The degree value for ", rad_value, "is ", degree_value, " degrees.")

def d2r(): # Degree to radian
    # Write your code here
    rad_value = 0
    degree_value = 0
    degree_value = float(input("Enter the degree value to convert to radian value: "))
    rad_value = degree_value * (PI / 180)
    print("The radian value for ", degree_value, "is ", rad_value, ".")


def main():
    print('''Rad-Deg Calculator:
    1. Radian to Degree convert
    2. Degree to Radian convert
    3. Exit''')
    choice = 0
    choice = int(input("Enter your option: "))
    while choice != 3:
        if choice == 1:
            r2d()
        elif choice == 2:
            d2r()
        else:
            print("Error. Wrong command.")
            break

main()
