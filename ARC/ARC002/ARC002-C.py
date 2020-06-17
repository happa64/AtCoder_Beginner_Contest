# https://atcoder.jp/contests/arc002/submissions/13102813
# C - コマンド入力
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    c = list(input())

    res = f_inf
    # LとRにアサインする組み合わせを全通り考える
    for L in product(["A", "B", "X", "Y"], repeat=2):
        for R in product(["A", "B", "X", "Y"], repeat=2):
            L = "".join(list(L))
            R = "".join(list(R))

            cnt = n
            i = 0
            while i < n:
                # コマンドを前から二つずつ見た時、LRのどちらかに一致していれば、入力回数を1引いて、2進める
                if "".join(c[i: i + 2]) == L:
                    cnt -= 1
                    i += 2
                elif "".join(c[i: i + 2]) == R:
                    cnt -= 1
                    i += 2
                # LRのどちらとも一致しない場合は、1進める
                else:
                    i += 1

            res = min(res, cnt)

    print(res)


if __name__ == '__main__':
    resolve()
