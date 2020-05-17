# https://atcoder.jp/contests/abc035/submissions/13288989
# C - オセロ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())
    LR = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]

    # imos法
    imos = [0 for _ in range(n + 1)]
    for i in range(q):
        l, r = LR[i]
        imos[l] += 1
        imos[r + 1] -= 1

    # 累積和
    R = [0]
    for cnt in imos:
        R.append(R[-1] + cnt)

    # 裏返した回数が偶数回であれば0、奇数回であれば1になる
    res = ""
    for i in range(1, n + 1):
        res += "0" if R[i] % 2 == 0 else "1"

    print(res)


if __name__ == '__main__':
    resolve()
