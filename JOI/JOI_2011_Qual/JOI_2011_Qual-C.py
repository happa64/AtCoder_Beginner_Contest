# https://atcoder.jp/contests/joi2011yo/submissions/15050474
# C - タイル (Tile)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        a = min(n - a + 1, a)
        b = min(n - b + 1, b)
        c = min(a, b)
        res = 3 if c % 3 == 0 else c % 3
        print(res)


if __name__ == '__main__':
    resolve()
