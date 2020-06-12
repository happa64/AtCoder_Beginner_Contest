# https://atcoder.jp/contests/abc046/submissions/12407494
# B - AtCoDeerくんとボール色塗り
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    print(k * pow(k - 1, n - 1))


if __name__ == '__main__':
    resolve()
