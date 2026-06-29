# Knowledge Graph Viewer — Design Spec

**Date**: 2026-06-30
**Status**: Approved by user
**Target**: defense_project/reference_materials/knowledge_graph/

---

## 1. Purpose

Build a single-file HTML knowledge graph viewer that consumes the pre-structured knowledge graph artifacts (papers.json, concepts.json, categories.json, edges_cocitation.csv) and lets the user visually explore:

- **Concept co-occurrence network** (paper ↔ concept bipartite)
- **Category hierarchy** (category → paper)
- **Temporal evolution** (papers laid out by year, cocitation edges)

Primary user: the thesis author, used while writing the literature review / locating gaps. Off-line, single file, medium interactivity.

---

## 2. Data Sources

Already exist, do NOT regenerate:

| File | Used for |
|------|----------|
| `papers.json` | Paper nodes (68) — id, title, authors, year, venue, doi, category, concepts, has_pdf, cited_count |
| `concepts.json` | Concept nodes (184) — name, paper_count, concept_groups |
| `categories.json` | Category nodes (10) — name, description, papers list |
| `edges_cocitation.csv` | Cocitation edges (24) — between papers in same `\cite{a,b,c}` |

---

## 3. Architecture

```
knowledge_graph/
└── index.html              # Single self-contained file
    ├── <style>             # All CSS inlined
    ├── <script src="vis-network">  # From CDN (unpkg)
    ├── App module
    │   ├── loadData()      # fetch all JSON + CSV
    │   ├── buildV1()       # concept co-occurrence graph
    │   ├── buildV2()       # category hierarchy
    │   ├── buildV3()       # temporal evolution
    │   ├── renderDetail()  # right-side detail panel
    │   └── attachEvents()  # tab switching, search, filters
    └── index.html          # served via `python -m http.server 8000`
```

No build step. Open `index.html` via local HTTP server.

---

## 4. View Specifications

### View 1: Concept Co-occurrence Network

- **Nodes**:
  - 68 paper nodes — light gray background, radius proportional to `cited_count`
  - 184 concept nodes — colored by `concept_groups` first word (bayesian=blue, algorithm=orange, cognitive=green, anthropomorphism=purple, etc.)
- **Edges**:
  - Paper → Concept: all `COVERS_CONCEPT` relations
  - No paper↔paper edges (avoid density)
- **Interaction**:
  - Click concept → highlight all papers covering it, dim others
  - Click paper → show detail panel
  - Drag, zoom default

### View 2: Category Hierarchy

- **Nodes**:
  - 10 category nodes — large, colored by category_descriptions
  - 68 paper nodes — small, same color as their category
- **Edges**:
  - Category → Paper: `IN_CATEGORY` relation
- **Layout**:
  - Hierarchical, direction = UD (category on top)

### View 3: Temporal Evolution

- **Nodes**:
  - 68 paper nodes
- **Edges**:
  - Cocitation edges from edges_cocitation.csv
- **Layout**:
  - Hierarchical, direction = LR (year on horizontal axis)
  - Year used as a grouping hint, computed from paper.year

---

## 5. Detail Panel

Right sidebar, 320px wide. On node click:

**Paper detail**:
- Title, authors, year, venue, DOI (clickable → doi.org)
- Concepts (clickable tags → switch to View 1, highlight concept)
- has_pdf badge → "📄 Open PDF" button (opens `file:///` path)

**Concept detail**:
- Name, group, paper_count
- List of papers (clickable)

**Category detail**:
- Name, description
- List of papers (clickable)

---

## 6. Search & Filter

Top toolbar (60px):
- Text search (title / author / concept) — instant filter
- Category multi-select dropdown
- Year range slider (1975–2026)
- Reset button

---

## 7. Performance & Offline

- vis-network loaded from `https://unpkg.com/vis-network@9.1.9/standalone/umd/vis-network.min.js`
- All data loaded from local JSON files via `fetch()`
- Open via: `cd knowledge_graph && python -m http.server 8000`, then visit `http://localhost:8000/`
- 252 nodes total — well within vis-network's comfort zone (< 1s render)

---

## 8. Testing

**Automated checks** (manual):
- 68 paper nodes render in V1
- 184 concept nodes render in V1
- 10 category nodes render in V2
- 24 cocitation edges render in V3
- Tab switching has no JS error (open browser console)

**Visual checks** (manual):
- Network is readable (no severe overlap)
- Colors are distinguishable
- Drag/zoom smooth

---

## 9. YAGNI — Features NOT included

- ❌ Edit/annotate
- ❌ Backend API
- ❌ Multi-user
- ❌ Inline PDF rendering
- ❌ Export PNG/SVG
- ❌ Layout algorithm switcher
- ❌ Author nodes (could be added later if needed)
- ❌ Author disambiguation

---

## 10. Deliverables

1. `defense_project/reference_materials/knowledge_graph/index.html` — single viewer file
2. `defense_project/reference_materials/knowledge_graph/README_RUN.md` — how to launch