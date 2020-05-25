# https://atcoder.jp/contests/abc029/submissions/13586184
# C - Brute-force Attack
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    def dfs(L):
        if len(L) == n:
            res.append("".join(L))
            return

        for s in ["a", "b", "c"]:
            L.append(s)
            dfs(L)
            L.pop()

    res = []
    dfs([])

    for i in res:
        print(i)


if __name__ == '__main__':
    resolve()
