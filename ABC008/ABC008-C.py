import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(int(input()) for _ in range(n))

    res = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                if C[i] % C[j] == 0:
                    cnt += 1
        if cnt % 2 == 0:
            res += (cnt + 2) / (2 * cnt + 2)
        else:
            res += 1 / 2
    print(res)


if __name__ == '__main__':
    resolve()
