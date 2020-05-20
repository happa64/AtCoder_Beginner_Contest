# https://atcoder.jp/contests/abc112/submissions/12806702
# D - Partition
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


# 約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def resolve():
    """
    解法概要：
        例えば、n = 3 ，m = 12の場合、aは(4, 4, 4)以上になりえない。そのため、解の候補は、m // n以下である。
        問題は、「a全てが、ある整数dの倍数、かつ合計がmであるときの、dの最大値を求めよ」と言い換えることが出来る。
        この時、配列aは(d, d, d, ・・・, d, m - d * (n - 1))と表せられる。
        つまり、m - d * (n - 1) ≡ 0 (mod d)であり、これを変形し、m ≡ d * (n - 1)(mod d)が成立する必要がある。
        上記式が成立する時、dはmの約数でなければならないことが分かる。
        つまりm // n以下の、mの約数の最大値が解となる。

    計算量：O(√M)
    :return:
    """
    n, m = map(int, input().split())

    ma = m // n

    div = make_divisors(m)
    res = 1
    for d in div:
        if d <= ma:
            res = d
        else:
            break

    print(res)


if __name__ == '__main__':
    resolve()
