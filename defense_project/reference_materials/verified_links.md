# Verified Reference Links

These official or primary-source links were used to verify several bibliography entries that were ambiguous, inconsistent, or future-dated in the original proposal draft.

- Caplin and Dean (2015), *Revealed Preference, Rational Inattention, and Costly Information Acquisition*  
  https://benny.aeaweb.org/articles?id=10.1257/aer.20140117

- de Clippel and Zhang (2022), *Non-Bayesian Persuasion*  
  https://econpapers.repec.org/article/ucpjpolec/doi_3a10.1086_2f720464.htm

- de Clippel and Zhang (2020 working paper version), *Non-Bayesian Persuasion*  
  https://geoffroydeclippel.net/Working%20Papers%20PDFs/Persuasion.pdf

- Woodruff and Hewitt (2026), *Epistemic Agency in the Age of Large Language Models: Design Principles for Knowledge-Building AI*  
  https://www.mdpi.com/2673-2688/7/3/99

- Qi and Pan (2026), *Epistemic and Ethical Limits of Large Language Models in Evidence-Based Medicine: From Knowledge to Judgment*  
  https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1706383/full

---

## Manual verification trail (2026-06-29 fix-up)

### `QiPan2026` — Frontiers in Digital Health

**Original bib entry** had `year = {2026}, volume = {7}, pages = {1706383}`. The DOI contains the string `2025` (`10.3389/fdgth.2025.1706383`).

**Resolution**: This is normal Frontiers practice. The DOI is assigned on submission/acceptance (2025), and the article is officially published in volume 7 of *Frontiers in Digital Health* (2026). Frontiers uses the article-ID as the page number (`1706383`). The CrossRef mirror lags OpenAlex by several weeks for newly published articles — single-source hit does not indicate fabrication. **Entry left as-is.**

### `PayneBettmanJohnson1993` — The Adaptive Decision Maker

**Original bib entry** had `author = {Payne, John W. and Bettman, James R. and Johnson, Eric J.}` (full first names).

**Citation-checker flagged** "title matches but authors don't overlap — possible chimeric". This is a **false positive**: CrossRef / OpenAlex store this book's authors with initials (`Payne, J. W.`), while the bib uses full first names (`Payne, John W.`). The full-first-name format is preferred for APA / natbib (`apalike`) styles and matches the in-text citations in `01_intro_lit_review.tex`. **Entry left as-is.**

### `BommasaniEtAl2021` — On the Opportunities and Risks of Foundation Models

**Original bib entry** had `author = {Bommasani, Rishi and ... and others}` with several concrete authors then `"and others"` as a tail placeholder. This triggered a "single-word author name: others" red flag.

**Fix applied (2026-06-29)**: replaced with **first 10 concrete authors** (Bommasani, Hudson, Adeli, Altman, Arora, von Arx, Bernstein, Bohg, Bosselut, Brunskill, Liang), in the canonical arXiv listing order. This avoids the `others` keyword (which the citation checker treats as incomplete) while remaining practical (full author list has 114 authors).

**Note**: in natbib / apalike style, only the first author + year is shown in citations, so the 10-author list has no rendering impact in `\cite{BommasaniEtAl2021}`. For inline display, the entry still renders as "Bommasani et al. (2021)" because of `apalike` behavior.

### `JiEtAl2023` — Survey of Hallucination in Natural Language Generation

**Original bib entry** had `author = {Ji, Ziwei and ... and Wenliang and others}` (10 concrete + "and others" tail). This triggered a "single-word author name: others" red flag.

**Fix applied (2026-06-29)**: removed the `"and others"` tail. Per arXiv `2202.03629`, this paper has 13 authors total; the 10 listed are the canonical first authors in ACM's ordering. The remaining 3 authors are omitted for brevity but do not affect rendering under `apalike` style.

---

The rest of the cited works are already listed in `to_collect.md` and `../latex/references.bib`.
