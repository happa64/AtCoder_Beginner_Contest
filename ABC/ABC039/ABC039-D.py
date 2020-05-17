# https://atcoder.jp/contests/abc039/submissions/13282022
# D - 画像処理高橋君
import sys
import copy

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = list(input() for _ in range(H))

    # 左上から右下に順に画像を見ていく
    res = [["." for _ in range(W)] for _ in range(H)]
    for h in range(H):
        for w in range(W):
            # 座標(h,w)が黒であれば、その周り8方向を見る
            if S[h][w] == "#":
                for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                    next_h, next_w = h + dh, w + dw
                    if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or S[next_h][next_w] == "#":
                        continue
                    else:
                        break
                # 周り8方向が全て黒であれば、元の画像でも座標(h,w)は黒である
                else:
                    res[h][w] = "#"

    S2 = copy.deepcopy(res)
    # 復元されたと思わる画像に、もう一度収縮処理を行う
    for h in range(H):
        for w in range(W):
            if res[h][w] == "#":
                for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                    next_h, next_w = h + dh, w + dw
                    if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                        continue
                    else:
                        S2[next_h][next_w] = "#"

    # 再収縮処理した画像と、与えられた画像が一致していればpossibleである
    for i in range(H):
        if "".join(S[i]) != "".join(S2[i]):
            print("impossible")
            break
    else:
        print("possible")
        for i in res:
            print("".join(i))


if __name__ == '__main__':
    resolve()
