# https://atcoder.jp/contests/joi2008yo/submissions/15088732
# B - JOIとIOI
import sys

sys.setrecursionlimit(10 ** 7)

f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    res1, res2 = 0, 0
    for i in range(n - 2):
        if s[i:i + 3] == "JOI":
            res1 += 1
        elif s[i:i + 3] == "IOI":
            res2 += 1
    print(res1, res2, sep="\n")


if __name__ == '__main__':
    resolve()
