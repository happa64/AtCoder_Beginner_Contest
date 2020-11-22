# https://atcoder.jp/contests/iroha2019-day1/submissions/17570727
# D - 肉と肉のぶつかり合い
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    for i in range(n):
        if i % 2 == 0:
            x += A[i]
        else:
            y += A[i]
    print("Takahashi" if x > y else "Aoki" if x < y else "Draw")


if __name__ == '__main__':
    resolve()
