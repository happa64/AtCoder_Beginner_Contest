# https://atcoder.jp/contests/abc167/submissions/13021637
# A - Registration
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    t = input()
    n = len(s)

    for i in range(n):
        if s[i] != t[i]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
