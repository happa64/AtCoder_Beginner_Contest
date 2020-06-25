# https://atcoder.jp/contests/abc107/submissions/13231500
# B - Grid Compression
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    # Aにおいて1行目～H行目まで、全部.の行を削除した配列res1を作る
    res = []
    for h in range(H):
        for w in range(W):
            if A[h][w] == "#":
                res.append(A[h])
                break

    # res1において1列目～W行目まで、全部.の列を削除した配列res2を作る
    res2 = [[] for _ in range(len(res))]
    for w in range(W):
        for h in range(len(res)):
            if res[h][w] == "#":
                for k in range(len(res)):
                    res2[k].append(res[k][w])
                break

    for i in res2:
        print("".join(i))


if __name__ == '__main__':
    resolve()
