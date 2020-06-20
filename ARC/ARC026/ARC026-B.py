# https://atcoder.jp/contests/arc026/submissions/14487515
# B - 完全数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def solve(n):
        res = [1]
        for i in range(2, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
        return res

    n = int(input())
    if n == 1:
        print("Deficient")
        exit()

    res = sum(solve(n))
    print("Perfect" if res == n else "Abundant" if res > n else "Deficient")


if __name__ == '__main__':
    resolve()
