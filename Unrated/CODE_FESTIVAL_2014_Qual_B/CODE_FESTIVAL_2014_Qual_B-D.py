# https://atcoder.jp/contests/code-festival-2014-qualb/submissions/16477896
# D - 登山家
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(int(input().rstrip()) for _ in range(n))
    res = [0] * n

    que = deque([0])
    for i in range(1, n):
        t = H[que[-1]]
        if H[i] <= t:
            que.append(i)
        else:
            while que and H[que[-1]] < H[i]:
                idx = que.pop()
                res[idx] += i - idx - 1
            que.append(i)
    while len(que) > 1:
        idx = que.popleft()
        res[idx] += que[-1] - idx

    que = deque([n - 1])
    for i in reversed(range(n - 1)):
        t = H[que[-1]]
        if H[i] <= t:
            que.append(i)
        else:
            while que and H[que[-1]] < H[i]:
                idx = que.pop()
                res[idx] += idx - i - 1
            que.append(i)
    while len(que) > 1:
        idx = que.popleft()
        res[idx] += idx - que[-1]

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
