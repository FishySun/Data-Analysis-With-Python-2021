#!/usr/bin/env python3

def reverse_dictionary(d):
    ans = dict()
    for key, value in d.items():
        for item in value:
            if item in ans:
                ans[item].append(key)
            else:
                ans[item] = list()
                ans[item].append(key) 

    return ans

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
