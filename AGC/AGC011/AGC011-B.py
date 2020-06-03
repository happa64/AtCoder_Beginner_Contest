# https://atcoder.jp/contests/agc011/tasks/agc011_b
# B - Colorful Creatures
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    # ソート済みAの累積和をとる
    ruiseki = [0] * n
    ruiseki[0] = A[0]
    for i in range(1, n):
        ruiseki[i] = ruiseki[i - 1] + A[i]

    idx = 0
    for i in range(n - 1):
        if ruiseki[i] * 2 < A[i + 1]:
            idx = i + 1

    print(n - idx)


if __name__ == '__main__':
    resolve()
