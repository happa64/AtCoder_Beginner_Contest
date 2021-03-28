# https://atcoder.jp/contests/abc197/submissions/21336318
# C - ORXOR
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = tuple(map(int, input().split()))

    res = f_inf
    for bit in range(1 << n):
        score = 0
        now = A[0]
        prev = 1 if bit & 1 else 0
        for mask in range(1, n):
            i = 1 if bit & (1 << mask) else 0
            if prev == i:
                now |= A[mask]
            else:
                score ^= now
                now = A[mask]
                prev = i
        score ^= now
        res = min(res, score)
    print(res)


if __name__ == '__main__':
    solve()
