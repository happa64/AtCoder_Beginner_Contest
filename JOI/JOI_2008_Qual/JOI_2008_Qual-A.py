# https://atcoder.jp/contests/joi2008yo/submissions/15088645
# A - おつり
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    r = 1000 - n

    res = 0
    for coin in [500, 100, 50, 10, 5, 1]:
        q, r = divmod(r, coin)
        res += q
    print(res)


if __name__ == '__main__':
    resolve()
