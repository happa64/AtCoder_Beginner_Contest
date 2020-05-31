# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_a
# A - CF
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    flg = False
    for i in s:
        if i == "C":
            flg = True

        if flg and i == "F":
            print("Yes")
            break
    else:
        print("No")


if __name__ == '__main__':
    resolve()
