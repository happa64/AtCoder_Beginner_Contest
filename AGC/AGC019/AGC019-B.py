import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = input()
    n = len(A)

    res = (n - 1) * n // 2 + 1
    D = Counter(A)
    for v in D.values():
        if v >= 2:
            res -= (v - 1) * v // 2
    print(res)


if __name__ == '__main__':
    resolve()
