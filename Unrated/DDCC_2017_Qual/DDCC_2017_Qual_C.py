# https://atcoder.jp/contests/ddcc2017-qual/submissions/16820321
# C - 収納
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, c = map(int, input().split())
    L = list(int(input()) for _ in range(n))
    L.sort(reverse=True)
    que = deque(L)
    res = 0
    while que:
        l = que.popleft()
        if que and l + que[-1] + 1 <= c:
            que.pop()
        res += 1

    print(res)


if __name__ == '__main__':
    resolve()
