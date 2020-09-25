# https://atcoder.jp/contests/joi2020yo2/submissions/15471903
# A - ポスター (Poster)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = [list(input()) for _ in range(n)]
    T = [list(input()) for _ in range(n)]

    res1 = 0
    res2 = 1
    res3 = 1
    res4 = 2
    for i in range(n):
        for j in range(n):
            if S[i][j] != T[i][j]:
                res1 += 1
            if S[i][j] != T[j][-(i + 1)]:
                res2 += 1
            if S[i][j] != T[-(j + 1)][i]:
                res3 += 1
            if S[i][j] != T[-(i + 1)][-(j + 1)]:
                res4 += 1
    res = min(res1, res2, res3, res4)
    print(res)


if __name__ == '__main__':
    resolve()
