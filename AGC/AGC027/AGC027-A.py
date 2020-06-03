# https://atcoder.jp/contests/agc027/tasks/agc027_a
# A - Candy Distribution Again
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    A = sorted(list(map(int, input().split())))

    res = 0
    for i in range(n):
        if i == n - 1 and A[i] < x:
            continue

        if A[i] <= x:
            x -= A[i]
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()
