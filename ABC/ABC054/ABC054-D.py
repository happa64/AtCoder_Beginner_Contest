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


if __name__ == '__main__':
    resolve()
