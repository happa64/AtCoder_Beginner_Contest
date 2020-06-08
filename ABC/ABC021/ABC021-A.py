# https://atcoder.jp/contests/abc021/submissions/14105031
# A - 足し算
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = [1 for _ in range(n)]
    print(n)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
