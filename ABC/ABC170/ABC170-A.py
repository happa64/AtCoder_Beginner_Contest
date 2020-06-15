# https://atcoder.jp/contests/abc170/submissions/14283832
# A - Five Variables
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = list(map(int, input().split()))
    print(x.index(0) + 1)


if __name__ == '__main__':
    resolve()
