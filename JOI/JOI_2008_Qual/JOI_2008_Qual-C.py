# https://atcoder.jp/contests/joi2008yo/submissions/15089127
# C - カードゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(int(input()) for _ in range(n))
    T = sorted(C)
    H = sorted([i for i in range(1, n * 2 + 1) if i not in T])
    card = -1
    tarou, hanako = 0, 0
    flg = 1
    while len(T) and len(H):
        if flg:
            for i in range(len(T)):
                if card < T[i]:
                    card = T[i]
                    T.pop(i)
                    break
            else:
                card = -1
            flg ^= 1
        else:
            for i in range(len(H)):
                if card < H[i]:
                    card = H[i]
                    H.pop(i)
                    break
            else:
                card = -1
            flg ^= 1
    print(len(H), len(T), sep="\n")


if __name__ == '__main__':
    resolve()
