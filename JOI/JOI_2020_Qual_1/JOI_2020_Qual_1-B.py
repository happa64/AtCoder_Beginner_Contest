# https://atcoder.jp/contests/joi2020yo1a/submissions/15316383
# B - 母音を数える (Counting Vowels)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()
    L = set(list("aiueo"))
    res = 0
    for i in range(n):
        if s[i] in L:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
