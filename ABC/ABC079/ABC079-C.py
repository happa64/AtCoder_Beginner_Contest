# https://atcoder.jp/contests/abc079/submissions/13430055
# C - Train Ticket
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要；
        +と-のパターンを全部試し、7になった式を出力すれば良い。

    計算量：O(2^3)
    """
    ABCD = list(input())

    # bit全探索
    for pattern in product(["+", "-"], repeat=3):
        # zipを使いたいが、番号が4つに対し演算子が3つのため、1つ空白を追加し配列長をそろえる
        pattern = list(pattern) + [" "]

        # 式の作成
        fomula = []
        for op, num in zip(pattern, ABCD):
            fomula.append(num)
            fomula.append(op)
        fomula = "".join(fomula).rstrip()

        # 式が7になるか判定
        if eval(fomula) == 7:
            print(fomula + "=" + "7")
            exit()


if __name__ == '__main__':
    resolve()
