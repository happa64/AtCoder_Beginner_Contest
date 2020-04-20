# https://atcoder.jp/contests/abc010/tasks/abc010_3
# C - 浮気調査
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    txa, tya, txb, tyb, T, V = map(int, input().split())
    n = int(input())
    XY = list(map(int, input().split()) for _ in range(n))
    D = T * V

    # 電話前と家の距離をa、家の距離と電話後の距離をb、TV=Dとすると√a + √b <= Dとなるか判定すればよい
    # しかしこのまま実装するとルートをとる為、浮動小数点の誤差によりWAとなる
    # 上式をTV^4 - 2aD^2 - 2bD^2 + a^2 + b^2 - 2ab >= 0に変形することで正確に判定することが出来る
    for x, y in XY:
        a = pow(x - txa, 2) + pow(y - tya, 2)
        b = pow(txb - x, 2) + pow(tyb - y, 2)
        if pow(D, 4) - 2 * a * pow(D, 2) - 2 * b * pow(D, 2) + pow(a, 2) + pow(b, 2) - 2 * a * b >= 0:
            print("YES")
            exit()
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
