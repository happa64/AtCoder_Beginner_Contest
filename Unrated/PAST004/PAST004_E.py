# https://atcoder.jp/contests/past202010-open/submissions/18010703
# E - アナグラム
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(input())

    for T in product(S, repeat=n):
        T = list(T)
        if S != T[::-1] and S != T and sorted(S) == sorted(T):
            print("".join(T))
            break
    else:
        print("None")


if __name__ == '__main__':
    resolve()
