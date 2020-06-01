# https://atcoder.jp/contests/abc012/submissions/13909507
# C - 九九足し算
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    diff = 2025 - n

    for i in range(1, 10):
        q, r = divmod(diff, i)
        if r == 0 and q <= 9:
            print(str(i) + " x " + str(diff // i))


if __name__ == '__main__':
    resolve()
