# https://atcoder.jp/contests/agc017/tasks/agc017_a
# A - Biscuits
import sys
from math import factorial

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, p = map(int, input().split())
    A = list(map(int, input().split()))

    # 袋の中身が偶数個のものと、奇数個のものをカウント
    cnt_odd = 0
    for i in range(n):
        if A[i] % 2 != 0:
            cnt_odd += 1
    cnt_even = n - cnt_odd

    # odd：全て奇数の袋かつ選ぶ袋の数も奇数の場合＝合計が奇数になる場合の数
    odd = 0
    for r in range(1, n + 1, 2):
        if cnt_odd - r >= 0:
            odd += factorial(cnt_odd) // factorial(r) // factorial(cnt_odd - r)

    # even：全て偶数の袋を選ぶ場合＝合計が偶数になる場合の数
    even = pow(2, cnt_even)

    # 合計が奇数になる場合は、(偶数) + (奇数)の場合のみ
    # つまり、oddとevenを掛け合わせると、合計が奇数になる場合の数が分かる
    odd_pattern = even * odd

    total = pow(2, n)
    if p == 0:
        print(total - odd_pattern)
    else:
        print(odd_pattern)


if __name__ == '__main__':
    resolve()
