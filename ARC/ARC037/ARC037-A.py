# https://atcoder.jp/contests/arc037/submissions/14646775
# A - 全優
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    M = list(map(int, input().split()))

    res = 0
    for m in M:
        res += max(0, 80 - m)
    print(res)


if __name__ == '__main__':
    resolve()
