# https://atcoder.jp/contests/abc135/submissions/13479512
# C - City Savers
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        貪欲法である。先頭から倒せる分だけ倒していけば良い。

    計算量：O(N)
    """
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    res = 0
    for i in range(n):
        if A[i] <= B[i]:
            res += A[i]
            B[i] -= A[i]
            A[i] = 0
            if A[i + 1] <= B[i]:
                res += A[i + 1]
                B[i] -= A[i + 1]
                A[i + 1] = 0
            else:
                res += B[i]
                A[i + 1] -= B[i]
                B[i] = 0
        else:
            res += B[i]
            A[i] -= B[i]
            B[i] = 0

    print(res)


if __name__ == '__main__':
    resolve()
