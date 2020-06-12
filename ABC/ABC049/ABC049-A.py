# https://atcoder.jp/contests/abc049/submissions/14186383
# A - 居合を終え、青い絵を覆う
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    c = input()
    L = list("aiueo")
    print("vowel" if c in L else "consonant")


if __name__ == '__main__':
    resolve()
