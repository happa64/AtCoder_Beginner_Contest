# https://atcoder.jp/contests/arc110/submissions/18599110?lang=ja
# C - Exoswap
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    P = list(map(int, input().split()))

    used_index = set()
    index_list = [0] * n
    for i in range(n):
        index_list[P[i] - 1] = i

    res = []
    target = 0
    while target != n:
        target_index = index_list[target]
        while target != target_index:
            left_index = target_index - 1
            if left_index in used_index:
                print(-1)
                exit()
            res.append(left_index + 1)
            used_index.add(left_index)
            left_num = P[left_index]
            P[left_index] = P[target_index]
            P[target_index] = left_num
            index_list[target] = left_index
            index_list[left_num - 1] = target_index
            target_index = index_list[target]
        target += 1

    if len(used_index) != n - 1:
        print(-1)
    else:
        print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
