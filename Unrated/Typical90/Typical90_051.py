# https://atcoder.jp/contests/typical90/submissions/22948445
# 051 - Typical Shop（★5）
import sys
from collections import defaultdict
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    N, K, P = map(int, input().split())
    A = tuple(map(int, input().split()))

    B = A[:N // 2]
    C = A[N // 2:]

    S = defaultdict(list)
    for bit in range(1 << len(B)):
        key = bin(bit).count("1")
        if key > K:
            continue
        tot = 0
        for mask in range(len(B)):
            if bit & (1 << mask):
                tot += B[mask]
        S[key].append(tot)

    T = defaultdict(list)
    for bit in range(1 << len(C)):
        key = bin(bit).count("1")
        if key > K:
            continue
        tot = 0
        for mask in range(len(C)):
            if bit & (1 << mask):
                tot += C[mask]
        T[key].append(tot)

    for i in range(K + 1):
        S[i].sort()
        T[i].sort()

    res = 0
    for i in range(K + 1):
        j = K - i
        for v in S[i]:
            idx = bisect_right(T[j], P - v)
            res += idx
    print(res)


if __name__ == '__main__':
    solve()
