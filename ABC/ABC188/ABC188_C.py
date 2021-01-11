# https://atcoder.jp/contests/abc188/submissions/19327052
# C - ABC Tournament
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    que = [[i + 1, A[i]] for i in range(1 << n)]
    while len(que) > 2:
        m = len(que)
        nxt_que = []
        for i in range(0, m - 1, 2):
            idx1, rate1 = que[i]
            idx2, rate2 = que[i + 1]
            if rate1 > rate2:
                nxt_que.append([idx1, rate1])
            else:
                nxt_que.append([idx2, rate2])
        que = nxt_que

    idx1, rate1 = que[0]
    idx2, rate2 = que[1]
    if rate1 > rate2:
        print(idx2)
    else:
        print(idx1)


if __name__ == '__main__':
    resolve()
