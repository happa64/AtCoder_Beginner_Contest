# https://atcoder.jp/contests/joi2021yo2/submissions/18954416
# A - 往復すごろく (Round Sugoroku)
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a = map(int, input().split())
    S = input()

    left = deque()
    right = deque()
    for i in range(n):
        if i + 1 < a and S[i] == "#":
            left.append(i + 1)
        elif i + 1 > a and S[i] == "#":
            right.append(i + 1)

    res = 0
    flg = 1
    now = a
    while left or right:
        if flg:
            nxt = right.popleft() if right else n + 1
            res += nxt - now
            now = nxt
        else:
            nxt = left.pop() if left else 0
            res += now - nxt
            now = nxt
        flg ^= 1
    print(res)


if __name__ == '__main__':
    resolve()
