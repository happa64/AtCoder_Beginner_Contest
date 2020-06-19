# https://atcoder.jp/contests/arc009/submissions/13114796
# B - おとぎの国の高橋君
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    B = list(map(str, input().split()))
    n = int(input())
    A = sorted(input() for _ in range(n))

    C = []
    for a in A:
        a_b = ""
        for i in a:
            a_b += str(B.index(i))
        C.append([int(a_b), int(a)])

    C = sorted(C, key=lambda x: x[0])

    for c in C:
        print(c[1])


if __name__ == '__main__':
    resolve()
