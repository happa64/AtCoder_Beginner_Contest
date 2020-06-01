# https://atcoder.jp/contests/abc012/submissions/13939287
# B - 入浴時間
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H, n = divmod(n, 3600)
    M, S = divmod(n, 60)
    print(":".join([str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)]))


if __name__ == '__main__':
    resolve()
