# https://atcoder.jp/contests/abc165/tasks/abc165_b
# B - 1%
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())

    cnt = 0
    v = 100
    while v < x:
        v = int(v + v * 0.01)
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    resolve()
