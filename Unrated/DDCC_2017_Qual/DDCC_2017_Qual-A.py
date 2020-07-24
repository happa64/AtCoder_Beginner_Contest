# https://atcoder.jp/contests/ddcc2017-qual/submissions/15394789
# A - DDCC型文字列
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print("Yes" if s[0] == s[1] and s[1] != s[2] and s[2] == s[3] else "No")


if __name__ == '__main__':
    resolve()
