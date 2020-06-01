# https://atcoder.jp/contests/abc067/submissions/13926396
# C - Splitting Pile
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))[::-1]

    snuke = sum(A)
    arai = 0

    res = f_inf
    for i in range(n - 1):
        snuke -= A[i]
        arai += A[i]
        res = min(res, abs(snuke - arai))

    print(res)


if __name__ == '__main__':
    resolve()
