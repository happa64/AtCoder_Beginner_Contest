# https://atcoder.jp/contests/abc066/submissions/13620559
# C - pushpush
import sys
# import numpy as np
from collections import Counter, deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = deque(list(map(int, input().split())))
    B = deque([])

    if n % 2 == 0:
        for i in range(n):
            a = deque.popleft(A)
            if i % 2 == 0:
                B.append(a)
            else:
                B.appendleft(a)
    else:
        for i in range(n):
            a = deque.popleft(A)
            if i % 2 != 0:
                B.append(a)
            else:
                B.appendleft(a)
    print(" ".join(map(str, B)))


if __name__ == '__main__':
    resolve()
