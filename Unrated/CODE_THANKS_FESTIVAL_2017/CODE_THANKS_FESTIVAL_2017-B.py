# https://atcoder.jp/contests/code-thanks-festival-2017-open/submissions/15396455
# B - Concatenated Palindrome
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    res = 0
    for i in reversed(range(len(s))):
        ss = s[i:]
        if ss == ss[::-1]:
            res = max(res, len(ss))
    print(len(s) - res)


if __name__ == '__main__':
    resolve()
