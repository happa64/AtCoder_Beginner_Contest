# https://atcoder.jp/contests/agc029/tasks/agc029_a
# A - Irreversible operation
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    # 操作が不可能になった時点で、石の配置は必ず・・・WWWWWBBBBB・・・となる
    # つまり、Wを左に移動する回数を求めれば良く、これは初期配置でWの左側にあるBを数え上げることで求まる
    cnt_B = 0
    res = 0
    for i in s:
        if i == "B":
            cnt_B += 1

        if i == "W":
            res += cnt_B

    print(res)


if __name__ == '__main__':
    resolve()
