# https://atcoder.jp/contests/ddcc2016-qual/submissions/15394735
# A - SDカード
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    print(b * c / a)


if __name__ == '__main__':
    resolve()
