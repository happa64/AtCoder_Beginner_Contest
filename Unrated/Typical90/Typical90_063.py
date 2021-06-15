# https://atcoder.jp/contests/typical90/submissions/23363093
# 063 - Monochromatic Subgrid（★4）
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    P = tuple(tuple(map(int, input().split())) for _ in range(H))

    res = 0
    for bit in range(1 << H):
        T = []
        for mask in range(H):
            if bit & (1 << mask):
                T.append(P[mask])
        m = bin(bit).count("1")
        num_dict = defaultdict(int)
        for w in range(W):
            S = tuple(T[h][w] for h in range(m))
            if len(set(S)) == 1:
                num_dict[S[0]] += m
        max_score = 0
        for v in num_dict.values():
            max_score = max(max_score, v)
        res = max(res, max_score)
    print(res)


if __name__ == '__main__':
    solve()
