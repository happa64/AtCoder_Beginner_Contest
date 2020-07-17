# https://atcoder.jp/contests/arc024/submissions/15284240
# B - 赤と黒の木
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    Col = list(int(input()) for _ in range(n))

    if len(set(Col)) == 1:
        print(-1)
        exit()

    L = 1
    Len = []
    for i in range(1, n):
        if Col[i] == Col[i - 1]:
            L += 1
        else:
            Len.append(L)
            L = 1
    Len.append(L)

    if Col[0] == Col[-1]:
        Len.append(Len[0] + Len[-1])

    res = (max(Len) + 1) // 2
    print(res)


if __name__ == '__main__':
    resolve()
