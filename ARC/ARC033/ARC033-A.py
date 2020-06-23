# https://atcoder.jp/contests/arc033/submissions/14638882
# A - 隠れた言葉
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = (n + 1) * n // 2
    print(res)


if __name__ == '__main__':
    resolve()
