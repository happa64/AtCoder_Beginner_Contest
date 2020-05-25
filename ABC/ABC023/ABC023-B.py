# https://atcoder.jp/contests/abc023/submissions/13586062
# B - 手芸王
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    que = deque(["b"])
    i = 0
    while len(que) < n:
        i += 1
        if i % 3 == 1:
            que.appendleft("a")
            que.append("c")
        elif i % 3 == 2:
            que.appendleft("c")
            que.append("a")
        else:
            que.appendleft("b")
            que.append("b")

    ac = "".join(que)
    print(i) if ac == s else print(-1)


if __name__ == '__main__':
    resolve()
