# https://atcoder.jp/contests/pakencamp-2019-day3/submissions/17396759
# B - 多数決
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(input().rstrip() for _ in range(n))
    b = S.count("black")
    w = S.count("white")

    print("black" if b > w else "white")


if __name__ == '__main__':
    resolve()
