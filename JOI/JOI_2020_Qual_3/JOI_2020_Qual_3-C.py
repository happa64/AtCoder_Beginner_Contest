# https://atcoder.jp/contests/joi2020yo1c/submissions/15341128
# C - 最長昇順連続部分列 (Longest Ascending Contiguous Subsequence)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 1
    cnt = 1
    for i in range(1, n):
        if A[i - 1] <= A[i]:
            cnt += 1
        else:
            cnt = 1
        res = max(res, cnt)
    print(res)


if __name__ == '__main__':
    resolve()
