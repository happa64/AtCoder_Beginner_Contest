# https://atcoder.jp/contests/past202012-open/submissions/19042611
# F - 一触即発
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    ABC = [set(map(lambda x:int(x) - 1, input().split())) for _ in range(m)]

    P = []
    for pattern in product([0, 1], repeat=n):
        if sum(pattern) == 0:
            continue
        for a, b, c in ABC:
            if pattern[a] and pattern[b] and pattern[c]:
                break
        else:
            P.append({i for i, p in enumerate(pattern) if p})

    res = 0
    for p in P:
        tmp = set()
        for abc in ABC:
            t = set()
            for num in abc:
                if num not in p:
                    t.add(num)
            if len(t) == 1:
                tmp |= t
        res = max(res, len(tmp))
    print(res)


if __name__ == '__main__':
    resolve()
