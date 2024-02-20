#!/usr/bin/python3
"""
    pascal module
"""


if __name__ == "__main__":
    def pascal_triangle(n):
        """ pascal triangle"""
        ls = []
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                ls.append(j)
        return ls
