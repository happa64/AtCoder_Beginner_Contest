# https://atcoder.jp/contests/abc062/submissions/13399246
# A - Grouping
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    A = [1, 3, 5, 7, 8, 10, 12]
    B = [4, 6, 9, 11]
    C = [2]
    if x in A and y in A:
        print("Yes")
    elif x in B and y in B:
        print("Yes")
    elif x in C and y in C:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
