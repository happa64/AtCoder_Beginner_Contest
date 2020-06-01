# https://atcoder.jp/contests/abc033/submissions/13939341
# B - 町の合併
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    total = 0
    city = []
    for _ in range(n):
        s, p = input().split()
        total += int(p)
        city.append([s, int(p)])

    for s, p in city:
        if total / 2 < p:
            print(s)
            break
    else:
        print("atcoder")


if __name__ == '__main__':
    resolve()
