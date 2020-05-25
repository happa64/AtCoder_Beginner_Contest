# https://atcoder.jp/contests/arc033/submissions/13589653
# B - メタ構文変数
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    na, nb = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = set(A + B)
    B = set(B)
    cnt = 0
    for a in A:
        if a in B:
            cnt += 1
    print(cnt / len(C))


if __name__ == '__main__':
    resolve()
