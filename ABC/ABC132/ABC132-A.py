# https://atcoder.jp/contests/abc132/submissions/13687001
# A - Fifty-Fifty
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print("Yes" if len(set(s)) == 2 else "No")


if __name__ == '__main__':
    resolve()
