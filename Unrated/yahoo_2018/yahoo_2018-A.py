# https://atcoder.jp/contests/yahoo-procon2018-qual/submissions/15395157
# A - yahoo
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print("YES" if s[:3] == "yah" and s[3] == s[4] else "NO")


if __name__ == '__main__':
    resolve()
