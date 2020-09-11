# https://atcoder.jp/contests/ddcc2019-qual/submissions/16627653
# B - チップ・ストーリー　～漆黒編～
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = sum([i for i in range(1, n // 2)]) * 4
    print(res if n % 2 == 0 else res + 1)


if __name__ == '__main__':
    resolve()
