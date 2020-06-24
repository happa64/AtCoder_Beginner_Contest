# https://atcoder.jp/contests/chokudai_S001/submissions/14660532
# E - 1は何番目？
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    print(A.index(1) + 1)


if __name__ == '__main__':
    resolve()
