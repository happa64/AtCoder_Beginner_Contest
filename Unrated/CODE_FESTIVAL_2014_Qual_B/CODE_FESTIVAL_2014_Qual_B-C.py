# https://atcoder.jp/contests/code-festival-2014-qualb/submissions/14895057
# C - 錬金術士
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S1 = input()
    S2 = input()
    S3 = input()

    C1 = Counter(S1)
    C2 = Counter(S2)
    C3 = Counter(S3)

    L = R = 0
    for i in range(26):
        x = chr(ord('A') + i)
        L += max(0, C3[x] - C2[x])
        R += min(C1[x], C3[x])

    print("YES" if L <= len(S3) // 2 <= R else "NO")


if __name__ == '__main__':
    resolve()
