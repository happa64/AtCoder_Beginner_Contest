# https://atcoder.jp/contests/abc062/submissions/17417136
# D - 3N Numbers
import sys
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    que_left = A[:n]
    heapify(que_left)
    left = [sum(que_left)]
    for i in range(n, 2 * n):
        now = left[-1] + A[i]
        heappush(que_left, A[i])
        now -= heappop(que_left)
        left.append(now)

    B = [-a for a in A]
    que_right = B[2 * n:]
    heapify(que_right)
    right = [sum(que_right) * -1]
    for i in range(2 * n - 1, n - 1, -1):
        now = right[-1] - B[i]
        heappush(que_right, B[i])
        now += heappop(que_right)
        right.append(now)
    right = right[::-1]

    res = -f_inf
    for i in range(n + 1):
        score = left[i] - right[i]
        res = max(res, score)
    print(res)


if __name__ == '__main__':
    resolve()
