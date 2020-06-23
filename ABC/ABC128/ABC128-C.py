# https://atcoder.jp/contests/abc128/submissions/14642676
# C - Switches
import sys
from itertools import product
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(m)]
    P = list(map(int, input().split()))

    res = 0
    for pattern in product([0, 1], repeat=n):
        total = 0
        for i in range(m):
            cnt = 0
            for idx, p in enumerate(pattern):
                if p == 1 and idx + 1 in S[i][1:]:
                    cnt += 1
            if cnt % 2 == P[i]:
                total += 1
        if total == m:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
