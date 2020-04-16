# https://atcoder.jp/contests/abc005/tasks/abc005_3
# C - おいしいたこ焼きの売り方
import math, itertools, heapq, collections, bisect, sys, copy

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** + 7


def resolve():
    t = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    res = []
    for b in B:
        for a in A:
            if b - t <= a <= b:
                res.append(b)
                idx = A.index(a)
                A.pop(idx)
                break

    if len(res) == m:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    resolve()
