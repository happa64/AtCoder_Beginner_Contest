# https://atcoder.jp/contests/abc009/tasks/abc009_1
# A - 引越し作業
import sys
import math
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print(math.ceil(n / 2))


if __name__ == '__main__':
    resolve()
