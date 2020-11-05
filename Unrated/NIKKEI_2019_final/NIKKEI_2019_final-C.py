# https://atcoder.jp/contests/nikkei2019-final/submissions/17894858
# C - Come Together
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def ternary_search(left, right, l, L):
        """
        f=凸関数の式
        :param left:取りうる一番大きい値
        :param right:取りうる一番小さい値
        :return: 凸関数の極小値（極大値）
        """
        for _ in range(100):
            mid_right = (left * 2 + right) // 3
            mid_left = (left + right * 2) // 3
            if f(mid_right, l, L) < f(mid_left, l, L):
                right = mid_left
            else:
                left = mid_right

        mi = f_inf
        for i in range(left, right + 1):
            mi = min(mi, f(i, l, L))

        return mi

    def f(x, l, cnt):
        ret = 0
        for i in range(1, l + 1):
            ret += abs(x - i) * cnt[i]
        return ret

    h, w, k = map(int, input().split())

    hc = [h] * (w + 1)
    wc = [w] * (h + 1)
    for _ in range(k):
        r, c = map(int, input().split())
        wc[r] -= 1
        hc[c] -= 1

    res = 0
    res += ternary_search(0, h, h, wc)
    res += ternary_search(0, w, w, hc)
    print(res)


if __name__ == '__main__':
    resolve()
