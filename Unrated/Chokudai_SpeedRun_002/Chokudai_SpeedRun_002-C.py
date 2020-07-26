# https://atcoder.jp/contests/chokudai_S002/submissions/15472764
# C - 和の最大値 α
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    for _ in range(n):
        a, b = map(int, input().split())
        res = max(res, a + b)
    print(res)


if __name__ == '__main__':
    resolve()
