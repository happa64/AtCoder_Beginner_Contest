# https://atcoder.jp/contests/abc168/submissions/13290960
# A - ∴ (Therefore)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = input()
    if n[-1] == "2" or n[-1] == "4" or n[-1] == "5" or n[-1] == "7" or n[-1] == "9":
        print("hon")
    elif n[-1] == "0" or n[-1] == "1" or n[-1] == "6" or n[-1] == "8":
        print("pon")
    else:
        print("bon")


if __name__ == '__main__':
    resolve()
