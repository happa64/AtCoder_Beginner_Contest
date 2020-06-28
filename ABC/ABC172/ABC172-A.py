# https://atcoder.jp/contests/abc172/submissions/14777692
# A - Calc
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())
    print(a + a ** 2 + a ** 3)


if __name__ == '__main__':
    resolve()
