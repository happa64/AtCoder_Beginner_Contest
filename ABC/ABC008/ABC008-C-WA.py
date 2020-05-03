# https://atcoder.jp/contests/abc008/tasks/abc008_3
# C - コイン（99点解法）

import sys
from itertools import permutations
from math import factorial

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(int(input()) for _ in range(n))

    res = 0
    # 数値の並び順を全て試す
    for P in permutations(C):
        # 左側にある約数が偶数個であれば表になる
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if i != j:
                    if P[i] % P[j] == 0:
                        cnt += 1
            if cnt % 2 == 0:
                res += 1

    print(res / factorial(n))


if __name__ == '__main__':
    resolve()
