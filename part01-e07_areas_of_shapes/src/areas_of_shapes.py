#!/usr/bin/env python3

import math

def triangle():
    "This function calculates the area of a triangle"
    base = int(input("Give base of the triangle: "))
    height = int(input("Give height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area is {area}")


def circle():
    "This function calculates the area of a circle"
    radius = int(input("Give radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area is {area}")


def rect():
    "This function calculates the area of a rectangle"
    width = int(input("Give width of the rectangle: "))
    height = int(input("Give height of the rectangle: "))
    area = width * height
    print(f"The area is {area}")


def main():
    while True:
        choice = input("Choose a shape (triangle, rectangle, circle): ")
        if choice == "":
            break
        elif choice == "triangle":
            triangle()
        elif choice == "rectangle":
            rect()
        elif choice == "circle":
            circle()
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
