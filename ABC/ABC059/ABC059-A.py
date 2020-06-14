# https://atcoder.jp/contests/abc059/submissions/14267031
# A - Three-letter acronym
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s1, s2, s3 = input().split()
    res = s1[0] + s2[0] + s3[0]
    print(res.upper())


if __name__ == '__main__':
    resolve()
