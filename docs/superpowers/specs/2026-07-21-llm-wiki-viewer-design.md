# Karpathy-Style LLM Wiki Viewer — Design Spec

**Date**: 2026-07-21
**Status**: Approved
**Goal**: Refactor `index.html` from a static network viewer into a Karpathy-inspired LLM Wiki visualization frontend.

---

## 1. Why this redesign

The current viewer is a read-only network diagram. Karpathy's LLM Wiki pattern (gist 442a6bf555914893e9891c11519de94f) treats the wiki as a **persistent, compounding artifact** — with three layers (raw / wiki / schema), three operations (Ingest / Query / Lint), and two navigation files (index.md / log.md).

We adopt the **visualization frontend** side of this pattern without adopting Obsidian. The viewer becomes the IDE; data files become the schema-driven wiki; operations surface as views.

---

## 2. Architecture

```
viewer/
├── index.html              # Single self-contained file, ~1500–2000 lines
└── SCHEMA.md               # Documents the expected data shape (optional)
```

No build step. Served via `py -m http.server 8765` from `knowledge_graph/`.

---

## 3. Eight Node Types

| Type | Emoji | Color source | Origin |
|------|-------|--------------|--------|
| `source` (paper) | 📄 | category color | papers.json |
| `concept` | 💡 | concept-group color | concepts.json |
| `category` | 📂 | category color | categories.json |
| `entity` (person) | 👤 | #9013FE (purple) | derived from papers.authors |
| `overview` (review doc) | 📋 | #50E3C2 (teal) | paper_research_summaries.md |
| `synthesis` | 🔬 | #D0021B (red) | derived from synthesis sections |
| `log_entry` | 📅 | #BDBDBD (gray) | static demo entries |
| `edge_type` | 🔗 | edge-color | relationship metadata |

---

## 4. Six Views

### V1: Catalog (default entry, mirrors Karpathy's index.md)

- **Left rail**: 10 categories as collapsible tree
- **Center**: per-category list, each row = one node with:
  - type emoji + title (or year+title for papers)
  - one-line summary (from paper_research_summaries.md when available)
  - metadata badges: cited_count, concept count, has_pdf
- **Right rail**: selected node's wiki card

### V2: Graph (core visualization)

- Nodes: type-styled (icon + color + shape variant)
- Edges: 4 relation types
  - `covers_concept` (paper → concept, gray)
  - `in_category` (paper → category, category color)
  - `authored_by` (paper → person, light purple)
  - `cocited_with` (paper ↔ paper, dark gray)
- Layout: force-directed, type clusters stay grouped

### V3: Timeline

- Year-stratified (1975 → 2026)
- Cocitation edges overlaid
- Year strata as ghost nodes

### V4: Wiki (full-page detail)

- YAML-style frontmatter block
- Title + type badge
- Summary paragraph
- `[[wikilinks]]` list (clickable)
- Sources block (PDF link, cited_in locations)
- Related nodes (bidirectional references)

### V5: Lint (health report)

Six client-side computed rules:

1. **Orphan nodes** (in-degree = 0)
2. **Low quality** (`has_pdf=false` AND `cited_count == 0`)
3. **Potential duplicates** (similar titles, same first author + similar year)
4. **Stale warning** (>5 years since publication AND not cited)
5. **High-value candidates** (frequently cited concept without dedicated entity node, or vice versa)
6. **Concept-paper imbalance** (single concept covered by >10 or <2 papers)

Each warning → clickable → jumps to node.

### V6: Query (full-text search)

- Search box: title / author / concept / venue
- Live highlight (yellow pulse on match)
- Top-10 hit cards on the right (ranked by field match count)
- One-click "fly to" → network.fit + select

---

## 5. Data Flow

```
DOMContentLoaded
  → fetch 5 files (papers.json, concepts.json, categories.json,
                   edges_cocitation.csv, citations_in_thesis.csv)
  → parse + index → App.state
  → render Catalog (default)
  → user actions:
       switch view       → renderView(viewId)
       click node        → renderWiki(nodeId)
       search            → highlight + ranking
       open Lint         → compute + render report
```

---

## 6. Technical Choices

- **vis-network 9.1.9** from CDN (already in use)
- **CSS variables** for theme tokens
- **Single App.state object** for central state
- **Module pattern (IIFE)** inside `<script>` to avoid globals
- **No external libraries** beyond vis-network

---

## 7. Out of Scope (YAGNI)

- ❌ Node editing (read-only)
- ❌ Backend API
- ❌ LLM calls
- ❌ Multi-user / login
- ❌ Inline PDF rendering
- ❌ Layout algorithm switcher
- ❌ Author disambiguation (treat `"Kamenica, E."` ≠ `"Kamenica, Emir"`)
- ❌ i18n (Chinese UI + English data labels only)

---

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Single file > 200KB | IIFE modules, `<style>` block kept tidy |
| vis-network shape variety insufficient | Combine emoji prefix + color + size for type distinction |
| Lint false positives | Mark warnings, allow per-item "ignore" stored in localStorage |
| Users miss Catalog default | Onboarding tooltip on first load |

---

## 9. Deliverables

1. `defense_project/reference_materials/knowledge_graph/index.html` — rewritten viewer
2. Updated `README_RUN.md` if anything changes about launch
3. Git commit + push