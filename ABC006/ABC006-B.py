# https://atcoder.jp/contests/abc006/tasks/abc006_2
# B - トリボナッチ数列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 4 + 7


def resolve():
    n = int(input())
    a = [0 for _ in range(n)]

    for i in range(n):
        if i == 0 or i == 1:
            a[i] = 0
        elif i == 2:
            a[i] = 1
        else:
            a[i] = a[i - 3] + a[i - 2] + a[i - 1]
            a[i] %= mod

    print(a[n - 1])


if __name__ == '__main__':
    resolve()
