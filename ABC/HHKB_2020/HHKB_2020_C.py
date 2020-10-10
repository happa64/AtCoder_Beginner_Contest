# https://atcoder.jp/contests/hhkb2020/submissions/17298916
# C - Neq Min
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    P = list(map(int, input().split()))

    used = set()
    i = 0
    for p in P:
        used.add(p)
        while i in used:
            i += 1
        print(i)


if __name__ == '__main__':
    resolve()
