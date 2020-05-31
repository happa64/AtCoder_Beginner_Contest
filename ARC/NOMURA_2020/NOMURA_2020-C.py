# https://atcoder.jp/contests/nomura2020/submissions/13756351
# C - Folia
import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    # 深い順から見ていき、各深さに期待する頂点の最大値と最小値を計算する
    # 深さdの最小値は、ceil(d+1に存在する頂点数/2)+(dの葉の数)
    # 深さdの最小値は、(d+1に存在する頂点数)+(dの葉の数)
    mi, ma = [A[-1]], [A[-1]]
    for i in reversed(range(n)):
        mi.append(math.ceil(mi[-1] / 2) + A[i])
        ma.append(ma[-1] + A[i])

    mi = mi[::-1]
    ma = ma[::-1]

    # 浅い順に見ていく
    res = []
    for i in range(n + 1):
        # 根の頂点数は1である必要がある
        if i == 0:
            if mi[i] <= 1 <= ma[i]:
                res.append(1)
                continue
            else:
                break

        if mi[i] <= (res[-1] - A[i - 1]) * 2 <= ma[i]:
            res.append((res[-1] - A[i - 1]) * 2)
        else:
            res.append(ma[i])

    print(sum(res) if len(res) != 0 else -1)


if __name__ == '__main__':
    resolve()
