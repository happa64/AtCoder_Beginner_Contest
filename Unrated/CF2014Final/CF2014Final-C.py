# https://atcoder.jp/contests/code-festival-2014-final/submissions/13588929
# C - N進数
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())

    def f(N):
        res = 0
        n = str(N)[::-1]
        for i in range(len(n)):
            res += pow(N, i) * int(n[i])
        return res

    for k in range(10, 10001):
        if f(k) == a:
            print(k)
            break
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
