# https://atcoder.jp/contests/typical90/submissions/21908204
# 004 - Cross Sum（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    A = tuple(tuple(map(int, input().split())) for _ in range(H))

    R = [sum(A[h]) for h in range(H)]
    C = [0] * W
    for w in range(W):
        for h in range(H):
            C[w] += A[h][w]

    res = [[R[h] + C[w] - A[h][w] for w in range(W)] for h in range(H)]
    for i in res:
        print(*i)


if __name__ == '__main__':
    solve()
