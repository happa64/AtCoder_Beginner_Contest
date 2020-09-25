# https://atcoder.jp/contests/joi2013ho/submissions/17001751
# 1 - 電飾 (illumination)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    bit = list(input().split())

    section = [0]
    cnt = 1
    for i in range(1, n):
        if bit[i - 1] == bit[i]:
            section.append(cnt)
            cnt = 1
        else:
            cnt += 1
    section.append(cnt)
    section.append(0)

    res = max([sum(section[i:i + 3]) for i in range(len(section) - 2)])
    print(res)


if __name__ == '__main__':
    resolve()
