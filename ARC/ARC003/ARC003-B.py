# https://atcoder.jp/contests/arc003/submissions/13586123
# B - さかさま辞書
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = []
    for _ in range(n):
        s = input()
        S.append(s[::-1])

    S = sorted(S)

    for res in S:
        print(res[::-1])


if __name__ == '__main__':
    resolve()
