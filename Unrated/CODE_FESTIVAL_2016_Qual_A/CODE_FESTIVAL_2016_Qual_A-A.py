# https://atcoder.jp/contests/code-festival-2016-quala/submissions/13608454
# A - CODEFESTIVAL 2016
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input())
    res = s[:4] + [" "] + s[4:]
    print("".join(res))


if __name__ == '__main__':
    resolve()
