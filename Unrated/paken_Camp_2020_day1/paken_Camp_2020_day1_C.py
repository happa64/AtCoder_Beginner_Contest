# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19531065
# C - 皆勤賞
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = set()
    for i in range(n):
        _ = int(input())
        if i == 0:
            res |= set(input().split())
        else:
            res &= set(input().split())
    print(len(res))


if __name__ == '__main__':
    resolve()
