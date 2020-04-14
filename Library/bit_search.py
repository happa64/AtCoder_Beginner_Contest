# bit全探索
for i in range(2 ** n):
    for j in range(n):
        if (i >> j) & 1:
    # ここで何らかの処理


# itertools.productを使う場合
from itertools import product

for pattern in product([0, 1], repeat=n):
    for p in pattern:
        if p == 1:
            # ここで何らかの処理