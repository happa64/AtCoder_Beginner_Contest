# https://atcoder.jp/contests/abc053/tasks/abc053_b
# B - A to Z String
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    flg = False
    idx_A = 0
    idx_Z = -1
    for idx, i in enumerate(s):
        if i == "A" and not flg:
            idx_A = idx
            flg = True

        if i == "Z" and flg:
            idx_Z = idx

    print(max(0, idx_Z - idx_A + 1))


if __name__ == '__main__':
    resolve()
