# https://atcoder.jp/contests/abc024/submissions/14105146
# A - 動物園
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, k = map(int, input().split())
    s, t = map(int, input().split())

    res = s * a + t * b
    if s + t >= k:
        res -= (s + t) * c
    print(res)


if __name__ == '__main__':
    resolve()
