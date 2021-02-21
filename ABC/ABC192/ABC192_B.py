# https://atcoder.jp/contests/abc192/submissions/20292563
# B - uNrEaDaBlE sTrInG
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    flg1 = all([s[i].islower() for i in range(0, n, 2)])
    flg2 = all([s[i].isupper() for i in range(1, n, 2)])
    print("Yes" if flg1 and flg2 else "No")


if __name__ == '__main__':
    resolve()
