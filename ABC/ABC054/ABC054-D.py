# https://atcoder.jp/contests/abc054/submissions/16558436
# D - Mixing Experiment
import sys
from itertools import product
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """半分全列挙"""
    n, Ma, Mb = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(n)]
    s = (n + 1) // 2
    t = n - s

    S = defaultdict(int)
    for pattern in product([0, 1], repeat=s):
        a = b = c = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                a += ABC[idx][0]
                b += ABC[idx][1]
                c += ABC[idx][2]
        S[(a, b)] = min(S.get((a, b), f_inf), c)

    T = defaultdict(int)
    for pattern in product([0, 1], repeat=t):
        a = b = c = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                a += ABC[s + idx][0]
                b += ABC[s + idx][1]
                c += ABC[s + idx][2]
        T[(a, b)] = min(T.get((a, b), f_inf), c)

    MAX_A = sum([a for a, _, _ in ABC])
    MAX_B = sum([b for _, b, _ in ABC])

    res = f_inf
    for k, v in S.items():
        a, b = k
        x, y = Ma, Mb
        while x <= MAX_A and y <= MAX_B:
            if T.get((x - a, y - b), -1) != -1:
                if not (a == b == 0 and x - a == x - b == 0):
                    cost = v + T[(x - a, y - b)]
                    res = min(res, cost)
            x += Ma
            y += Mb
    print(res if res != f_inf else -1)


def resolve2():
    """DP"""
    n, ma, mb = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(n)]
    MAX_A = sum([a for a, _, _ in ABC]) + 1
    MAX_B = sum([b for _, b, _ in ABC]) + 1

    dp = [[[f_inf] * MAX_B for _ in range(MAX_A)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    for i in range(n):
        a, b, c = ABC[i]
        for j in range(MAX_A):
            for k in range(MAX_B):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + a < MAX_A and k + b < MAX_B:
                    dp[i + 1][j + a][k + b] = min(dp[i + 1][j + a][k + b], dp[i][j][k] + c)

    res = f_inf
    for i in range(MAX_A):
        for j in range(MAX_B):
            if i == j == 0:
                continue
            if i * mb == j * ma:
                res = min(res, dp[-1][i][j])
    print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
