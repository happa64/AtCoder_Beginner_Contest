# https://atcoder.jp/contests/abc158/tasks/abc158_d
# D - String Formation
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    q = int(input())
    query = [list(input().split()) for _ in range(q)]

    S = deque([s])
    flg = 1
    for i in range(q):
        if query[i][0] == "1":
            flg ^= 1
        else:
            _, f, c = query[i]
            if f == "1":
                S.appendleft(c) if flg else S.append(c)
            else:
                S.append(c) if flg else S.appendleft(c)

    print("".join(S) if flg else "".join(S)[::-1])


if __name__ == '__main__':
    resolve()
