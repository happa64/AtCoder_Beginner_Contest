# https://atcoder.jp/contests/arc030/submissions/14638677
# A - 閉路グラフ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    k = int(input())

    print("YES" if k <= n // 2 else "NO")


if __name__ == '__main__':
    resolve()
