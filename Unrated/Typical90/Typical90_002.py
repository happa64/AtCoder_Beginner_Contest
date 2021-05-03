# https://atcoder.jp/contests/typical90/submissions/21907692
# 002 - Encyclopedia of Parentheses（★3）
import sys
from itertools import product
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())

    for pattern in product("()",repeat=n):
        que = deque()
        for p in pattern:
            if p == ")":
                if que and que[-1] == "(":
                    que.pop()
                else:
                    que.append(p)
            else:
                que.append(p)
        if not que:
            print("".join(pattern))


if __name__ == '__main__':
    solve()
