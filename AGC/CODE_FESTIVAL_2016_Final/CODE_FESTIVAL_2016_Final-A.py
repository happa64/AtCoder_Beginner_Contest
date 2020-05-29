# https://atcoder.jp/contests/cf16-final/submissions/13677844
# A - Where's Snuke?
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = [list(input().split()) for _ in range(H)]

    for w in range(W):
        for h in range(H):
            if S[h][w] == "snuke":
                break
        else:
            continue
        break

    print(chr(65 + w) + str(h + 1))


if __name__ == '__main__':
    resolve()
