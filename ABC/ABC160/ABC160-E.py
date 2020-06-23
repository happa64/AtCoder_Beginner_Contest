# https://atcoder.jp/contests/abc160/submissions/14641812
# E - Red and Green Apples
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y, a, b, c = map(int, input().split())
    P = sorted(list(map(int, input().split())), reverse=True)
    Q = sorted(list(map(int, input().split())), reverse=True)
    R = sorted(list(map(int, input().split())), reverse=True)
    Apples = sorted(P[:x] + Q[:y] + R, reverse=True)
    print(sum(Apples[: x + y]))


if __name__ == '__main__':
    resolve()
