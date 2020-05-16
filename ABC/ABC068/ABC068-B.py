# https://atcoder.jp/contests/abc068/submissions/12235009
# B - Break Number
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 0
    ans = 0
    for i in range(1, n + 1):
        n = int(str(i)[::])
        cnt = 0
        while n % 2 == 0:
            n //= 2
            cnt += 1

        if res <= cnt:
            res = cnt
            ans = i
    print(ans)


if __name__ == '__main__':
    resolve()
