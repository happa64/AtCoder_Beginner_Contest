# https://atcoder.jp/contests/nikkei2019-2-final/submissions/15734985
# A - Count Triplets
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for j in range(1, n - 1):
        a = 0
        for i in range(j):
            if A[i] < A[j]:
                a += 1
        b = 0
        for k in range(j + 1, n):
            if A[j] > A[k]:
                b += 1
        res += a * b
    print(res)


if __name__ == '__main__':
    resolve()
