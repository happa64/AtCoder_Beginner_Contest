# https://atcoder.jp/contests/abc103/submissions/13178238
# B - String Rotation
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input())
    t = list(input())
    que = deque(t)
    n = len(s)

    for i in range(n):
        if s == list(que):
            print("Yes")
            break
        a = que.popleft()
        que.append(a)
    else:
        print("No")


if __name__ == '__main__':
    resolve()
