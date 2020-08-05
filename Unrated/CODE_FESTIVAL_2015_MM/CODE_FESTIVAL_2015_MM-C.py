# https://atcoder.jp/contests/code-festival-2015-morning-middle/submissions/15697046
# C - 一次元オセロ
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = deque(list(map(int, input().split())))

    res = 0
    while len(A) != 1:
        left = A[0] + A[1] + 1
        right = A[-1] + A[-2] + 1
        if left < right:
            w = A.popleft()
            res += w
            A[0] += w + 1
            b = A.popleft()
            res += b
            A[0] += b + 1
        else:
            w = A.pop()
            res += w
            A[-1] += w + 1
            b = A.pop()
            res += b
            A[-1] += b + 1
    print(res)


if __name__ == '__main__':
    resolve()
