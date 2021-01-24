# https://atcoder.jp/contests/abc189/submissions/19665225
# E - Rotate and Flip
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    xy = tuple(list(map(int, input().split())) + [1] for _ in range(n))
    m = int(input())
    op = tuple(tuple(map(int, input().split())) for _ in range(m))
    q = int(input())
    query = tuple(tuple(map(int, input().split())) for _ in range(q))

    affine = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]] for _ in range(m + 1)]
    for idx in range(m):
        if op[idx][0] == 1:
            matrix = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
        elif op[idx][0] == 2:
            matrix = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        elif op[idx][0] == 3:
            matrix = [[-1, 0, 2 * op[idx][1]], [0, 1, 0], [0, 0, 1]]
        else:
            matrix = [[1, 0, 0], [0, -1, 2 * op[idx][1]], [0, 0, 1]]
        affine[idx + 1] = [[sum([matrix[i][k] * affine[idx][k][j] for k in range(3)]) for j in range(3)] for i in range(3)]

    for a, b in query:
        res = [sum([affine[a][i][j] * xy[b - 1][j] for j in range(3)]) for i in range(3)]
        print(*res[:2])


if __name__ == '__main__':
    resolve()
