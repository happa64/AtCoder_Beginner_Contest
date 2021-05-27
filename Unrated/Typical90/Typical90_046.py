# https://atcoder.jp/contests/typical90/submissions/22857513
# 046 - I Love 46（★3）
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    _ = int(input())
    A = tuple(map(lambda x: int(x) % 46, input().split()))
    B = tuple(map(lambda x: int(x) % 46, input().split()))
    C = tuple(map(lambda x: int(x) % 46, input().split()))

    A = Counter(A)
    B = Counter(B)
    C = Counter(C)

    res = 0
    for a, v1 in A.items():
        for b, v2 in B.items():
            for c, v3 in C.items():
                if (a + b + c) % 46 == 0:
                    res += v1 * v2 * v3
    print(res)


if __name__ == '__main__':
    solve()
