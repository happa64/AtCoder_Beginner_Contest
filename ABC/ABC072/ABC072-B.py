# https://atcoder.jp/contests/abc072/submissions/12986611
# B - OddString
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    res = ""
    for i in range(0, len(s), 2):
        res += s[i]
    print(res)


if __name__ == '__main__':
    resolve()
