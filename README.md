# Brandt's Conjecture 5.1, resolved via the Strong Brandt–Thomassé theorem

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21518998.svg)](https://doi.org/10.5281/zenodo.21518998)

**Status: conditional result, pending specialist review.** This repository contains a short
mathematical note and machine verification scripts for the following claim:

> **Theorem (conditional).** Brandt's Conjecture 5.1 [Brandt, *Discrete Mathematics* 251 (2002),
> 33–46] is true, conditional on Theorem 1.2 of Łuczak–Polcyn–Reiher,
> *Strong Brandt–Thomassé Theorems*, [arXiv:2406.10745](https://arxiv.org/abs/2406.10745).

Brandt's conjecture (2002, open since): if a maximal triangle-free graph `G` has fractional
total domination number `d_f(G) < 3`, then `A(G)x = 1` has a nonnegative rational solution.
The note proves the stronger conclusion that a **strictly positive** rational solution exists
(extending an observation Brandt made for twin-free graphs), and establishes the equivalence,
for maximal triangle-free graphs:

```
d_f(G) < 3   ⟺   G satisfies D₄   ⟺   G is a (nonempty) blow-up of an Andrásfai or Vega graph
```

## The proof in ten lines

1. If `G` fails property D₄ (Łuczak–Polcyn–Reiher, Definition 1.1), the failing vertex sequence,
   scaled by `1/m`, is a feasible dual vector of objective exactly 3 for the fractional total
   domination LP. Weak duality gives `d_f(G) ≥ 3`.
2. Contrapositive: `d_f(G) < 3` forces D₄. By LPR Theorem 1.2 (the conditional input),
   `G` is then a blow-up of an Andrásfai graph `Γ_i` or a Vega graph `Υ_i^{μν}`.
3. `Γ_i` is `i`-regular on `3i−1` vertices, so `x = (1/i)·1` solves `Ax = 1` with `x > 0`.
4. For each Vega variant we give explicit closed-form positive integer weights `w` with
   `Aw = D·1` and `1ᵀw = 3D−1`, where `D = 9i−6−μ−ν`; so `x = w/D > 0` solves `Ax = 1`.
5. `d_f` and positive equality feasibility are invariant under nonempty blow-ups
   (class-sum / uniform-lift argument). Chain complete.
6. Sharpness: a 9-vertex maximal triangle-free graph with `d_f = 3` exactly admits nonnegative
   but **no positive** equality solution — the strict inequality in the conjecture is necessary
   (and the non-strict variant recorded on D. West's open problems page fails at the boundary).

## Verify it yourself (≈15 seconds, no dependencies)

```
python3 verify/vega_weights.py     # checks the Vega weight identities, all 4 variants, i = 2..8
python3 verify/boundary9.py        # checks the 9-vertex sharpness example end to end
```

Both scripts are pure Python standard library, print `PASS` lines for every check, and exit
nonzero on any failure. The duality lemma (step 1) requires no computation — it is five lines
of arithmetic reproduced in the note.

## Repository layout

```
note/brandt51.tex     the manuscript (LaTeX)
verify/               machine verification scripts + expected outputs
CITATION.cff          citation metadata
```

## Honest caveats

- The result is **conditional** on arXiv:2406.10745, which is (as of this writing) an
  unrefereed preprint by leading authors in the area.
- Novelty status is "apparently unnoticed in the searches performed; specialist review
  requested." The LPR paper does not mention Brandt's conjecture, fractional domination,
  or LP duality (checked against the full text), but this is not a priority proof.
- Provenance: the mathematics in the note was produced with substantial AI assistance
  (research sessions directed by the author), after which every step was independently
  verified — the duality lemma by hand, the Vega weight identities and the boundary example
  by machine (the scripts in `verify/`), and the LPR statements against the posted PDF.
  The author takes full responsibility for the content.

## References

- S. Brandt, *A 4-colour problem for dense triangle-free graphs*, Discrete Mathematics 251
  (2002), 33–46. DOI: 10.1016/S0012-365X(01)00340-5. (Conjecture 5.1.)
- T. Łuczak, J. Polcyn, C. Reiher, *Strong Brandt–Thomassé Theorems*, arXiv:2406.10745 (2024).
- D. B. West, *Regular supergraphs of maximal triangle-free graphs*, open problem page:
  https://dwest.web.illinois.edu/openp/regsup.html
