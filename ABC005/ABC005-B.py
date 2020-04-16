# https://atcoder.jp/contests/abc005/tasks/abc005_2
# B - おいしいたこ焼きの食べ方
import math, itertools, heapq, collections, bisect, sys, copy

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** + 7


def resolve():
    n = int(input())
    T = list(int(input()) for _ in range(n))
    T.sort()
    print(T[0])


if __name__ == '__main__':
    resolve()
