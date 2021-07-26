#!/usr/bin/env python3

def find_matching(L, pattern):
    ans = list()
    for i, x in enumerate(L):
        if pattern in x:
            ans.append(i)
    return ans

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")

if __name__ == "__main__":
    main()
