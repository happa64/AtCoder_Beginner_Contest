# https://atcoder.jp/contests/abc174/submissions/15632847
# D - Alter Altar
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(input())

    W = deque()
    R = deque()
    for i in range(n):
        if C[i] == "W":
            W.append(i)
        if C[i] == "R":
            R.appendleft(i)

    res = 0
    i = 0
    cnt = 0
    while R:
        if C[i] == "W":
            cnt += 1
        if cnt:
            r = R.popleft()
            w = W.popleft()
            C[r], C[w] = C[w], C[r]
            cnt -= 1
            res += 1
        else:
            R.pop()
        i += 1
    print(res)


if __name__ == '__main__':
    resolve()
