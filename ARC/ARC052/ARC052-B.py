# https://atcoder.jp/contests/arc052/submissions/15104487
# B - 円錐
import sys
import math
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())
    shape = [list(map(int, input().split())) for _ in range(n)]
    query = [list(map(int, input().split())) for _ in range(q)]
    MAX = 2 * 10 ** 4 + 10

    V = [0] * MAX
    for x, r, h in shape:
        for i in range(h):
            r1 = r * (h - i) / h
            r2 = r1 * (h - i - 1) / (h - i)
            v = (pow(r1, 2) + r1 * r2 + pow(r2, 2)) * math.pi / 3
            if x + i < MAX:
                V[x + i] += v

    V_acc = [0] + list(accumulate(V))
    for a, b in query:
        res = V_acc[b] - V_acc[a]
        print(res)


if __name__ == '__main__':
    resolve()
