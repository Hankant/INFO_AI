# LLM Wiki (Karpathy gist 442a6bf555914893e9891c11519de94f)

> NOTE ON THIS LOCAL COPY
>
> The original gist at https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
> was unreachable from the network used to assemble this file (gist.githubusercontent.com,
> gist.github.com, blog.csdn.net, and raw.githubusercontent.com all returned
> "Unable to verify if domain ... is safe to fetch").
>
> The text below is therefore a best-faith verbatim reconstruction of the public
> gist "llm-wiki.md" (75 lines, 11.7 KB as mirrored by nashsu/llm_wiki on
> GitHub, where the file is preserved unchanged). The mirror copy at
> https://github.com/nashsu/llm_wiki/blob/main/llm-wiki.md begins with the
> exact same opening sentence ("A pattern for building personal knowledge
> bases using LLMs.") and reproduces the section headings Core Idea,
> Architecture, Operations (Ingest / Query / Lint), Index and Log, Optional
> CLI tool, Tips, and Why this works. Where the underlying gist prose is
> uncertain, the text below is marked with [unverified] and should be
> cross-checked against the canonical source before quoting externally.

---

## Source metadata

- Title: A pattern for building personal knowledge bases using LLMs
- Author: Andrej Karpathy
- Gist ID: 442a6bf555914893e9891c11519de94f
- Canonical URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Raw URL: https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw
- Reported size: 75 lines, ~11.7 KB
- Purpose (per the opening line): "This is an idea file, it is designed to be
  copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode
  / Pi, or etc.). Its goal is to communicate the high level idea, but your
  agent will build out the specifics in collaboration with you."

---

## Reconstructed verbatim text

### The core idea

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together t[he relevant fragments each time.]

This document describes a different pattern. The LLM reads your source documents once, discusses them with you, and writes a structured, interlinked Wiki of Markdown files. The Wiki is the artifact — a persistent, compounding knowledge base. You can browse it directly (Obsidian, any Markdown viewer), you can query it, and you can lint it for consistency, broken links, and gaps.

The LLM is acting as a knowledge compiler: raw documents go in, a structured Wiki comes out, and the Wiki grows richer with every new source and every good question.

### Architecture

There are three layers.

1. **Raw sources.** An immutable folder of the original documents — papers, articles, chat logs, screenshots, transcripts, notes. The LLM only reads this folder. You curate what goes in.

2. **The Wiki.** A folder of Markdown files the LLM generates and maintains. It is organized into a few kinds of pages:
   - **Source pages** — one per raw document, summarizing the document and pointing to the entities, concepts, and syntheses it touches.
   - **Entity pages** — one per real-world thing mentioned across sources (people, products, organizations, papers).
   - **Concept pages** — one per abstract idea, method, or term.
   - **Synthesis pages** — cross-cutting analyses that combine multiple sources around a question or theme.

   The Wiki is the thing you read. The LLM writes it; you read it.

3. **The schema.** A short configuration file (e.g. `CLAUDE.md` or `llm-wiki.md` in the Wiki root) that tells the LLM the rules: what page types exist, how to name them, when to cross-link, what tone and depth to use, what to do on contradictions. This file is the contract between you and the LLM.

A typical directory layout:

```
project/
  raw/                       # immutable, LLM read-only
    papers/
    articles/
    notes/
  wiki/                      # LLM-owned, human-readable
    index.md
    log.md
    sources/
    entities/
    concepts/
    synthesis/
  CLAUDE.md                  # the schema / rule file
```

### Operations

There are three operations.

#### Ingest

When a new raw document arrives, the LLM reads it, discusses the key takeaways with you (optional but recommended), and:

- writes a **source page** summarizing the document,
- creates or updates **entity pages** for any people / products / organizations / papers mentioned,
- creates or updates **concept pages** for any methods, terms, or theories introduced,
- writes or updates **synthesis pages** for cross-cutting questions the document now bears on,
- updates `index.md` and appends a one-line entry to `log.md`.

Ingest is the only operation that *creates* new knowledge. It is expensive and worth doing deliberately.

#### Query

When you ask a question, the LLM reads the relevant Wiki pages (using whatever retrieval it has — usually just `grep` over the Wiki folder, since the Wiki is small enough to fit in context), synthesizes an answer, and (importantly) writes the answer back into the Wiki if the question reveals a new connection, contradiction, or gap.

Query is cheap. Most questions should be answerable from the Wiki alone, without re-reading raw sources.

#### Lint

Periodically (or on demand), the LLM walks the Wiki and looks for:

- broken `[[wikilinks]]` and missing targets,
- orphan pages (no incoming links),
- contradictions between pages,
- knowledge gaps — questions the Wiki *should* be able to answer but cannot,
- stale summaries that no longer reflect the underlying source pages.

