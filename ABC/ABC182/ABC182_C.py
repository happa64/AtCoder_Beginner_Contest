# https://atcoder.jp/contests/abc182/submissions/17957241
# C - To 3
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = input()

    tot = 0
    for i in n:
        tot += int(i)

    res = f_inf
    for pattern in product([0, 1], repeat=len(n)):
        cnt = sum(pattern)
        tmp = tot
        for idx, p in enumerate(pattern):
            if p == 1:
                tmp -= int(n[idx])
        if tmp % 3 == 0:
            res = min(res, cnt)
    print(res if res != len(n) else -1)


if __name__ == '__main__':
    resolve()
