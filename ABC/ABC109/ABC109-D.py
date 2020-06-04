# https://atcoder.jp/contests/abc109/submissions/12947852
# D - Make Them Even
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 一筆書きになるようにグリッドを見ていき、Aが奇数であれば、次のマスに渡す
    res = []
    for h in range(H):
        for w in range(W) if h % 2 == 0 else reversed(range(W)):
            if h % 2 == 0:
                if w < W - 1:
                    if A[h][w] % 2 != 0:
                        A[h][w] -= 1
                        A[h][w + 1] += 1
                        res.append([h + 1, w + 1, h + 1, w + 2])
                else:
                    if A[h][w] % 2 != 0:
                        if h + 1 < H:
                            A[h][w] -= 1
                            A[h + 1][w] += 1
                            res.append([h + 1, w + 1, h + 2, w + 1])
            else:
                if w > 0:
                    if A[h][w] % 2 != 0:
                        A[h][w] -= 1
                        A[h][w - 1] += 1
                        res.append([h + 1, w + 1, h + 1, w])
                else:
                    if A[h][w] % 2 != 0:
                        if h + 1 < H:
                            A[h][w] -= 1
                            A[h + 1][w] += 1
                            res.append([h + 1, w + 1, h + 2, w + 1])

    print(len(res))
    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
