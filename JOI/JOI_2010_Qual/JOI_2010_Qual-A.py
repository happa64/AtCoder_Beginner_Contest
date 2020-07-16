# https://atcoder.jp/contests/joi2010yo/submissions/15275815
# A - レシート
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    total = int(input())
    for _ in range(9):
        total -= int(input())
    print(total)


if __name__ == '__main__':
    resolve()
