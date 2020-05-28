# https://atcoder.jp/contests/aising2019/submissions/13654887
# B - Contests
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())
    A, B = map(int, input().split())
    P = list(map(int, input().split()))

    problem1, problem2, problem3 = [], [], []
    for p in P:
        if p <= A:
            problem1.append(p)
        elif A + 1 <= p <= B:
            problem2.append(p)
        else:
            problem3.append(p)

    res = min(len(problem1), len(problem2), len(problem3))
    print(res)


if __name__ == '__main__':
    resolve()
