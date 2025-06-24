def tsp_held_karp(matriz):
    from itertools import combinations

    n = len(matriz)
    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = (matriz[0][k], [0, k])

    for s in range(2, n):
        for subset in combinations(range(1, n), s):
            bits = sum(1 << k for k in subset)
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k: continue
                    res.append((C[(prev, m)][0] + matriz[m][k], C[(prev, m)][1] + [k]))
                C[(bits, k)] = min(res)

    bits = (2 ** n - 1) - 1
    res = [(C[(bits, k)][0] + matriz[k][0], C[(bits, k)][1] + [0]) for k in range(1, n)]
    return min(res, key=lambda x: x[0])
