# https://atcoder.jp/contests/arc034/submissions/13473390
# B - 方程式
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


# nの桁和を返す
def digit_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def resolve():
    """
    解法概要；
        f(x)の値はxに比べて小さく、最大でも精々17*9=153のため、(n-桁数×9)～nの間で全探索すればよい。

    :return:
    """
    n = int(input())
    a = len(str(n)) * 9

    res = []
    for i in range(max(0, n - a), n):
        if i + digit_sum(i) == n:
            res.append(i)

    print(len(res))
    if len(res) != 0:
        print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
