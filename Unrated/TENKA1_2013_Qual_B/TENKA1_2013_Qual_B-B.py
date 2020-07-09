# https://atcoder.jp/contests/tenka1-2013-qualb/submissions/15103636
# B - 天下一後入れ先出しデータ構造
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    Q, L = map(int, input().split())
    query = [list(input().split()) for _ in range(Q)]

    que = deque([])
    size = 0
    for i in range(Q):
        if query[i][0] == "Push":
            _, n, m = query[i]
            n, m = int(n), int(m)
            que.appendleft([n, m])
            size += n
            if size > L:
                print("FULL")
                exit()
        elif query[i][0] == "Pop":
            _, n = query[i]
            n = int(n)
            size -= n
            if size < 0:
                print("EMPTY")
                exit()
            else:
                while n:
                    if que[0][0] <= n:
                        n -= que[0][0]
                        que.popleft()
                    else:
                        que[0][0] -= n
                        n = 0
        elif query[i][0] == "Top":
            if size == 0:
                print("EMPTY")
                exit()
            else:
                print(que[0][1])
        else:
            print(size)
    print("SAFE")


if __name__ == '__main__':
    resolve()
