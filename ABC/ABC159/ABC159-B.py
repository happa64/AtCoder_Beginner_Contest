# https://atcoder.jp/contests/abc159/submissions/14423416
# B - String Palindrome
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)

    if S == S[::-1]:
        ss = S[: n // 2]
        if ss == ss[::-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
