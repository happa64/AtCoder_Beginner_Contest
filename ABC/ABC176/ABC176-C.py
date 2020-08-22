# https://atcoder.jp/contests/abc176/submissions/16112418
# C - Step
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for i in range(1, n):
        if A[i - 1] > A[i]:
            res += A[i - 1] - A[i]
            A[i] = A[i - 1]
    print(res)


if __name__ == '__main__':
    resolve()
