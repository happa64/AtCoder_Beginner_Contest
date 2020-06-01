# https://atcoder.jp/contests/past202004-open/submissions/13920834
# L - 辞書順最小
import sys
import heapq
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k, d = map(int, input().split())
    A = list(map(int, input().split()))

    que = []
    heapq.heapify(que)
    left = 0
    right = n - (k - 1) * d
    for i in range(left, right):
        heapq.heappush(que, (A[i], i))

    if len(que) == 0:
        print(-1)
        exit()

    res = []
    for _ in range(k):
        while 1:
            a, idx = heapq.heappop(que)
            if left <= idx:
                res.append(a)
                if right >= n:
                    break
                for j in range(right, right + d):
                    heapq.heappush(que, (A[j], j))
                left = idx + d
                right += d
                break

    print(*res)


if __name__ == '__main__':
    resolve()
