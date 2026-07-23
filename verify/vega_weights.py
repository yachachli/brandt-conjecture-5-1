#!/usr/bin/env python3
"""Independent verification of the Vega weight identities (Theorem: vega weights).

For each i in 2..8 and each variant (mu, nu) in {0,1}^2, this script constructs the
Vega graph Upsilon_i^{mu nu} from scratch (inner Andrasfai graph + external hexagon
+ outer vertices, per Luczak-Polcyn-Reiher, arXiv:2406.10745), builds the closed-form
weight vector w from the note, and checks:

  1. every constructed graph is maximal triangle-free;
  2. A w = D * 1        with D = 9i - 6 - mu - nu   (every neighbourhood sums to D);
  3. sum(w) = 3D - 1;
  4. every weight is a positive integer.

Pure standard library. Exit code 0 iff all checks pass.
Expected output: one PASS line per (i, mu, nu), then ALL CHECKS PASSED.
"""
import sys
from itertools import combinations


def vega(i, mu, nu):
    """Vertices and edges of Upsilon_i^{mu nu}."""
    n_in = 3 * i - 1
    inner = [v for v in range(n_in) if not (nu == 1 and v == 2 * i - 1)]
    ext = ['a', 'v', 'c', 'u', 'b', 'w', 'x'] + ([] if mu == 1 else ['y'])
    V = inner + ext
    E = set()

    def add(p, q):
        E.add(frozenset((p, q)))

    # inner Andrasfai edges: circulant, difference mod (3i-1) in {i, ..., 2i-1}
    for r in inner:
        for s in inner:
            if r < s and ((s - r) % n_in in range(i, 2 * i)
                          or (r - s) % n_in in range(i, 2 * i)):
                add(r, s)
    R = [v for v in inner if v < i]
    Gc = [v for v in inner if i <= v < 2 * i]
    B = [v for v in inner if v >= 2 * i]
    for h, cls in (('a', R), ('u', R), ('b', Gc), ('v', Gc), ('c', B), ('w', B)):
        for q in cls:
            add(h, q)
    for p, q in [('a', 'v'), ('v', 'c'), ('c', 'u'),
                 ('u', 'b'), ('b', 'w'), ('w', 'a')]:
        add(p, q)
    for q in ['a', 'b', 'c']:
        add('x', q)
    if mu == 0:
        add('x', 'y')
        for q in ['u', 'v', 'w']:
            add('y', q)
    return V, E


def weights(i, mu, nu):
    """The closed-form weight vector from the note."""
    w = {}
    if nu == 0:
        for v in range(3 * i - 1):
            w[v] = 3
        w[0] = 1
        w[2 * i - 1] = 1
    else:
        for v in range(3 * i - 1):
            if v != 2 * i - 1:
                w[v] = 3
        w[0] = 2
        w[i - 1] = 2
    table = {
        (0, 0): dict(a=3*i-2, v=3*i-2, c=3*i-3, u=3*i-2, b=3*i-2, w=3*i-3, x=1, y=1),
        (1, 0): dict(a=3*i-2, v=3*i-3, c=3*i-3, u=3*i-3, b=3*i-2, w=3*i-4, x=2),
        (0, 1): dict(a=3*i-2, v=3*i-3, c=3*i-3, u=3*i-2, b=3*i-3, w=3*i-3, x=1, y=1),
        (1, 1): dict(a=3*i-2, v=3*i-4, c=3*i-3, u=3*i-3, b=3*i-3, w=3*i-4, x=2),
    }
    w.update(table[(mu, nu)])
    return w


def main():
    ok = True
    for i in range(2, 9):
        for mu in (0, 1):
            for nu in (0, 1):
                V, E = vega(i, mu, nu)
                D = 9 * i - 6 - mu - nu
                w = weights(i, mu, nu)
                nbr = {v: set() for v in V}
                for e in E:
                    p, q = tuple(e)
                    nbr[p].add(q)
                    nbr[q].add(p)

                pos = set(w) == set(V) and all(
                    isinstance(w[v], int) and w[v] > 0 for v in V)
                tri = any(len(nbr[p] & nbr[q] & set(V)) > 0
                          and frozenset((p, q)) in E
                          for p, q in combinations(V, 2)
                          if frozenset((p, q)) in E
                          and (nbr[p] & nbr[q]))
                mtf = all(frozenset((p, q)) in E or (nbr[p] & nbr[q])
                          for p, q in combinations(V, 2))
                aw = all(sum(w[u] for u in nbr[v]) == D for v in V)
                tot = sum(w.values()) == 3 * D - 1

                good = pos and mtf and (not tri) and aw and tot
                ok = ok and good
                tag = "PASS" if good else "FAIL"
                print(f"{tag}  i={i} (mu,nu)=({mu},{nu})  |V|={len(V)}  D={D}  "
                      f"Aw=D*1:{aw}  sum(w)=3D-1:{tot}  MTF:{mtf}  "
                      f"triangle-free:{not tri}  w>0:{pos}")
    print("ALL CHECKS PASSED" if ok else "CHECKS FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
