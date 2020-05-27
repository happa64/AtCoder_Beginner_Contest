# https://atcoder.jp/contests/soundhound2018-summer-qual/submissions/13630556
# A - F
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print("+" if a + b == 15 else "*" if a * b == 15 else "x")


if __name__ == '__main__':
    resolve()
