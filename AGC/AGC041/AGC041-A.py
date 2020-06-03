# https://atcoder.jp/contests/agc041/tasks/agc041_a
# A - Table Tennis Training
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    ab = abs(a - b)
    if ab % 2 == 0:
        print(ab // 2)
    else:
        res1 = a + (ab - 1) // 2
        res2 = n - b + 1 + (ab - 1) // 2
        print(min(res1, res2))


if __name__ == '__main__':
    resolve()
