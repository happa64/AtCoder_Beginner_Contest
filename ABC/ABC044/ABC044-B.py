# https://atcoder.jp/contests/abc044/submissions/12264905
# B - 美しい文字列
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    w = input()

    D = Counter(w)
    for v in D.values():
        if v % 2 != 0:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
