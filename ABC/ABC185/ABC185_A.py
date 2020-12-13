# https://atcoder.jp/contests/abc185/submissions/18721369
# A - ABC Preparation
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = list(map(int, input().split()))
    print(min(A))


if __name__ == '__main__':
    resolve()
