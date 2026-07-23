# Verification scripts

Both scripts are pure Python 3 standard library — no installs, no dependencies.
Each prints a PASS line per check and exits 0 on success, nonzero on any failure.
Total runtime: a few seconds.

## `vega_weights.py`

Verifies the core new computation of the note (Theorem on Vega weights): for every
`i = 2..8` and all four Vega variants `(mu, nu)`, it rebuilds the Vega graph from scratch
following the Łuczak–Polcyn–Reiher construction and checks that the closed-form weight
vector `w` satisfies `A w = D·1` and `sum(w) = 3D − 1` with `D = 9i − 6 − mu − nu`, that
all weights are positive integers, and that each constructed graph is maximal
triangle-free. These identities are affine in `i`; the range `2..8` exercises every
residue behaviour of the circulant construction.

```
$ python3 vega_weights.py
PASS  i=2 (mu,nu)=(0,0)  |V|=13  D=12  Aw=D*1:True  sum(w)=3D-1:True  ...
...   (28 lines)
ALL CHECKS PASSED
```

## `boundary9.py`

Verifies the sharpness example end to end from its graph6 string `H?q`qjo`: maximal
triangle-freeness, degrees `(3^8, 4)`, the exact primal and dual certificates giving
`d_f = 3`, the nonnegative equality family, and the vector `r` with `Aᵀr = e_8`,
`1ᵀr = 0` that forces `x_8 = 0` in every solution of `Ax = 1` — hence no strictly
positive solution and no regular vertex-multiplication.

```
$ python3 boundary9.py
graph6 H?q`qjo: n=9 degrees=[3, 3, 3, 3, 3, 3, 3, 3, 4]
PASS ...
ALL CHECKS PASSED
```

## What is *not* machine-checked here

The duality lemma (failure of D₄ ⇒ dual certificate of value 3) is five lines of
arithmetic in the note and needs no code. The classification theorem (LPR Theorem 1.2)
is the note's declared conditional input — it is not re-proved or re-checked here.
