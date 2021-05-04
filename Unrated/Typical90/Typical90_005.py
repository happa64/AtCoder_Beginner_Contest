import sys
import numpy as np
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, b, k = map(int, input().split())
    C = tuple(map(int, input().split()))

    A = [[0] * b for _ in range(b)]
    for i in range(b):
        for c in C:
            A[i][(i * 10 + c) % b] += 1
    A = np.array(A, dtype=np.int64)

    Mat = [deepcopy(A)]
    m = n.bit_length()
    for _ in range(m):
        Mat.append(A @ Mat[-1] % MOD)

    res = np.array([1] + [0] * (b - 1), dtype=np.int64)
    for i in range(m):
        if n & (1 << i):
            res = Mat[i] @ res
            res %= MOD
    print(res[0])


if __name__ == '__main__':
    solve()