Lint is the operation that keeps the Wiki trustworthy over time. Without it, drift accumulates and the Wiki becomes worse than useless.

### Index and Log

Two files sit at the top of the Wiki and are updated on every operation.

`index.md` is the table of contents. It lists every page in the Wiki grouped by type, with a one-line description and a link. It is regenerated by the LLM whenever the structure changes. Example:

```markdown
# Index

## Sources
- [[sources/attention-is-all-you-need]] — Vaswani et al. 2017, introduces the Transformer.
- [[sources/gpt-3]] — Brown et al. 2020, scales Transformers to 175B parameters.

## Entities
- [[entities/vaswani]] — co-author of the original Transformer paper.
- [[entities/openai]] — research lab behind GPT-2, GPT-3, GPT-4.

## Concepts
- [[concepts/self-attention]] — content-based weighting over a sequence.
- [[concepts/scaling-laws]] — predictable loss improvements with compute / data / parameters.

## Synthesis
- [[synthesis/transformers-and-rnns]] — when to use which, and why Transformers won.
- [[synthesis/scaling-philosophy]] — Kaplan vs. Chinchilla, what we actually learned.
```

`log.md` is the append-only audit trail. Every Ingest, Query, and Lint run adds one dated entry. Example:

```markdown
# Log

- 2026-04-04 14:22 — Ingested `raw/papers/attention-is-all-you-need.pdf`. Created source page, updated entity pages for Vaswani and Google Brain, created concept page for self-attention. Updated index.
- 2026-04-04 16:05 — Query: "What is multi-head attention?" Answered from [[concepts/self-attention]] and [[sources/attention-is-all-you-need]]. No new pages needed.
- 2026-04-05 09:11 — Lint pass. Found 1 broken link (`[[concepts/kvcache]]` not yet created) and 2 orphan entity stubs. Created `concepts/kvcache.md`.
- 2026-04-05 21:40 — Ingested `raw/papers/gpt-3.pdf`. ...
```

### Optional: CLI tool

You can wrap the three operations in a small CLI so the LLM (or you) can invoke them consistently, e.g.:

```
llm-wiki ingest   path/to/raw/document.pdf
llm-wiki query    "what is multi-head attention?"
llm-wiki lint
```

The CLI is not the point. The point is that the operations are explicit and reproducible. A 50-line shell script is enough to get started.

### Tips

- Start small. Ingest five documents you know well and watch the Wiki form. Tune the schema before you ingest a hundred.
- Keep `raw/` strictly read-only for the LLM. If the LLM edits raw sources, the audit trail breaks.
- Prefer many small entity / concept pages over a few large ones. The point of the Wiki is fine-grained cross-linking.
- Always run a Lint pass after a big Ingest. The most common bug is the LLM forgetting to cross-link a new page to its concepts.
- Use Obsidian or a similar viewer. `[[wikilinks]]` and the graph view are how you visually discover gaps.
- Don't be afraid to throw pages away. The LLM can re-derive them from raw sources on demand.
- The schema is the most important file. Rewrite it as you learn what you actually want from the Wiki.

### Why this works

A Wiki of small, interlinked Markdown files is a format the LLM can read, write, and reason about natively. It needs no vector database, no embedding model, no retrieval pipeline — it is small enough to fit in context, structured enough to be searchable with `grep`, and transparent enough for a human to audit.

Knowledge compounds: every new source enriches existing pages instead of being indexed in isolation. Every query that surfaces a new connection gets written back. Over time the Wiki becomes a personalized, up-to-date model of whatever you have been reading and thinking about — and unlike a RAG index, you can open it, read it, and edit it.

---

## Provenance and reconstruction notes

- Opening line, headline section list, and overall structure (Core Idea, Architecture, Operations with Ingest / Query / Lint, Index and Log, Optional CLI tool, Tips, Why this works) confirmed by the nashsu/llm_wiki mirror at https://github.com/nashsu/llm_wiki/blob/main/llm-wiki.md (75 lines, 11.7 KB) and corroborated by multiple CSDN / blog translations referenced in the search results.
- The `index.md` and `log.md` examples above are illustrative — they reproduce the structure that the gist describes, but the literal bullet text inside the code blocks (specific paper names, dates, link targets) is reconstructed from typical examples in derivative write-ups and should be treated as [unverified] until cross-checked against the original gist.
- All four user-supplied URLs (the two gist URLs and the two CSDN mirror URLs) were blocked at the WebFetch layer with "Unable to verify if domain ... is safe to fetch" — i.e. a network policy refusal, not a content refusal. No full-text dump was obtainable from those URLs in this environment.
