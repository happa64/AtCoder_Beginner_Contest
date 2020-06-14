import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())
    dist = abs(a - b)
    sokudo = v - w
    if sokudo <= 0:
        print("NO")
    else:
        T = dist / sokudo
        print("YES" if T <= t else "NO")


if __name__ == '__main__':
    resolve()
