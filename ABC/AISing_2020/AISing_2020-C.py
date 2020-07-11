# https://atcoder.jp/contests/aising2020/submissions/15179079
# C - XYZ Triplets
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = [0] * (n + 10)
    for x in range(1, int(pow(n, 0.5)) + 1):
        for y in range(1, int(pow(n, 0.5)) + 1):
            for z in range(1, int(pow(n, 0.5)) + 1):
                t = pow(x, 2) + pow(y, 2) + pow(z, 2) + x * y + y * z + z * x
                if t <= n:
                    res[t] += 1

    for x in range(1, n + 1):
        print(res[x])


if __name__ == '__main__':
    resolve()
