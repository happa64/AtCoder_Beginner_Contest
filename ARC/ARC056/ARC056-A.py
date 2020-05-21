# https://atcoder.jp/contests/arc056/submissions/13454157
# A - みんなでワイワイみかん
import sys
import math

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, k, l = map(int, input().split())

    res1 = 0
    # セットで出来る限り買い、余ったものを単品で買う
    res1 += (k // l) * b
    amari = k % l
    res1 += amari * a

    # 全てセットで買う
    res2 = math.ceil(k / l) * b

    print(min(res1, res2))


if __name__ == '__main__':
    resolve()
