# https://atcoder.jp/contests/abc127/submissions/14486039
# D - Integer Cards
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    query = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[1],
                   reverse=True)

    B = []
    for i in range(m):
        b, c = query[i]
        while b and len(B) != n:
            B.append(c)
            b -= 1
    B.sort(reverse=True)

    for i in range(len(B)):
        if A[i] < B[i]:
            A[i] = B[i]
    print(sum(A))


def resolve2():
    n, m = map(int, input().split())
    A = []
    for a in map(int, input().split()):
        A.append([1, a])

    for _ in range(m):
        b, c = map(int, input().split())
        A.append([b, c])
    A.sort(key=lambda x: x[1], reverse=True)

    num, res = 0, 0
    for a, b in A:
        if num + a <= n:
            res += a * b
            num += a
        else:
            res += (n - num) * b
            break
    print(res)


if __name__ == '__main__':
    resolve2()
