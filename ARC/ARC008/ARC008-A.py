# https://atcoder.jp/contests/arc008/submissions/14462857
# A - たこ焼き買えるかな？
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 0
    if n >= 10:
        res += (n // 10) * 100
        n %= 10
    res += min(n * 15, ((n + 10 - 1) // 10) * 100)
    print(res)


if __name__ == '__main__':
    resolve()
