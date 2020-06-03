# https://atcoder.jp/contests/agc004/tasks/agc004_a
# A - Divide a Cuboid
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = sorted(list(map(int, input().split())))

    for i in ABC:
        if i % 2 == 0:
            print(0)
            break
    else:
        print(ABC[0] * ABC[1])


if __name__ == '__main__':
    resolve()
