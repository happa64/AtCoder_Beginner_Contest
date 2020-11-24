# https://atcoder.jp/contests/nikkei2019-ex/submissions/18385907
# G - 回文スコア
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    D = Counter(S)

    even = 0
    one = 0
    for v in D.values():
        if v % 2 == 0:
            even += v
        else:
            if v != 1:
                even += v - 1
            one += 1

    if one:
        res = pow(even + 1, 2)
        one -= 1
    else:
        res = pow(even, 2)
    res += one
    print(res)


if __name__ == '__main__':
    resolve()
