# https://atcoder.jp/contests/arc046/submissions/14402976
# A - ゾロ目数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    zorome = []
    for i in range(1, 555556):
        i = str(i)
        if len(i) == 1:
            zorome.append(i)
        else:
            for j in range(1, len(i)):
                if i[j - 1] != i[j]:
                    break
            else:
                zorome.append(i)
    print(zorome[n - 1])


if __name__ == '__main__':
    resolve()
