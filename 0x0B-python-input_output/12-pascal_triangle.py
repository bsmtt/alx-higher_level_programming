#!/usr/bin/python3
if __name__ == "__main__":

def pascal_triangle(n):
    ls = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            ls.append(j)
    return ls
