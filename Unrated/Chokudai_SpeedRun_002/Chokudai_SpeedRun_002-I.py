import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]
    lose = set()
    for i in range(n):
        if i not in lose:
            for j in range(n):
                if i == j:
                    continue
                ai, bi = AB[i]
                aj, bj, = AB[j]
                if (ai + bj - 1) // bj == (aj + bi - 1) // bi:
                    lose.add(i)
                    lose.add(j)
                elif (ai + bj - 1) // bj > (aj + bi - 1) // bi:
                    lose.add(j)
                else:
                    lose.add(i)
    for i in range(n):
        if i not in lose:
            print(i + 1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
