# https://atcoder.jp/contests/abc097/submissions/12248078
# B - Exponential
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    m = 0
    for i in range(1, 1000):
        for j in range(2, 100):
            k = pow(i, j)
            if k <= x:
                m = max(m, k)
    print(m)


if __name__ == '__main__':
    resolve()
