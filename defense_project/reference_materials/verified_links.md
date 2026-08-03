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

---

## Political attitudes, deliberation, and LLM persuasion (verified 2026-07-29)

- `FisherEtAl2025PoliticalDecision` — ACL Anthology and Crossref
  https://aclanthology.org/2025.acl-long.328/
  https://doi.org/10.18653/v1/2025.acl-long.328

- `TesslerEtAl2024CommonGround` — Science and Crossref
  https://www.science.org/doi/10.1126/science.adq2852
  https://doi.org/10.1126/science.adq2852

- `HuqClaggettShirado2025` — arXiv v2 and DataCite DOI
  https://arxiv.org/abs/2510.21984
  https://doi.org/10.48550/arXiv.2510.21984
  v1 used the title *From Social Division to Cohesion with AI Message Suggestions in Online Chat Groups*.

- `SalviEtAl2025ConversationalPersuasion` — Nature Human Behaviour and Crossref
  https://www.nature.com/articles/s41562-025-02194-6
  https://doi.org/10.1038/s41562-025-02194-6

- `LinEtAl2025PersuadingVoters` — Nature and Crossref
  https://www.nature.com/articles/s41586-025-09771-9
  https://doi.org/10.1038/s41586-025-09771-9

---

## Echo chambers, beliefs, attitudes, and opinion dynamics (verified 2026-08-01)

- `NyhanEtAl2023` — Nature, Crossref, and user-provided publisher PDF
  https://www.nature.com/articles/s41586-023-06297-w
  https://doi.org/10.1038/s41586-023-06297-w
  Local PDF SHA256: `4B27C3F6553AE06CEFA6D1E3001940AAC80BF7F706729ED999CC89BC72480FE5`

- `PerraRocha2019` — Scientific Reports, Crossref, and user-provided publisher PDF
  https://www.nature.com/articles/s41598-019-43830-2
  https://doi.org/10.1038/s41598-019-43830-2
  Local PDF SHA256: `C35C245DE2180ABEB801FDDA6D44E7A92582DA6BBD0F01FBDFB5552751EAA3CE`

## Paper 2 / EWA DOI 核验（2026-08-03）

50 个唯一 DOI 均由 DOI/Crossref/OpenAlex 元数据确认存在。逐条 DOI、题名、出版年份、本地 PDF 状态及来源 Markdown 见 [paper2_ewa/manifest.csv](./paper2_ewa/manifest.csv)。

部分 INFORMS 文献在项目旧稿中使用 online-first 年份，而 Crossref 当前使用卷期出版年份；导航卡片已逐条提示，不自动改写正文年份。
