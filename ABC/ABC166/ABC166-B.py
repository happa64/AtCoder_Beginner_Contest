# https://atcoder.jp/contests/abc166/tasks/abc166_b
# B - Trick or Treat
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    sunuke = [0] * n
    for _ in range(k):
        d = int(input())
        A = list(map(int, input().split()))
        for i in range(d):
            sunuke[A[i] - 1] += 1

    res = 0
    for i in sunuke:
        if i == 0:
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()
