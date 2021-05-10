# https://codeforces.com/contest/1455/submission/100003388
# A - Strange Functions
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def g(x):
        return x / f(f(x))

    def f(x):
        x = str(x)
        X = list(x[::-1])
        while X:
            if X[0] != "0":
                break
            X.pop(0)
        x = "".join(X)
        return int(x)

    t = int(input())
    for _ in range(t):
        n = int(input())
        res = set()
        i = 1
        while i <= n:
            res.add(g(i))
            i *= 10
        print(len(res))


if __name__ == '__main__':
    resolve()
