# https://atcoder.jp/contests/abc173/tasks/abc173_a
# A - Payment
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    for i in range(0, 10001, 1000):
        if i >= n:
            print(i - n)
            break


if __name__ == '__main__':
    resolve()
