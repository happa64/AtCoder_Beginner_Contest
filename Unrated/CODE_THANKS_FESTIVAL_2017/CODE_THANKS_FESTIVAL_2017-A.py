# https://atcoder.jp/contests/code-thanks-festival-2017-open/submissions/15390558
# A - Time Penalty
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    T = list(int(input()) for _ in range(8))
    print(max(T))


if __name__ == '__main__':
    resolve()
