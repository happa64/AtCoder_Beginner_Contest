# https://atcoder.jp/contests/abc173/submissions/14996082
# D - Chat in a Circle
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)

    res = 0
    que = deque([A[0]])
    for i in range(1, n):
        a = que.popleft()
        res += a
        que.append(A[i])
        que.append(A[i])
    print(res)


if __name__ == '__main__':
    resolve()
