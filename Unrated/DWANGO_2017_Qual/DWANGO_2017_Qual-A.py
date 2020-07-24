# https://atcoder.jp/contests/dwacon2017-prelims/submissions/15395433
# A - 動画検索
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    res = max(0, a + b - n)
    print(res)


if __name__ == '__main__':
    resolve()
