#!/usr/bin/env python3

def merge(L1, L2):
    "Merge two sorted list L1 and L2 without changing the original"
    Left = L1.copy()
    Right = L2.copy()

    L = list()
    i = 0
    j = 0

    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            L.append(Left[i])
            i += 1
        else:
            L.append(Right[j])
            j += 1
    while i < len(Left):
        L.append(Left[i])
        i += 1
    while j < len(Right):
        L.append(Right[j])
        j += 1
    return L


def main():
    pass

if __name__ == "__main__":
    main()
