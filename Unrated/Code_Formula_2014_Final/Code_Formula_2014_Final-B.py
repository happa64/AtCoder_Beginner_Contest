# https://atcoder.jp/contests/code-formula-2014-final/submissions/15358145
# B - 3歩進んで2歩下がる
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    if n % 2 == 0:
        print(n // 2)
    else:
        res = (n + 1) // 2 + 2
        print(res)


if __name__ == '__main__':
    resolve()
