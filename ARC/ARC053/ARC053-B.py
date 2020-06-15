# https://atcoder.jp/contests/arc053/submissions/13168022
# B - 回文分割
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    D = Counter(s)

    odd = 0
    for v in D.values():
        odd += 1 if v % 2 != 0 else 0

    print(n if odd == 0 else 2 * ((n - odd) // (2 * odd)) + 1)


if __name__ == '__main__':
    resolve()
