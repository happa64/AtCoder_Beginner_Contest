# https://atcoder.jp/contests/tenka1-2012-qualC/submissions/13112930
# B - ロイヤルストレートフラッシュ
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K"]

    # ロイヤルストレートフラッシュのカードを列挙
    Royal = []
    for i in ["S", "H", "D", "C"]:
        for j in ["A", "10", "J", "Q", "K"]:
            Royal.append(i + j)

    # 文字列をカード毎に分離
    card = []
    for i in range(len(s)):
        if s[i] in number:
            card.append(s[i - 1:i + 1]) if s[i] != "1" else card.append(s[i - 1:i + 2])

    # 山札の上からロイヤルストレートフラッシュの候補を見ていき、ロイヤルストレートフラッシュが出来たらカードのマークを記録する
    d = defaultdict(int)
    mark = ""
    for c in card:
        if c in Royal:
            d[c[0]] += 1
            if d[c[0]] == 5:
                mark = c[0]
                break

    res = ""
    cnt = 0
    # 手札が5枚になるまで、ロイヤルストレートフラッシュの候補以外かつ、マークがmark以外のカードを捨てていく
    for c in card:
        if c in Royal:
            if c[0] == mark:
                cnt += 1
                if cnt == 5:
                    break
            else:
                res += c
        else:
            res += c

    print(0) if res == "" else print(res)


if __name__ == '__main__':
    resolve()
