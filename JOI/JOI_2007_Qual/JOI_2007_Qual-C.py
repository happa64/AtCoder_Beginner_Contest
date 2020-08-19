# https://atcoder.jp/contests/joi2007yo/submissions/16034254
# C - シーザー暗号
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    res = ""
    for s in S:
        if ord(s) - 3 >= ord("A"):
            idx = ord(s) - 3
        else:
            diff = ord(s) - ord("A")
            diff = 3 - diff - 1
            idx = ord("Z") - diff
        res += chr(idx)
    print(res)


if __name__ == '__main__':
    resolve()
