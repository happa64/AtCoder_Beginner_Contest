# https://atcoder.jp/contests/past202004-open/tasks/past202004_b
# B - 多数決
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    D = Counter(s)

    ma = 0
    res = ""
    for k, v in D.items():
        if ma < v:
            res = k
            ma = v
    print(res)


if __name__ == '__main__':
    resolve()
