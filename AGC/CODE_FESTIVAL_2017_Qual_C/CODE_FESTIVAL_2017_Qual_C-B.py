# https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b
# B - Similar Arrays
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    # Aに似ている整数はA-1, A, A-2の何れかである
    similar = []
    for i in range(n):
        similar.append(list(range(A[i] - 1, A[i] + 2)))

    # Bのパターンを全て試す
    res = 0
    for pattern in product([0, 1, 2], repeat=n):
        value = 1
        for idx, i in enumerate(pattern):
            value *= similar[idx][i]

        if value % 2 == 0:
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()
