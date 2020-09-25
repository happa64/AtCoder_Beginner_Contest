# https://atcoder.jp/contests/joi2019ho/submissions/16998648
# A - 勇者ビ太郎 (Bitaro the Brave)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = list(input().rstrip() for _ in range(H))

    res = 0
    cnt_I = [0] * W
    for h in reversed(range(H)):
        cnt_O = 0
        for w in reversed(range(W)):
            if S[h][w] == "J":
                res += cnt_O * cnt_I[w]
            elif S[h][w] == "O":
                cnt_O += 1
            else:
                cnt_I[w] += 1
    print(res)


if __name__ == '__main__':
    resolve()
