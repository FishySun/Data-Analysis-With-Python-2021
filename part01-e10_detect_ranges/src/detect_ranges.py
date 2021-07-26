#!/usr/bin/env python3

def detect_ranges(L):
    """This functions sorts the given list and returns a transformed list
    where pairs are used for all the detected intervals"""
    l = sorted(L)
    ans = list()
    start = -1
    inside = False
    ans.append(l[0])
    for i in range(1, len(l)):
        if l[i] == l[i-1] + 1:
            if inside:
                ans.pop(-1)
                ans.append((start, l[i]+1))
            else:
                start = l[i-1]
                ans.pop(-1)
                ans.append((start, l[i]+1))
                inside = True
        else:
            ans.append(l[i])
            inside = False
    return ans


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
