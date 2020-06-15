# https://atcoder.jp/contests/tenka1-2014-qualb/submissions/14384727
# A - HAGIXILE
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    res = S.replace("HAGIYA", "HAGIXILE")
    print(res)


if __name__ == '__main__':
    resolve()
