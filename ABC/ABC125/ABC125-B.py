# https://atcoder.jp/contests/abc125/submissions/14028451
# B - Resale
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    res = 0
    for i in range(n):
        diff = V[i] - C[i]
        res += diff if diff > 0 else 0

    print(res)


if __name__ == '__main__':
    resolve()
