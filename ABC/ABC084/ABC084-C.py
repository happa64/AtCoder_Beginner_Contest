# https://atcoder.jp/contests/abc084/submissions/14005490
# C - Special Trains
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    CSF = [list(map(int, input().split())) for _ in range(n - 1)]

    for i in range(n):
        if i == n - 1:
            print(0)
            break
        c1, s1, _ = CSF[i]
        t = s1 + c1
        for j in range(i + 1, n - 1):
            c2, s2, f2 = CSF[j]
            if t <= s2:
                t = s2 + c2
            else:
                if t % f2 == 0:
                    wait = 0
                else:
                    wait = f2 - (t - s2) % f2
                t += c2 + wait
        print(t)


if __name__ == '__main__':
    resolve()
