# https://atcoder.jp/contests/abc128/submissions/12860088
# B - Guidebook
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    SP = []
    for i in range(n):
        s, p = map(str, input().split())
        SP.append([i + 1, s, int(p)])
    SP = sorted(SP, key=lambda x: x[2], reverse=True)
    SP = sorted(SP, key=lambda x: x[1])

    for idx, _, _ in SP:
        print(idx)


if __name__ == '__main__':
    resolve()
