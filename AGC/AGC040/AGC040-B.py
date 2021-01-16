# https://atcoder.jp/contests/agc040/submissions/19452515
# B - Two Contests
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    ma = -f_inf  # 右端の区間の左側
    mi = f_inf  # 左端の区間の右側
    LR = []
    for _ in range(n):
        l, r = map(int, input().split())
        r += 1  # 半開区間にする
        ma = max(ma, l)
        mi = min(mi, r)
        LR.append((l, r))

    res = 0
    t = []
    for l, r in LR:
        # パターン1: 今見てる区間を独立、それ以外を右端と左端の区間と同じグループにする
        res = max(res, max(0, mi - ma) + r - l)
        # パターン2: 右端と左端を別のグループに分け、各区間をそれぞれ貪欲に割り当てていく
        a = max(0, mi - l)  # 左端の区間のグループに割り当て
        b = max(0, r - ma)  # 右端の区間のグループに割り当て
        t.append((a, b))

    # 「(a, b)のペアから、aとbを一個だけ選ぶ操作をn個全てのペアに対して行う。min{a}+min{b}の最大値を求めよ」
    # という問題帰結でき、これはaを昇順,bを降順にソートして前から見ていくことで解ける。
    t.sort(key=lambda x: [x[0], -x[1]])
    w = f_inf
    for i in range(n):
        a, b = t[i]
        if i != 0:
            res = max(res, w + a)
        w = min(w, b)
    print(res)


if __name__ == '__main__':
    resolve()
