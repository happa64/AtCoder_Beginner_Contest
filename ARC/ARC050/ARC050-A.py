# https://atcoder.jp/contests/arc050/submissions/14378836
# A - 大文字と小文字
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    C, c = input().split()
    print("Yes" if C.lower() == c else "No")


if __name__ == '__main__':
    resolve()
