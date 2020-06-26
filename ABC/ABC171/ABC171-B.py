# https://atcoder.jp/contests/abc171/submissions/14687852
# B - Mix Juice
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    P = sorted(list(map(int, input().split())))
    res = sum(P[:k])
    print(res)


if __name__ == '__main__':
    resolve()
