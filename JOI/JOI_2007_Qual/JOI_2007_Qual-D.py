# https://atcoder.jp/contests/joi2007yo/submissions/16034525
# D - カードの並び替え
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def cut(L, k):
        tmp = []
        L1 = L[:k]
        L2 = L[k:]
        tmp.extend(L2)
        tmp.extend(L1)
        return tmp

    def shuffle(L):
        tmp = []
        L1 = L[:n]
        L2 = L[n:]
        for i in range(2 * n):
            card = L1.pop(0) if i % 2 == 0 else L2.pop(0)
            tmp.append(card)
        return tmp

    n = int(input())
    m = int(input())
    K = list(int(input()) for _ in range(m))

    cards = list(range(1, 2 * n + 1))
    for i in range(m):
        k = K[i]
        if k == 0:
            cards = shuffle(cards)
        else:
            cards = cut(cards, k)
    print(*cards, sep="\n")


if __name__ == '__main__':
    resolve()
