# https://atcoder.jp/contests/arc054/submissions/14153323
# B - ムーアの法則
import sys
import math

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    P(x) = x+P*2^(-x/1.5)は下に凸な関数であるため、微分した式が0になるようなxを求めれば良い。
    """
    P = float(input())
    x = max(0, -1.5 * math.log2(1.5 / (P * math.log(2))))
    res = x + P * pow(2, -x / 1.5)
    print(res)


def resolve2():
    """
    三分探索
    """
    def ternary_search(high, low):
        while abs(high - low) > 10 ** (-9):
            mid_left = high / 3 + low * 2 / 3
            mid_right = high * 2 / 3 + low / 3
            if f(mid_left) >= f(mid_right):
                low = mid_left
            else:
                high = mid_right
        return f(high)

    def f(x):
        return x + p / pow(2, x / 1.5)

    p = float(input())
    res = ternary_search(100, 0)
    print(res)


if __name__ == '__main__':
    resolve()
