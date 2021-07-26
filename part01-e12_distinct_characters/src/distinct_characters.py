#!/usr/bin/env python3

def distinct_characters(L):
    ans = dict()
    for items in L:
        ans[items] = len(set(items)) 
    return ans

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
