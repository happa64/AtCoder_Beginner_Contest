# https://atcoder.jp/contests/past201912-open/tasks/past201912_b
# B - 増減管理
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    a = list(int(input()) for _ in range(n))

    for i in range(1, n):
        if a[i] == a[i - 1]:
            print("stay")
        elif a[i] < a[i - 1]:
            print("down", a[i - 1] - a[i])
        else:
            print("up", a[i] - a[i - 1])


if __name__ == '__main__':
    resolve()
