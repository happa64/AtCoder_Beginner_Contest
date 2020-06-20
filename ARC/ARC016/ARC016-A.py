# https://atcoder.jp/contests/arc016/submissions/14484267
# A - クイズゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        if i != m:
            print(i)
            break


if __name__ == '__main__':
    resolve()
