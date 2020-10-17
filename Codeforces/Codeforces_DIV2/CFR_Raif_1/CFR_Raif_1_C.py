# https://codeforces.com/contest/1428/submission/95767809
# C. ABBB
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        S = input().rstrip()
        que = deque()
        for s in S:
            if que and ((que[-1] == "A" and s == "B") or (que[-1] == "B" and s == "B")):
                que.pop()
            else:
                que.append(s)
        print(len(que))


if __name__ == '__main__':
    resolve()
