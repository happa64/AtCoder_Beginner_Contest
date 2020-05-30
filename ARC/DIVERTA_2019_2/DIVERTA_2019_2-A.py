# https://atcoder.jp/contests/diverta2019-2/submissions/13700311
# A - Ball Distribution
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    res = n - k
    print(res if k != 1 else 0)


if __name__ == '__main__':
    resolve()
