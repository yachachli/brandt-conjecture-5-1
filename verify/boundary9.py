#!/usr/bin/env python3
"""Independent verification of the 9-vertex sharpness example (graph6: H?q`qjo).

Checks, with exact rational arithmetic and no dependencies:

  1. the graph decoded from its graph6 string is triangle-free, maximal triangle-free,
     with degree sequence (3,3,3,3,3,3,3,3,4), so delta = 3 = n/3;
  2. primal certificate p = (1,0,0,1,0,0,0,0,1):        A p >= 1,  1^T p = 3;
  3. dual certificate   z = (1/2)(1,0,0,1,1,1,1,1,0):   A^T z <= 1, 1^T z = 3;
     hence d_f = 3 exactly;
  4. the family x(t) = (t, 1/2-t, 1/2-t, t, 1/2, 1/2, 1/2, 1/2, 0) solves A x = 1
     with x >= 0 for t in [0, 1/2];
  5. r = (1/2)(0,1,1,0,-1,-1,-1,-1,2) satisfies A^T r = e_8 and 1^T r = 0, so EVERY
     solution of A x = 1 has x_8 = r^T A x = r^T 1 = 0: no strictly positive solution
     exists, i.e. no vertex multiplication of this graph yields a regular graph.

Exit code 0 iff all checks pass.
"""
import sys
from fractions import Fraction as F
from itertools import combinations

G6 = "H?q`qjo"


def decode_graph6(s):
    n = ord(s[0]) - 63
    bits = []
    for ch in s[1:]:
        v = ord(ch) - 63
        bits += [(v >> k) & 1 for k in range(5, -1, -1)]
    adj = [[0] * n for _ in range(n)]
    idx = 0
    for j in range(n):
        for i in range(j):
            if bits[idx]:
                adj[i][j] = adj[j][i] = 1
            idx += 1
    return n, adj


def main():
    n, adj = decode_graph6(G6)
    ok = n == 9
    deg = [sum(row) for row in adj]

    tri_free = all(not (adj[a][b] and adj[b][c] and adj[a][c])
                   for a, b, c in combinations(range(n), 3))
    maximal = all(adj[u][v] or any(adj[u][w] and adj[v][w] for w in range(n))
                  for u, v in combinations(range(n), 2))
    degs_ok = sorted(deg) == [3] * 8 + [4]
    print(f"graph6 {G6}: n={n} degrees={deg}")
    print(f"PASS triangle-free: {tri_free}" if tri_free else "FAIL triangle-free")
    print(f"PASS maximal triangle-free: {maximal}" if maximal else "FAIL maximal")
    print(f"PASS degree sequence (3^8,4), delta=3=n/3: {degs_ok}")
    ok = ok and tri_free and maximal and degs_ok

    def Av(vec):
        return [sum(F(adj[i][j]) * vec[j] for j in range(n)) for i in range(n)]

    p = [F(x) for x in (1, 0, 0, 1, 0, 0, 0, 0, 1)]
    c1 = all(v >= 1 for v in Av(p)) and sum(p) == 3
    print(f"PASS primal p: Ap>=1 and 1^Tp=3: {c1}")

    z = [F(x, 2) for x in (1, 0, 0, 1, 1, 1, 1, 1, 0)]
    c2 = all(v <= 1 for v in Av(z)) and sum(z) == 3     # A symmetric
    print(f"PASS dual z: A^Tz<=1 and 1^Tz=3 (hence d_f=3): {c2}")

    def xt(t):
        return [t, F(1, 2) - t, F(1, 2) - t, t,
                F(1, 2), F(1, 2), F(1, 2), F(1, 2), F(0)]
    c3 = all(all(v == 1 for v in Av(xt(t))) and all(u >= 0 for u in xt(t))
             for t in (F(0), F(1, 4), F(1, 2)))
    print(f"PASS equality family x(t) solves Ax=1, x>=0: {c3}")

    r = [F(x, 2) for x in (0, 1, 1, 0, -1, -1, -1, -1, 2)]
    Ar = Av(r)
    c4 = Ar == [F(0)] * 8 + [F(1)] and sum(r) == 0
    print(f"PASS r: A^Tr=e_8 and 1^Tr=0 (forces x_8=0 in every solution): {c4}")

    ok = ok and c1 and c2 and c3 and c4
    print("ALL CHECKS PASSED" if ok else "CHECKS FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
