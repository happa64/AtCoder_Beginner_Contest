# https://atcoder.jp/contests/arc004/submissions/13108664
# B - 2点間距離の最大と最小 ( Maximum and Minimum )
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    D = list(int(input()) for _ in range(n))

    # 最大の距離は点をトポロジカル順に並べた場合である
    max_dist = sum(D)

    # トポロジカル順に並べた時、左端からの累積和と、右端からの累積和と計算する
    Ruiseki_left, Ruiseki_right = [0], [0]
    for i in range(n):
        Ruiseki_left.append(Ruiseki_left[-1] + D[i])
        Ruiseki_right.append(Ruiseki_right[-1] + D[-(i + 1)])

    # 右端からi番目の点を折り返し、左端からj番目の点を折り返し場合を全探索する
    min_dist = max_dist
    for i in range(n):
        for j in range(n - i):
            dist = abs(max_dist - Ruiseki_left[i] * 2 - Ruiseki_right[j] * 2)
            min_dist = min(min_dist, dist)
            if i > 0 and j > 0:
                # 右端からi番目までの距離：a、左端からj番目までの距離：b、その間の距離：c
                a = Ruiseki_left[i]
                b = Ruiseki_right[j]
                c = max_dist - a - b

                # a,b,cで三角形が作れれば0番目とN番目の距離は0になる
                if a + b > c and b + c > a and c + a > b:
                    min_dist = 0
                    break

    print(max_dist)
    print(min_dist)


if __name__ == '__main__':
    resolve()
