# https://atcoder.jp/contests/arc006/submissions/14446208
# A - 宝くじ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    E = list(map(int, input().split()))
    B = int(input())
    L = list(map(int, input().split()))

    cnt = 0
    for l in L:
        if l in E:
            cnt += 1

    if cnt == 6:
        print(1)
    elif cnt == 5:
        if B in L:
            print(2)
        else:
            print(3)
    elif cnt == 4:
        print(4)
    elif cnt == 3:
        print(5)
    else:
        print(0)


if __name__ == '__main__':
    resolve()
