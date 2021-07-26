#!/usr/bin/env python3

def square(i):
    "This function returns the square of its parameter"
    return i ** 2

def triple(i):
    "This function multiplies its parameter by three"
    return 3 * i

def main():
    for i in range(1, 11):
        sq = square(i)
        tr = triple(i)
        if sq > tr:
            break
        print(f"triple({i})=={tr} square({i})=={sq}")

if __name__ == "__main__":
    main()
