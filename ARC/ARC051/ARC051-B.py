# https://atcoder.jp/contests/arc051/submissions/13174105
# B - 互除法
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())

    f = [f_inf for _ in range(50)]
    f[0], f[1] = 0, 1

    def Fib(n):
        if f[n - 1] != f_inf:
            return f[n - 1]
        else:
            f[n - 1] = Fib(n - 1) + Fib(n - 2)
            return Fib(n - 1) + Fib(n - 2)

    Fib(50)
    print(f[k - 1], f[k])


def resolve2():
    k = int(input())
    fib = [1, 1]
    for i in range(50):
        fib.append(fib[-1] + fib[-2])

    print(fib[k - 1], fib[k])


if __name__ == '__main__':
    resolve()
