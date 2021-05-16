# https://atcoder.jp/contests/abc201/submissions/22607988
# C - Secret Number
import sys
from itertools import product
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    S = input()

    check = [True] * 10
    for i, s in enumerate(S):
        if s == "o":
            check[i] = False

    res = 0
    for pattern in product(range(10), repeat=4):
        ok = deepcopy(check)
        for p in pattern:
            if S[p] == "x":
                ok[p] = False
            if S[p] == "o":
                ok[p] = True
        if all(ok):
            res += 1
    print(res)


if __name__ == '__main__':
    solve()
