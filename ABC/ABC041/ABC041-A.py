# https://atcoder.jp/contests/abc041/submissions/14167907
# A - 添字
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    i = int(input())
    print(s[i - 1])


if __name__ == '__main__':
    resolve()
