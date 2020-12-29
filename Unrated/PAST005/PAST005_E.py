# https://atcoder.jp/contests/past202012-open/submissions/19042600
# E - ハンコ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def rotation(L, num):
        if num == 0:
            res = [[""] * W for _ in range(H)]
            for h in range(H):
                for w in range(W):
                    res[h][w] = L[h][w]
        elif num == 1:
            res = [[""] * H for _ in range(W)]
            for h in range(H):
                for w in range(W):
                    res[w][H - 1 - h] = L[h][w]
        elif num == 2:
            res = [[""] * W for _ in range(H)]
            for h in range(H):
                for w in range(W):
                    res[h][w] = L[-(h + 1)][-(w + 1)]
        else:
            res = [[""] * H for _ in range(W)]
            for h in range(H):
                for w in range(W):
                    res[W - 1 - w][h] = L[h][w]
        return res

    H, W = map(int, input().split())
    S = list(input().rstrip() for _ in range(H))
    T = list(input().rstrip() for _ in range(H))
    tot = sum([T[h][w] == "#" for h in range(H) for w in range(W)])

    for i in range(4):
        T_ = rotation(T, i)
        if i == 0 or i == 2:
            for h in range(H):
                for w in range(W):
                    for offset_h in range(H):
                        for offset_w in range(W):
                            cnt = 0
                            for dh in range(H):
                                for dw in range(W):
                                    now_h, now_w = h + dh, w + dw
                                    if now_h >= H or now_w >= W or S[now_h][now_w] == "#":
                                        continue
                                    if offset_h + dh >= H or offset_w + dw >= W:
                                        continue
                                    if T_[offset_h + dh][offset_w + dw] == "#":
                                        cnt += 1
                            if cnt == tot:
                                print("Yes")
                                exit()
        else:
            for h in range(H):
                for w in range(W):
                    for offset_h in range(W):
                        for offset_w in range(H):
                            cnt = 0
                            for dh in range(H):
                                for dw in range(W):
                                    now_h, now_w = h + dh, w + dw
                                    if now_h >= H or now_w >= W or S[now_h][now_w] == "#":
                                        continue
                                    if offset_h + dh >= W or offset_w + dw >= H:
                                        continue
                                    if T_[offset_h + dh][offset_w + dw] == "#":
                                        cnt += 1
                            if cnt == tot:
                                print("Yes")
                                exit()

    print("No")


if __name__ == '__main__':
    resolve()
