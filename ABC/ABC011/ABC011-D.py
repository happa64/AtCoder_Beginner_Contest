# https://atcoder.jp/contests/abc011/tasks/abc011_4
# https://emtubasa.hateblo.jp/entry/2018/09/04/000000を参照
# D - 大ジャンプ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, d = map(int, input().split())
    x, y = map(int, input().split())

    if x % d or y % d:
        print(0)
        exit()

    x = abs(x // d)
    y = abs(y // d)

    if x + y > n or (n - x - y) % 2 != 0:
        print(0)
        exit()

    fact = [0 for _ in range(n + 1)]
    fact[0] = 1
    for i in range(n):
        fact[i + 1] = fact[i] * (i + 1)

    res = 0
    # （移動可能回数）-（x,yに到達可能な最短回数）= （余分に移動できる回数）
    # 上下を1セット、左右を1セットとして考えると同じ位置に居座ることができ、余分に移動できるセット数は1/2（zとする）になる
    z = (n - x - y) // 2
    # 左右にi回移動すると考えると、上下にz-i回移動できる
    # また例えば右にi回移動したとすると、左にはx+i回移動する必要がある
    # また下にz-i回移動したとすると、上にはy + z - i回移動する必要がある
    # つまり、左：x+i、右：i、上：y+z-i、下：z-i回移動することになる
    for i in range(z + 1):
        l, r, u, d, = x + i, i, y + z - i, z - i
        # 同じものaがp個，bがq個，cがr個、合計n個あるとき，これらを全部使って1列に並べる順列の総数はn!/p!q!r!通りである
        res += fact[n] // fact[l] // fact[r] // fact[u] // fact[d] / pow(4, n)

    print(res)


if __name__ == '__main__':
    resolve()
