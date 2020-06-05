# https://atcoder.jp/contests/abc036/submissions/14015070
# B - 回転
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = [list(input()) for _ in range(n)]

    res = [[""] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = S[j][i]

    for i in res:
        print("".join(i[::-1]))


if __name__ == '__main__':
    resolve()
