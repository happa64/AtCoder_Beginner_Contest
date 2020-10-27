# https://atcoder.jp/contests/tenka1-2012-qualB/submissions/17688950
# C - 席が足りない
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    MAX = 24 * 60
    T = []
    for _ in range(n):
        Ts, Te = input().split()
        h, m = map(int, Ts.split(":"))
        Ts = h * 60 + m
        h, m = map(int, Te.split(":"))
        Te = h * 60 + m
        T.append((Ts, Te))

    T.sort()
    ok = [[True] * n for _ in range(n)]
    for i in range(n):
        shift = [0] * MAX
        for j in range(T[i][0], T[i][1]):
            shift[j % MAX] = 1
        for j in range(i + 1, n):
            for k in range(T[j][0], T[j][1]):
                if shift[k % MAX]:
                    ok[i][j] = ok[j][i] = False
                    break

    res = 0
    not_used = list(range(n))
    while not_used:
        res += 1
        used = []
        next_not_used = []
        for i in not_used:
            for j in used:
                if not ok[i][j]:
                    next_not_used.append(i)
                    break
            else:
                used.append(i)
        not_used = next_not_used
    print(res)


if __name__ == '__main__':
    resolve()
