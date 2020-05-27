# https://atcoder.jp/contests/soundhound2018-summer-qual/submissions/13630583
# B - Acrostic
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    w = int(input())

    res = [s[i] for i in range(0, len(s), w)]
    print("".join(res))


if __name__ == '__main__':
    resolve()
