# https://atcoder.jp/contests/donuts-2015/submissions/14879886
# A - ドーナツの体積
import sys
import math
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    r, d = map(int, input().split())
    res = (2 * d * math.pi) * (pow(r, 2) * math.pi)
    print(res)


if __name__ == '__main__':
    resolve()
