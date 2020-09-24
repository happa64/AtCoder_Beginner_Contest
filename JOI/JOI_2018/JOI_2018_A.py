# https://atcoder.jp/contests/joi2018ho/submissions/16991089
# A - ストーブ (Stove)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    T = list(int(input()) for _ in range(n))
    k -= 1

    res = T[-1] - T[0] + 1
    L = []
    for i in range(n - 1):
        time_ = T[i + 1] - T[i] - 1
        if time_ != 0:
            L.append(time_)
    L.sort()

    while L and k:
        res -= L.pop()
        k -= 1
    print(res)


if __name__ == '__main__':
    resolve()
