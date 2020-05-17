# https://atcoder.jp/contests/arc020/submissions/13281269
# B - 縞模様
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, c = map(int, input().split())
    A = list(int(input()) - 1 for _ in range(n))

    res = f_inf
    # 使う二色を決め打ちし（10×10=100通り）、コストを計算する
    for x in range(10):
        for y in range(10):
            if x == y:
                continue

            cost = 0
            for i in range(n):
                if i % 2 == 0:
                    if A[i] != x:
                        cost += c
                else:
                    if A[i] != y:
                        cost += c

            res = min(res, cost)

    print(res)


if __name__ == '__main__':
    resolve()
