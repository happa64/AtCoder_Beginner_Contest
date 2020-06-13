# https://atcoder.jp/contests/abc096/submissions/14212870
# D - Five, Five Everywhere
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def is_prime(n):
        if n == 1:
            return False
        for k in range(2, int(pow(n, 0.5)) + 1):
            if n % k == 0:
                return False
        return True

    n = int(input())

    res = []
    for i in range(2, 55556):
        if is_prime(i):
            if i % 5 == 1:
                res.append(i)
        if len(res) == n:
            print(*res)
            break


if __name__ == '__main__':
    resolve()
