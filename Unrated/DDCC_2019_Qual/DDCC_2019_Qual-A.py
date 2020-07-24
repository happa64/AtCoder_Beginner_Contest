# https://atcoder.jp/contests/ddcc2019-qual/submissions/15394848
# A - チップ・ストーリー　～無色編～
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print(pow(4, n))


if __name__ == '__main__':
    resolve()
