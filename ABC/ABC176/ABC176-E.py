# https://atcoder.jp/contests/abc176/submissions/16136789
# E - Bomber
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, m = map(int, input().split())
    H_list = [0] * H
    W_list = [0] * W
    bomb = []
    for _ in range(m):
        h_, w_ = map(lambda x: int(x) - 1, input().split())
        H_list[h_] += 1
        W_list[w_] += 1
        bomb.append([h_, w_])

    ma = max(H_list) + max(W_list)
    cnt_H = Counter(H_list)
    cnt_W = Counter(W_list)
    cnt = 0
    for k, v in cnt_H.items():
        if cnt_W.get(ma - k) is not None:
            cnt += v * cnt_W[ma - k]

    for h, w in bomb:
        total = H_list[h] + W_list[w]
        if total == ma:
            cnt -= 1
    if cnt:
        print(ma)
    else:
        print(ma - 1)


if __name__ == '__main__':
    resolve()
