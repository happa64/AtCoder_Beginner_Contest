# https://atcoder.jp/contests/abc031/submissions/14150216
# A - ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, d = map(int, input().split())
    res = max((a + 1) * d, a * (d + 1))
    print(res)


if __name__ == '__main__':
    resolve()
