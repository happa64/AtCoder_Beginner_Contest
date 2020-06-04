# https://atcoder.jp/contests/abc084/tasks/abc084_d
# D - 2017-like Number
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


# 素数判定
def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(pow(n, 0.5)) + 1):
        if n % k == 0:
            return False
    return True


def resolve():
    q = int(input())
    LR = [list(map(int, input().split())) for _ in range(q)]

    # 1であれば2017に似た整数、0であれば2017に似ていない数字
    Lile_2017 = [0] * (10 ** 5 + 1)

    # 素数判定済み配列
    prime = set()
    not_prime = set()

    # 1~100000が2017に似た数かどうか判定する
    for n in range(1, 10 ** 5 + 1):
        flg1, flg2 = False, False
        if n % 2 != 0:
            if n in prime:
                flg1 = True
            elif n in not_prime:
                flg1 = False
            else:
                flg1 = is_prime(n)
                prime.add(n) if flg1 else not_prime.add(n)

            if (n + 1) // 2 in prime:
                flg2 = True
            elif (n + 1) // 2 in not_prime:
                flg2 = False
            else:
                flg2 = is_prime((n + 1) // 2)
                prime.add((n + 1) // 2) if flg1 else not_prime.add((n + 1) // 2)

        Lile_2017[n - 1] += 1 if flg1 and flg2 else 0

    # 2017に似た数の累積和配列を作る
    Ruiseki = [0]
    for i in range(1, 10 ** 5 + 1):
        Ruiseki.append(Ruiseki[-1] + Lile_2017[i - 1])

    # クエリに答える
    for l, r in LR:
        print(Ruiseki[r] - Ruiseki[l - 1])


if __name__ == '__main__':
    resolve()
