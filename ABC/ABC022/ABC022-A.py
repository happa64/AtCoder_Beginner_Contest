# https://atcoder.jp/contests/abc022/submissions/14105084
# A - Best Body
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, s, t = map(int, input().split())
    w = int(input())
    A = list(int(input()) for _ in range(n - 1))

    res = 1 if s <= w <= t else 0
    for a in A:
        w += a
        if s <= w <= t:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
