#!/usr/bin/env python3
# Created by: Andrei Chirilov
# Created on: Septemeber 2019
# This program calculates the area and perimeter of a rectangle
# with user input


def main():

    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))

    area = length*width
    perimeter = 2*(length+width)

    print("")
    print("Area is {}mm2".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
