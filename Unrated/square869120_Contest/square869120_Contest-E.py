# https://atcoder.jp/contests/s8pc-1/submissions/15123998
# E - 散歩 (E869120 and Path Length)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    R = [0]
    for i in range(1, n):
        R.append(R[-1] + pow(A[i - 1], A[i], mod))

    prev = 0
    res = 0
    for j in range(q):
        res += abs(R[C[j] - 1] - R[prev])
        res %= mod
        prev = C[j] - 1
    res += abs(R[0] - R[prev])
    print(res % mod)


if __name__ == '__main__':
    resolve()
