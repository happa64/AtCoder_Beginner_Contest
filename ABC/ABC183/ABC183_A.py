# https://atcoder.jp/contests/abc183/submissions/18116493
# A - ReLU
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    if x >= 0:
        print(x)
    else:
        print(0)


if __name__ == '__main__':
    resolve()
