# https://atcoder.jp/contests/joi2021yo1c/submissions/18697135
# B - IOI 文字列 (IOI String)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input().rstrip()
    res = 0
    for i in range(n):
        if i % 2 == 0 and s[i] != "I":
            res += 1
        if i % 2 and s[i] != "O":
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
