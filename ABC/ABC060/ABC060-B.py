import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())

    for i in range(a, a * b + 1, a):
        if i % b == c:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
