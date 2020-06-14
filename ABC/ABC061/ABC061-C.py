# https://atcoder.jp/contests/abc061/submissions/12897676
# C - Big Array
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    AB = sorted(AB, key=lambda x: x[0])

    for i in range(n):
        a, b = AB[i]
        if b < k:
            k -= b
        else:
            print(a)
            break


if __name__ == '__main__':
    resolve()
