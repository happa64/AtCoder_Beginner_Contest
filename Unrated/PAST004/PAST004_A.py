# https://atcoder.jp/contests/past202010-open/submissions/18010669
# A - 中央値
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = list(map(int, input().split()))
    ABC = [[num, idx] for idx, num in enumerate(ABC)]
    ABC.sort()
    res = ABC[1][1]
    if res == 0:
        print("A")
    elif res == 1:
        print("B")
    else:
        print("C")


if __name__ == '__main__':
    resolve()
