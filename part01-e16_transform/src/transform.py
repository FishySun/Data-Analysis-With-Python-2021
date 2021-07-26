#!/usr/bin/env python3

def transform(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    return list(map(lambda x: int(x[0]) * int(x[1]), list(zip(s1, s2))))


def main():
    pass

if __name__ == "__main__":
    main()
