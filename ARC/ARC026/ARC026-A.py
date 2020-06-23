# https://atcoder.jp/contests/arc026/submissions/14638199
# A - ダイナミックなポーズ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())

    res = min(n, 5) * b + max(0, (n - 5)) * a
    print(res)


if __name__ == '__main__':
    resolve()
