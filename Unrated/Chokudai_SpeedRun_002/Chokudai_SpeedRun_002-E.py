# https://atcoder.jp/contests/chokudai_S002/submissions/15473054
# E - カツサンドくん α
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
        res += min(a // 2, b)
    print(res)


if __name__ == '__main__':
    resolve()
