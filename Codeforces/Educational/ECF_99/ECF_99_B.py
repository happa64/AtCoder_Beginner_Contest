# https://codeforces.com/contest/1455/submission/100027049
# B - Jumps
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        x = int(input())
        i = 0
        step = 1
        while i < x:
            i += step
            step += 1
        step -= 1

        diff = i - x
        if diff == 1:
            step += 1
        print(step)


if __name__ == '__main__':
    resolve()
