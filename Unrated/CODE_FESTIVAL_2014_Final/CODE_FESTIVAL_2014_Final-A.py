# https://atcoder.jp/contests/code-festival-2014-final/submissions/14799715
# A - 50m走
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = int(input())
    print(50 / s)


if __name__ == '__main__':
    resolve()
