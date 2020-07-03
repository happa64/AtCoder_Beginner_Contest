# https://atcoder.jp/contests/cf16-final/submissions/12535288
# B - Exactly N points
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    cnt = 0
    for i in range(1, n + 1):
        cnt += i
        if cnt >= n:
            res = i
            break

    remove = cnt - n
    for i in range(1, res + 1):
        if i != remove:
            print(i)


if __name__ == '__main__':
    resolve()
