# https://atcoder.jp/contests/colopl2018-qual/submissions/22668659
# C - すぬけそだて――ごはん――
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())

    odd = tuple(num for num in range(a, b + 1) if num % 2)
    even = tuple(num for num in range(a, b + 1) if num % 2 == 0)
    n = len(odd)

    res = 0
    for bit in range(1 << n):
        T = tuple(odd[mask] for mask in range(n) if bit & (1 << mask))
        ok = True
        for i, t1 in enumerate(T):
            for t2 in T[i + 1:]:
                if gcd(t1, t2) != 1:
                    ok = False
                    break
            else:
                continue
            break
        if not ok:
            continue
        res += 1
        for s in even:
            for t in T:
                if gcd(s, t) != 1:
                    break
            else:
                res += 1
    print(res)


if __name__ == '__main__':
    resolve()
