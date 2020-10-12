# https://atcoder.jp/contests/arc105/submissions/17336691
# A - Fourtune Cookies
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = list(map(int, input().split()))

    for pattern in product([0, 1], repeat=4):
        t = 0
        s = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                t += A[idx]
            else:
                s += A[idx]
        if t == s:
            print("Yes")
            break
    else:
        print("No")


if __name__ == '__main__':
    resolve()
