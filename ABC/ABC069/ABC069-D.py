# https://atcoder.jp/contests/arc080/tasks/arc080_b
# D - Grid Coloring
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    n = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(n):
        for _ in range(A[i]):
            B.append(i + 1)

    # 上から順に先頭から、値が小さい順にマスを塗っていく
    res = [[0] * W for _ in range(H)]
    for b in B:
        for h in range(H):
            for w in range(W):
                if res[h][w] == 0:
                    res[h][w] = b
                    break
            else:
                continue
            break

    # 上から奇数番目のマスを反転させると蛇行状に塗ることができ、これが答えとなる
    for i in range(H):
        if i % 2 == 0:
            print(*res[i])
        else:
            print(*res[i][::-1])


if __name__ == '__main__':
    resolve()
