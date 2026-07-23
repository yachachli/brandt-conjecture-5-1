# Brandt's Conjecture 5.1, resolved via the Strong Brandt–Thomassé theorem

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21518998.svg)](https://doi.org/10.5281/zenodo.21518998)

**Status: conditional results, pending specialist review.** This repository contains a short
mathematical note and machine verification scripts for two claims about Brandt's
Conjecture 5.1 [Brandt, *Discrete Mathematics* 251 (2002), 33–46]: if a maximal
triangle-free graph `G` has fractional total domination number `d_f(G) < 3`, then
`A(G)x = 1` has a nonnegative rational solution.

> **Claim 1 (resolution from known ingredients).** Conjecture 5.1 — together with
> Conjectures 4.1, 5.2, and 5.3 of the same paper — follows from the Brandt–Thomassé
> structure theorem plus equality weights on Andrásfai/Vega graphs that go back to
> Brandt–Pisanski (1998) and Brandt–Thomassé themselves (recorded in
> [Łuczak–Polcyn–Reiher 2021](https://arxiv.org/abs/2002.01498), Fact 4.2), via a short
> rational blow-up argument. The deduction appears never to have been stated, but the
> ingredients were available.

> **Claim 2 (exact characterization, the sharper contribution).** Conditional on Theorem 1.2
> of [Łuczak–Polcyn–Reiher 2024](https://arxiv.org/abs/2406.10745), for maximal
> triangle-free graphs:
>
> ```
> d_f(G) < 3  ⟺  G satisfies D₄  ⟺  G is a (nonempty) blow-up of an Andrásfai or Vega graph
> ```
>
> with the solution always strictly positive — an LP characterization of a first-order
> definable structural class.

## The two arguments, in outline

**Claim 1 (short route, uses only the ordinary Brandt–Thomassé theorem):** given `d_f(G) < 3`,
perturb the witness to a strictly positive rational `p` with `Ap ≥ 1`, `1ᵀp < 3`; scale to
integers `m = Lp` and blow `G` up into `H` with class sizes `m_v`. Then `|V(H)| < 3L` and
`δ(H) ≥ L`, so `δ(H) > |V(H)|/3`, and the Brandt–Thomassé structure theorem makes `H` an
Andrásfai/Vega blow-up. Those base graphs carry the known positive equality weights
(Brandt–Pisanski / Brandt–Thomassé; LPR 2021, Fact 4.2), so `H` has a positive solution of
`Ax = 1` — and summing it over the blow-up classes lands a positive solution on `G`. □

**Claim 2 (equivalence, uses the strong 2024 theorem):**
1. If `G` fails property D₄, the failing vertex sequence, scaled by `1/m`, is a feasible dual
   vector of objective exactly 3 for the fractional total domination LP; weak duality gives
   `d_f(G) ≥ 3`. So `d_f(G) < 3` forces D₄ — this half-page duality step appears to be new.
2. By LPR 2024 Theorem 1.2, `G` is then a blow-up of an Andrásfai `Γ_i` or Vega `Υ_i^{μν}`.
3. `Γ_i` is `i`-regular, so `x = (1/i)·1` works; each Vega variant carries the known weights
   `w` with `Aw = D·1`, `D = 9i−6−μ−ν` (restated and machine-verified here).
4. `d_f` and positive equality feasibility are blow-up invariants. All three conditions
   coincide. □

**Sharpness:** a 9-vertex maximal triangle-free graph with `d_f = 3` exactly admits nonnegative
but **no positive** equality solution — the strict inequality is necessary, and the non-strict
variant recorded on D. West's open problems page fails at precisely this boundary.

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

## What is new here, and what was already known

- **Already known:** the Vega equality weights (Brandt–Thomassé's manuscript; regular-blow-up
  fact due to Brandt–Pisanski 1998; both published in LPR 2021, Fact 4.2 with the same
  table), and the Brandt–Thomassé structure theorem itself.
- **Apparently new:** the LP-duality lemma (`D₄` failure ⇒ dual certificate of value 3), the
  three-way equivalence, the explicit observation that Brandt's Conjectures 4.1/5.1/5.2/5.3
  follow from the literature, the 9-vertex boundary example, and the boundary correction to
  the West-page variant. Neither LPR paper mentions fractional domination, LP duality, or
  Brandt's conjectures (checked against both full texts).

## Honest caveats

- **Every route here is conditional on unrefereed structural inputs:** Claim 1 on the
  Brandt–Thomassé structure theorem (unpublished manuscript, also implied by the 2024
  preprint), Claim 2 on arXiv:2406.10745 (2024, unrefereed).
- No priority claim is made; an earlier version of this note presented the Vega weights as
  new, which was incorrect and is corrected in this version.
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
