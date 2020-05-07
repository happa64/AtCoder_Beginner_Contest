# https://atcoder.jp/contests/abc048/submissions/12915549
# C - Boxes and Candies
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    res = 0
    if A[0] > x:
        res += A[0] - x
        A[0] = x

    for i in range(1, n):
        if A[i - 1] + A[i] > x:
            res += A[i] + A[i - 1] - x
            A[i] -= A[i] + A[i - 1] - x

    print(res)


if __name__ == '__main__':
    resolve()
