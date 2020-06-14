# https://atcoder.jp/contests/abc128/submissions/12826611
# D - equeue
import sys
from collections import deque
import heapq

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    V = list(map(int, input().split()))

    res = 0
    for i in range(1, k + 1):
        # i回取り出す
        for j in range(i + 1):
            que = deque(V)
            get = []
            heapq.heapify(get)
            # j回前から取り出す
            for x in range(j):
                if que:
                    v = que.popleft()
                    heapq.heappush(get, v)

            # i - j回前から取り出す
            for _ in range(i - j):
                if que:
                    v = que.pop()
                    heapq.heappush(get, v)

            # 何も戻さない場合のスコア
            score = sum(get)
            res = max(res, score)

            # 宝石の価値が低い順に1 ~ k - i回戻す場合のスコア
            for _ in range(k - i):
                if get:
                    heapq.heappop(get)

                score = sum(get)
                res = max(res, score)

    print(res)


if __name__ == '__main__':
    resolve()
