# https://atcoder.jp/contests/abc010/tasks/abc010_2
# B - 花占い
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    # 〇：好き、✖：嫌いとするとパターンは6毟り毎に元に戻ることがわかる
    # 〇✖〇✖〇✖|〇✖〇✖〇✖
    # 〇✖〇〇✖〇|〇✖〇〇✖〇
    # mod 6のパターンを全て列挙すればOK
    for i in range(n):
        if A[i] % 6 == 0:
            res += 3
        elif A[i] % 6 == 2:
            res += 1
        elif A[i] % 6 == 4:
            res += 1
        elif A[i] % 6 == 5:
            res += 2

    print(res)


if __name__ == '__main__':
    resolve()
