#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    root1= (-b + math.sqrt(b ** 2 - 4 * a * c)) / ( 2 * a )
    root2= (-b - math.sqrt(b ** 2 - 4 * a * c)) / ( 2 * a )
    return (root1, root2)

def main():
    pass

if __name__ == "__main__":
    main()
