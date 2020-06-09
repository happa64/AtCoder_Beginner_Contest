# https://atcoder.jp/contests/abc030/submissions/13172350
# C - 飛行機乗り
import sys
import heapq

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    heapq.heapify(A)
    heapq.heapify(B)

    res = 0
    now = "a"
    while A and B:
        if now == "a":
            if A[0] + x <= B[0]:
                res += 1
                now = "b"
                heapq.heappop(A)
            else:
                heapq.heappop(B)
        else:
            if B[0] + y <= A[0]:
                res += 1
                now = "a"
                heapq.heappop(B)
            else:
                heapq.heappop(A)

    print((res + 1) // 2)


if __name__ == '__main__':
    resolve()
