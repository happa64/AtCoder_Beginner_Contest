# https://atcoder.jp/contests/abc192/submissions/20282048
# A - Star
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    res = 100 - x % 100
    print(res)


if __name__ == '__main__':
    resolve()
