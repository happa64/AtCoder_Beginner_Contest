# https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_b
# B - Problem Set
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    D = list(map(int, input().split()))
    m = int(input())
    T = list(map(int, input().split()))

    P = Counter(D)

    for i in range(m):
        P[T[i]] -= 1

    for v in P.values():
        if v < 0:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    resolve()
