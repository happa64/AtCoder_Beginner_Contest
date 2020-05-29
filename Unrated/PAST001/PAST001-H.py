# https://atcoder.jp/contests/past201912-open/tasks/past201912_h
# H - まとめ売り
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    # セット販売できるか否か？というクエリは最小値を見れば判断できる
    # 奇数番号、偶数番号のカードの最小値を前処理しておき、販売するたびに最小値を更新していけば良い
    n = int(input())
    C = [f_inf] + list(map(int, input().split()))
    odd_min = min([C[i] for i in range(1, n + 1, 2)])
    even_min = min([C[i] for i in range(0, n + 1, 2)])

    q = int(input())
    S = list(list(map(int, input().split())) for _ in range(q))

    res = 0
    # 奇数番号、偶数番号のカードをセット販売した合計枚数を加算しておく
    # 単品販売する場合は、そのセット販売した合計枚数を引いた値がa枚以上であればよい
    odd_saled, even_saled = 0, 0
    for query in S:
        if query[0] == 1:
            _, x, a = query
            if x % 2 != 0:
                if C[x] - odd_saled >= a:
                    res += a
                    C[x] -= a
                    odd_min = min(odd_min, C[x])
            else:
                if C[x] - even_saled >= a:
                    res += a
                    C[x] -= a
                    even_min = min(even_min, C[x])

        elif query[0] == 2:
            _, a = query
            if odd_min >= a:
                res += a * ((n + 1) // 2)
                odd_min -= a
                odd_saled += a

        else:
            _, a = query
            if min(even_min, odd_min) >= a:
                res += a * n
                odd_min -= a
                odd_saled += a
                even_min -= a
                even_saled += a

    print(res)


if __name__ == '__main__':
    resolve()
