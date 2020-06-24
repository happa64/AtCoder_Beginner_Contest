# https://atcoder.jp/contests/arc035/submissions/13172753
# B - アットコーダー王国のコンテスト事情
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T = sorted(list(int(input()) for _ in range(n)))

    # 解答時間をソートし、先頭から解くとペナルティを最小にできる
    R = [0]
    for i in range(n):
        R.append(R[-1] + T[i])

    # n!を前処理しておく
    fact = [1]
    for i in range(2, 10 ** 5):
        fact.append((fact[-1] * i) % mod)

    # 組み合わせは、(Tiの種類)!のを全て掛け合わせた値である
    D = Counter(T)
    res = 1
    for v in D.values():
        res = res * fact[v - 1] % mod

    print(sum(R))
    print(res)


if __name__ == '__main__':
    resolve()
