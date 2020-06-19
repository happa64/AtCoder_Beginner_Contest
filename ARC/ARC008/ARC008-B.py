# https://atcoder.jp/contests/arc008/submissions/13113852
# B - 謎のたこ焼きおじさん
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    NAME = list(input())
    KIT = list(input())

    for i in NAME:
        if i not in set(KIT):
            print(-1)
            exit()

    KITS = KIT[::]
    for i in range(1, 51):
        NAME_D = Counter(NAME)
        KITS_D = Counter(KITS)
        for k, v in KITS_D.items():
            if NAME_D.get(k) is not None:
                NAME_D[k] -= v
        for v in NAME_D.values():
            if v > 0:
                break
        else:
            print(i)
            break
        KITS += KIT


if __name__ == '__main__':
    resolve()
