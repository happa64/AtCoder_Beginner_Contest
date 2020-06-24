# https://atcoder.jp/contests/abc147/submissions/12842252
# C - HonestOrUnkind2
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    query = [[] for _ in range(n)]
    for i in range(n):
        a = int(input())
        for _ in range(a):
            x, y = map(int, input().split())
            query[i].append([x - 1, y])

    res = 0
    # 1:正直，0:不親切のパターンを全列挙し、証言に矛盾が無かったパターンを調べる
    for pattern in product([0, 1], repeat=n):
        for idx, p in enumerate(pattern):
            if p == 1:
                for x, y in query[idx]:
                    if pattern[x] != y:
                        break
                else:
                    continue
                break
        else:
            res = max(res, sum(pattern))

    print(res)


if __name__ == '__main__':
    resolve()
