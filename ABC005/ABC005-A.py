# https://atcoder.jp/contests/abc005/tasks/abc005_1
# A - おいしいたこ焼きの作り方
import math, itertools, heapq, collections, bisect, sys, copy

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** + 7


def resolve():
    x, y = map(int, input().split())
    print(y // x)


if __name__ == '__main__':
    resolve()
