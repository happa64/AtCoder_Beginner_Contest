# https://atcoder.jp/contests/abc065/submissions/13479836
# C - Reconciled?
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        まず、犬と猿の数が2以上異なっていれば、並べることは出来ない。
        犬と猿を独立に並べるとすると、それぞれの並べ方の場合の数は、N!とM!である。
        よって、解はN!×M!×(交互になる並べ方)である。

        犬と猿の数の差が1の時は、例えば、犬猿犬猿犬、のように交互になる並べ方は1通りである。
        犬と猿の数の差が2の時は、例えば、犬猿犬猿、猿犬猿犬、のように交互になる並べ方は2通りである。

    計算量：O(max(N,M))
    """
    n, m = map(int, input().split())

    if abs(n - m) >= 2:
        print(0)
        exit()

    # 階乗(mod 10**9+7)の前処理
    fact = [1]
    for i in range(2, max(n, m) + 1):
        fact.append((fact[-1] * i) % mod)

    res = fact[n - 1] * fact[m - 1] % mod
    print(res if n != m else res * 2 % mod)


if __name__ == '__main__':
    resolve()
