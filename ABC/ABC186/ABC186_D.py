# https://atcoder.jp/contests/abc186/submissions/18889997
# D - Sum of difference
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    R = [0] + list(accumulate(A))
    res = 0
    for i in range(1, n + 1):
        r = A[i - 1] * (n - i)
        diff = R[-1] - R[i]
        res += abs(r - diff)
    print(res)


if __name__ == '__main__':
    resolve()
