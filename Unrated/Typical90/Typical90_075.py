# https://atcoder.jp/contests/typical90/submissions/23739757
# 075 - Magic For Balls（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())

    cnt = 1
    update = True
    while update:
        update = False
        for i in range(2, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                n //= i
                cnt += 1
                update = True
                break

    res = 0
    while cnt != 1:
        cnt = (cnt + 1) // 2
        res += 1
    print(res)


if __name__ == '__main__':
    solve()
