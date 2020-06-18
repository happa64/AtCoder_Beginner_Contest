# https://atcoder.jp/contests/arc007/submissions/14447705
# C - 節約生活
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    C = input()
    n = len(C)

    res = f_inf
    for pattern in product([0, 1], repeat=n):
        T = [0] * n
        for i in range(n):
            if pattern[i] == 1:
                for j in range(n):
                    if C[j] == "o":
                        T[(i + j) % n] = 1
        if all(T):
            res = min(res, sum(pattern))
    print(res)


if __name__ == '__main__':
    resolve()
