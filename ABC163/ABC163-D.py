# https://atcoder.jp/contests/abc163/tasks/abc163_d
# D - Sum of Large Numbers
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    res = 0
    # 選ぶ個数が異なる時、和が重複することは無いため、i個選んだ時の和の数の総和を考えればよい
    # i個選んだ時の和の数は、（数値が大きい順にi個選んだ時の和）-（数値が小さい順にi個選んだ時の和）である
    for i in range(k, n + 2):
        mi = (i - 1) * i // 2
        ma = n * (n + 1) // 2 - (n - i) * (n - i + 1) // 2
        res += ma - mi + 1
        res %= mod

    print(res)


if __name__ == '__main__':
    resolve()
