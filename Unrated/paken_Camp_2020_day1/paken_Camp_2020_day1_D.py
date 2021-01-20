# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19532000
# D - 立方体を壊せ！
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    if k <= n:
        print(pow(k, 3))
    elif k <= n * 2:
        print(pow(k, 3) - pow(k - n, 3) * 3)
    elif k <= n * 3:
        print(pow(n, 3) * 6 - pow(n * 3 - k, 3))
    else:
        print(pow(n, 3) * 6)


if __name__ == '__main__':
    resolve()
