# https://atcoder.jp/contests/abc162/tasks/abc162_e
# E - Sum of gcd of Tuples (Hard)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    D = [0] * (k + 1)

    # 最大公約数がiの倍数となるような数列の数は(k // i)^nで求められる
    for i in range(1, k + 1):
        D[i] = pow(k // i, n, mod)

    # 最大公約数がi丁度になるような数列の数は「iの倍数かつ、2i,3i,4i,・・・、(k+1)iではない数」である
    # 倍数の累積和を分解していくイメージ？
    # iを大きい順見ていき、iの倍数の個数を引いていけば、最大公約数がiとなる数列の個数が求まる
    for i in range(k, 0, -1):
        for j in range(2 * i, k + 1, i):
            D[i] = (D[i] - D[j]) % mod

    # 最大公約数がiとなる個数とiを掛け合わせたものの総和が答えとなる
    res = 0
    for i in range(1, k + 1):
        res = (res + D[i] * i) % mod

    print(res)


if __name__ == '__main__':
    resolve()
