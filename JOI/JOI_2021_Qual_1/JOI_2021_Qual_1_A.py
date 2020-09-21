# https://atcoder.jp/contests/joi2021yo1a/submissions/16942858
# A - 2 番目に大きい整数 (The Second Largest Integer)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = list(map(int, input().split()))
    ABC.sort()
    print(ABC[1])


if __name__ == '__main__':
    resolve()
