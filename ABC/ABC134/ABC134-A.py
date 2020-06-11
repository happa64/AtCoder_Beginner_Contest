# https://atcoder.jp/contests/abc134/submissions/14167929
# A - Dodecagon
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    r = int(input())
    res = 3 * pow(r, 2)
    print(res)


if __name__ == '__main__':
    resolve()
