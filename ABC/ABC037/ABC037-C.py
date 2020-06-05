# https://atcoder.jp/contests/abc037/submissions/13101828
# C - 総和
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和
    R = [0]
    for i in range(n):
        R.append(R[-1] + A[i])

    res = 0
    for i in range(n - k + 1):
        res += R[i + k] - R[i]

    print(res)


if __name__ == '__main__':
    resolve()
