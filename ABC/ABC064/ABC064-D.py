# https://atcoder.jp/contests/abc064/tasks/abc064_d
# D - Insertion
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    insert_L = 0
    cnt_L = 0

    # 正しい括弧の時、(と)の数は同じになる
    # 左側に(、右側に)を挿入するのが最も辞書順最小となる
    for s in S:
        # 文字列を先頭から見ていき、(の数を加算し、)が出てきたら減算する
        if s == '(':
            cnt_L += 1
        else:
            if cnt_L:
                cnt_L -= 1
            # もし、(の数がゼロであれば、左側に挿入する(の数を加算する
            else:
                insert_L += 1

    insert_R = cnt_L

    res = '(' * insert_L + S + ')' * insert_R
    print(res)


if __name__ == '__main__':
    resolve()
