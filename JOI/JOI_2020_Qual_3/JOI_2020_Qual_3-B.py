# https://atcoder.jp/contests/joi2020yo1c/submissions/15341086
# B - キャピタリゼーション (Capitalization)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input().replace("joi", "JOI")
    print(s)


if __name__ == '__main__':
    resolve()
