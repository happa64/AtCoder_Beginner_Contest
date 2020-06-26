# https://atcoder.jp/contests/arc068/submissions/14694445
# D - Card Eater
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    D = Counter(A)
    ev = 0
    for k, v in D.items():
        if v % 2 == 0:
            ev += 1

    print(len(D) if ev % 2 == 0 else len(D) - 1)


if __name__ == '__main__':
    resolve()
