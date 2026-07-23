# Brandt's fractional conjectures on dense triangle-free graphs: a resolution and an LP characterization

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21518998.svg)](https://doi.org/10.5281/zenodo.21518998)

**Status: conditional results, pending specialist review.** This repository contains a short
mathematical note and machine verification scripts concerning the four conjectures of the
final section of [Brandt, *A 4-colour problem for dense triangle-free graphs*, Discrete
Mathematics 251 (2002), 33–46], of which the central one is:

> **Conjecture 5.1 (Brandt, 2002).** If `G` is a maximal triangle-free graph with fractional
> total domination number `d_f(G) < 3`, then `A(G)x = 1` has a rational solution `x ≥ 0`.

## Background: where this sits

Triangle-free graphs with minimum degree above `n/3` are the classical subject of a line of
work running from Erdős–Simonovits (1972) and Andrásfai–Erdős–Sós through Häggkvist,
Chen–Jin–Koh, and Jin, culminating in the Brandt–Thomassé theorem that all such graphs are
4-colourable, and in the structure theory behind it: every *maximal* triangle-free graph in
this density range is a blow-up of one of two explicit families, the Andrásfai and Vega
graphs. Łuczak, Polcyn, and Reiher's 2024 preprint *Strong Brandt–Thomassé Theorems*
(arXiv:2406.10745) sharpens this structure theorem, replacing the density hypothesis by a
first-order condition `D₄` about common neighbours of vertex sequences.

Brandt's 2002 paper closed with a section proposing a *fractional* view of this landscape:
that the right threshold is not the vertex-degree ratio but the value of a linear program —
the fractional total domination number `d_f` — and that the LP threshold `d_f < 3` should
govern when such a graph is **regularizable** (can be turned into a regular graph by
duplicating vertices, equivalently: `Ax = 1` is solvable). He formulated this as four
interlocking conjectures (4.1, 5.1, 5.2, 5.3). The structural side of the program advanced
over two decades; the fractional side appears to have remained where he left it. Conjecture
4.1 is recorded, in a slightly loosened form, on D. B. West's open problems archive.

This note closes the fractional side, in two parts.

## The two claims

> **Claim 1 (resolution from known ingredients).** Conjecture 5.1 — together with
> Conjectures 4.1, 5.2, and 5.3 — follows from the Brandt–Thomassé structure theorem plus
> equality weights on Andrásfai/Vega graphs that go back to Brandt–Pisanski (1998) and
> Brandt–Thomassé themselves (recorded in
> [Łuczak–Polcyn–Reiher 2021](https://arxiv.org/abs/2002.01498), Fact 4.2), via a short
> rational blow-up argument. The deduction appears never to have been stated, but every
> ingredient was available; no priority is claimed for them.

> **Claim 2 (exact characterization; the sharper contribution).** Conditional on Theorem 1.2
> of [Łuczak–Polcyn–Reiher 2024](https://arxiv.org/abs/2406.10745), for maximal
> triangle-free graphs:
>
> ```
> d_f(G) < 3  ⟺  G satisfies D₄  ⟺  G is a (nonempty) blow-up of an Andrásfai or Vega graph
> ```
>
> with the equality solution always strictly positive.

## Why this is of interest

**It completes a stated program.** Brandt's fractional section was not a list of stray
questions but a proposed alternative route to the 4-colour theorem for dense triangle-free
graphs, with Conjecture 5.1 as its keystone and 4.1/5.2/5.3 as its consequences. The
4-colour theorem itself was eventually proved structurally; the fractional program was left
open. Under the stated conditional inputs, all four conjectures now hold, the strict
threshold `d_f < 3` is shown to be exact, and the program can be marked closed rather than
abandoned.

**One class, three formalisms.** Claim 2 says that a single class of graphs is
simultaneously: the strict side of a *polyhedral* threshold (`d_f < 3`), the models of a
*first-order sentence* (`D₄`), and an explicitly described *structural* family
(Andrásfai/Vega blow-ups). Łuczak–Polcyn–Reiher already found the coincidence of the last
two "somewhat surprising"; the LP leg is new, and it is the leg Brandt predicted in 2002.
Characterizations of one class from unrelated formalisms are how such classes become robust
mathematical objects rather than artifacts of one proof.

**An efficient membership test for a structural class.** Deciding from the definitions
whether a graph is an Andrásfai/Vega blow-up, or whether it satisfies `D₄`, is not obviously
tractable. `d_f`, by contrast, is a single polynomial-size linear program — Brandt himself
emphasized this computability. Conditionally, membership in the Brandt–Thomassé structure
class is therefore decidable by solving one LP and comparing the optimum with 3.

**The `d_f` spectrum below 3 is discrete.** An immediate consequence of Claim 2 and the
computed values (Corollary in the note): on maximal triangle-free graphs, `d_f` takes *no*
value below 3 other than
```
3 − 1/k,   k = 1, 2, 3, …
```
(the Andrásfai graphs `Γ_k` attain every such value; the Vega values `3 − 1/(9i−6−μ−ν)`
form a subset). The set is discrete with sole accumulation point 3 — everything else below
3 is forbidden. The threshold value 3 itself is attained and is genuinely different: the
9-vertex graph below has `d_f = 3` and is *not* regularizable.

**A correction to the public record.** The variant of Conjecture 4.1 recorded on West's
open problems page uses the non-strict bound `δ(G) ≥ n/3`. The 9-vertex sharpness example
(graph6 `H?q`qjo`: `δ = n/3` exactly, every solution of `Ax = 1` has a forced zero
coordinate) refutes that variant at the boundary, while leaving Brandt's strict original
untouched. The strict inequalities in Brandt's formulations are not caution — they are the
truth.

## The two arguments, in outline

**Claim 1 (short route, uses only the ordinary Brandt–Thomassé theorem):** given
`d_f(G) < 3`, perturb the witness to a strictly positive rational `p` with `Ap ≥ 1`,
`1ᵀp < 3`; scale to integers `m = Lp` and blow `G` up into `H` with class sizes `m_v`. Then
`|V(H)| < 3L` and `δ(H) ≥ L`, so `δ(H) > |V(H)|/3`, and the structure theorem makes `H` an
Andrásfai/Vega blow-up. Those base graphs carry the known positive equality weights, so `H`
has a positive solution of `Ax = 1` — and summing it over the blow-up classes lands a
positive solution on `G`. □

**Claim 2 (equivalence, uses the strong 2024 theorem):**
1. If `G` fails property `D₄`, the failing vertex sequence, scaled by `1/m`, is a feasible
   dual vector of objective exactly 3 for the fractional total domination LP; weak duality
   gives `d_f(G) ≥ 3`. So `d_f(G) < 3` forces `D₄` — this half-page duality step appears to
   be new.
2. By LPR 2024 Theorem 1.2, `G` is then a blow-up of an Andrásfai `Γ_i` or Vega `Υ_i^{μν}`.
3. `Γ_i` is `i`-regular, so `x = (1/i)·1` works; each Vega variant carries the known weights
   `w` with `Aw = D·1`, `D = 9i−6−μ−ν` (restated and machine-verified here).
4. `d_f` and positive equality feasibility are blow-up invariants. All three conditions
   coincide. □

## Verify it yourself (≈15 seconds, no dependencies)

```
python3 verify/vega_weights.py     # Vega weight identities, all 4 variants, i = 2..8
python3 verify/boundary9.py        # the 9-vertex sharpness example, end to end
```

Both scripts are pure Python standard library, print PASS lines for every check, and exit
nonzero on any failure. The duality lemma requires no computation — it is five lines of
arithmetic reproduced in the note.

## Repository layout

```
note/brandt51.tex, .pdf   the manuscript
verify/                   machine verification scripts + expected outputs
CITATION.cff              citation metadata
```

## What is new here, and what was already known

- **Already known:** the Vega equality weights (Brandt–Thomassé's manuscript;
  regular-blow-up fact due to Brandt–Pisanski 1998; both published in LPR 2021, Fact 4.2
  with the same table), and the Brandt–Thomassé structure theorem itself.
- **Apparently new:** the LP-duality lemma (`D₄` failure ⇒ dual certificate of value 3), the
  three-way equivalence and its consequences above, the explicit observation that Brandt's
  Conjectures 4.1/5.1/5.2/5.3 follow from the literature, the 9-vertex boundary example,
  and the boundary correction to the West-page variant. Neither LPR paper mentions
  fractional domination, LP duality, or Brandt's conjectures (checked against both full
  texts).

## Honest caveats

- **Every route here is conditional on unrefereed structural inputs:** Claim 1 on the
  Brandt–Thomassé structure theorem (unpublished manuscript, also implied by the 2024
  preprint), Claim 2 on arXiv:2406.10745 (2024, unrefereed).
- No priority claim is made; an earlier version of this note presented the Vega weights as
  new, which was incorrect and is corrected in this version (see release notes for v1.1).
- Provenance: the mathematics in the note was produced with substantial AI assistance —
  research sessions run with OpenAI's GPT 5.6 Sol Pro, directed by the author, with
  independent verification and review by Anthropic's Claude Fable 5 — after which every
  step was checked: the duality lemma by hand, the Vega weight identities and the boundary
  example by machine (the scripts in `verify/`), and the LPR statements against the posted
  PDFs. A further independent AI-assisted review identified the prior appearance of the
  Vega weights and supplied the short route of Claim 1. The author takes full
  responsibility for the content.

## References

- S. Brandt, *A 4-colour problem for dense triangle-free graphs*, Discrete Mathematics 251
  (2002), 33–46. DOI: 10.1016/S0012-365X(01)00340-5. (Conjectures 4.1, 5.1, 5.2, 5.3.)
- S. Brandt, T. Pisanski, *Another infinite sequence of dense triangle-free graphs*,
  Electron. J. Combin. 5 (1998), R43.
- S. Brandt, S. Thomassé, *Dense triangle-free graphs are four-colorable: a solution to the
  Erdős–Simonovits problem*, unpublished manuscript.
- T. Łuczak, J. Polcyn, C. Reiher, *Andrásfai and Vega graphs in Ramsey–Turán theory*,
  J. Graph Theory (2021). DOI: 10.1002/jgt.22682; arXiv:2002.01498.
- T. Łuczak, J. Polcyn, C. Reiher, *Strong Brandt–Thomassé Theorems*, arXiv:2406.10745
  (2024).
- D. B. West, *Regular supergraphs of maximal triangle-free graphs*, open problem page:
  https://dwest.web.illinois.edu/openp/regsup.html
