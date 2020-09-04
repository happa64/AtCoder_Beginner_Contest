# https://atcoder.jp/contests/abc031/submissions/16501252
# D - 語呂合わせ
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k, n = map(int, input().split())
    query = [list(input().split()) for _ in range(n)]

    for pattern in product([1, 2, 3], repeat=k):
        D = dict()
        for v, w in query:
            left = 0
            if sum([pattern[int(num) - 1] for num in v]) != len(w):
                break
            for num in v:
                length = pattern[int(num) - 1]
                ss = w[left: left + length]
                if D.get(int(num) - 1) is None:
                    D[int(num) - 1] = ss
                    left += length
                elif D.get(int(num) - 1) != ss:
                    break
                else:
                    left += length
            else:
                continue
            break
        else:
            for i in range(k):
                print(D[i])
            break


if __name__ == '__main__':
    resolve()
