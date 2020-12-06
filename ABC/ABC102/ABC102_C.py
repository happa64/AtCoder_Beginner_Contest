# https://atcoder.jp/contests/arc100/submissions/13209890
# C - Linear Approximation
import sys
import statistics
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(n)]

    b = statistics.median(A)

    res = 0
    for a in A:
        res += abs(a - b)

    print(int(res))


if __name__ == '__main__':
    resolve()
