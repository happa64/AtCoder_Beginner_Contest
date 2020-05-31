# https://atcoder.jp/contests/code-festival-2017-qualc/submissions/13756839
# A - Can you get AC?
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    print("Yes" if "AC" in s else "No")


if __name__ == '__main__':
    resolve()
