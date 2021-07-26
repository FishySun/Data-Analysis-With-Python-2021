#!/usr/bin/env python3

def interleave(*lists):
   return [i for tup in zip(*lists) for i in tup]

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
