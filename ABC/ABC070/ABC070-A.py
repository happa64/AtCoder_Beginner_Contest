# https://atcoder.jp/contests/abc070/submissions/13229438
# A - Palindromic Number
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = input()
    print("Yes") if n == n[::-1] else print("No")


if __name__ == '__main__':
    resolve()
