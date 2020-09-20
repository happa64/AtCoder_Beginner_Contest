# https://atcoder.jp/contests/ddcc2017-final/submissions/16906702
# A - 正方形のチップ２
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def calc(R):
        r = R // 2
        res = 0
        for i in range(R // k):
            x = i * k - r
            for j in range(R // k):
                y = j * k - r
                if x ** 2 + y ** 2 <= r ** 2 and (x + k) ** 2 + y ** 2 <= r ** 2 and x ** 2 + (y + k) ** 2 <= r ** 2\
                        and (x + k) ** 2 + (y + k) ** 2 <= r ** 2:
                    res += 1
        return res

    k = int(input())
    print(calc(200), calc(300))


if __name__ == '__main__':
    resolve()
