# https://atcoder.jp/contests/abc031/submissions/14014966
# B - 運動管理
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    l, h = map(int, input().split())
    n = int(input())

    for _ in range(n):
        a = int(input())
        if l <= a <= h:
            print(0)
        elif a < l:
            print(l - a)
        else:
            print(-1)


if __name__ == '__main__':
    resolve()
