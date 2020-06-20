# https://atcoder.jp/contests/arc013/submissions/14484183
# A - 梱包できるかな？
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    res = 0
    for p1 in permutations(A):
        for p2 in permutations(B):
            t = 1
            for a, b in zip(p1, p2):
                t *= (a // b)
            res = max(res, t)
    print(res)


if __name__ == '__main__':
    resolve()
