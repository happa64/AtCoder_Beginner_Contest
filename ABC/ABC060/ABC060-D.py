# https://atcoder.jp/contests/arc073/submissions/15533142
# D - Simple Knapsack
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N, W = map(int, input().split())
    V = [[0] for _ in range(4)]
    for i in range(N):
        w, v = map(int, input().split())
        if i == 0:
            init = w
        V[w - init].append(v)

    for i in range(4):
        V[i].sort(reverse=True)

    res = 0
    for i in range(len(V[0]) + 1):
        a = sum(V[0][:i])
        for j in range(len(V[1]) + 1):
            b = sum(V[1][:j])
            for k in range(len(V[2]) + 1):
                c = sum(V[2][:k])
                for l in range(len(V[3]) + 1):
                    d = sum(V[3][:l])
                    total_w = init * i + (init + 1) * j + (init + 2) * k + (init + 3) * l
                    if total_w <= W:
                        res = max(res, a + b + c + d)
    print(res)


if __name__ == '__main__':
    resolve()
