#!/usr/bin/env python3
"""
Build the knowledge_graph/ artifacts from references.bib, .tex files, and summary docs.
Run from project root: PYTHONIOENCODING=utf-8 py -3 e:/Info_AI/export_bib.py
"""
import json
import re
import os
from pathlib import Path
from collections import defaultdict

REPO = Path(r"e:/Info_AI")
LATEX = REPO / "defense_project" / "latex"
REFS = LATEX / "references.bib"
KG = REPO / "defense_project" / "reference_materials" / "knowledge_graph"
KG.mkdir(parents=True, exist_ok=True)

# ---------- 1. Parse references.bib ----------
def parse_bib(path):
    text = path.read_text(encoding="utf-8")
    entry_pat = re.compile(r"@(\w+)\{([^,\s]+)\s*,(.*?)\n\}", re.DOTALL)
    field_pat = re.compile(r"(\w+)\s*=\s*\{([^}]*)\}|(\w+)\s*=\s*([^\s,]+)")
    entries = []
    for m in entry_pat.finditer(text):
        etype, key, body = m.group(1).lower(), m.group(2), m.group(3)
        fields = {}
        for fm in field_pat.finditer(body):
            fn = fm.group(1) or fm.group(3)
            fv = fm.group(2) or fm.group(4)
            if fn and fv:
                fields[fn.lower()] = fv.strip().strip(',').strip()
        # Clean authors for parsing
        authors_raw = fields.get("author", "")
        authors = [a.strip() for a in re.split(r"\s+and\s+", authors_raw) if a.strip()]
        entries.append({
            "key": key,
            "type": etype,
            "title": fields.get("title", ""),
            "authors": authors,
            "authors_raw": authors_raw,
            "year": fields.get("year", ""),
            "journal": fields.get("journal", ""),
            "booktitle": fields.get("booktitle", ""),
            "publisher": fields.get("publisher", ""),
            "volume": fields.get("volume", ""),
            "number": fields.get("number", ""),
            "pages": fields.get("pages", ""),
            "doi": fields.get("doi", ""),
            "eprint": fields.get("eprint", ""),
            "url": fields.get("url", ""),
            "note": fields.get("note", ""),
            "venue": fields.get("journal") or fields.get("booktitle") or fields.get("publisher") or "",
        })
    return entries

entries = parse_bib(REFS)
print(f"Parsed {len(entries)} bib entries")

# ---------- 2. Category map (from to_collect.md structure) ----------
CATEGORY_MAP = {
    # Foundational theory
    "KamenicaGentzkow2011": "foundational_theory",
    "BergemannMorris2019": "foundational_theory",
    "deClippelZhang2020": "foundational_theory",
    "deClippelZhang2022": "foundational_theory",
    # Information acquisition
    "Sims2003": "information_acquisition",
    "CaplinDean2015": "information_acquisition",
    "PayneBettmanJohnson1993": "information_acquisition",
    "EnkeZimmermann2019": "information_acquisition",
    "Nickerson1998": "information_acquisition",
    "LordRossLepper1979": "information_acquisition",
    "Edwards1965": "information_acquisition",
    # Algorithms / trust / HCI
    "ParasuramanRiley1997": "algorithms_trust_hci",
    "LeeSee2004": "algorithms_trust_hci",
    "Dietvorst2015": "algorithms_trust_hci",
    "Logg2019": "algorithms_trust_hci",
    "ReevesNass1996": "algorithms_trust_hci",
    "NassMoon2000": "algorithms_trust_hci",
    "EpleyWaytzCacioppo2007": "algorithms_trust_hci",
    "Waytz2010": "algorithms_trust_hci",
    "SundarNass2000": "algorithms_trust_hci",
    "PuringtonEtAl2017": "algorithms_trust_hci",
    "Bender2021": "algorithms_trust_hci",
    "VodrahalliEtAl2021": "algorithms_trust_hci",
    # Recommender / generative AI
    "ResnickVarian1997": "recommender_genai",
    "AdomaviciusTuzhilin2005": "recommender_genai",
    "Bozdag2013": "recommender_genai",
    "Vaswani2017": "recommender_genai",
    "Brown2020": "recommender_genai",
    "Ouyang2022": "recommender_genai",
    "BommasaniEtAl2021": "recommender_genai",
    "JiEtAl2023": "recommender_genai",
    "HicksHumphriesSlater2024": "recommender_genai",
    "Shanahan2024": "recommender_genai",
    "WingerterStraubSchweitzer2025": "recommender_genai",
    # Narrative / epistemic / medical AI
    "GreenBrock2000": "narrative_epistemic",
    "WoodruffHewitt2026": "narrative_epistemic",
    "QiPan2026": "narrative_epistemic",
    # Newly added candidates (existing)
    "AlonsoCamara2016": "newly_added_candidates",
    "BakshyMessingAdamic2015": "newly_added_candidates",
    "Benjamin2019": "newly_added_candidates",
    "CasteloBosLehmann2019": "newly_added_candidates",
    "DworczakMartini2019": "newly_added_candidates",
    "Edwards1968": "newly_added_candidates",
    "Gabaix2019": "newly_added_candidates",
    "Grether1980": "newly_added_candidates",
    "GuzmanLewis2020": "newly_added_candidates",
    "KahnemanTversky1973": "newly_added_candidates",
    "KiddBirhane2023": "newly_added_candidates",
    "Kruglanski2004": "newly_added_candidates",
    "RabinSchrag1999": "newly_added_candidates",
    # Self vs AI batch (2026-06-29)
    "YanivKleinberger2000": "advice_taking",
    "BonaccioDalal2006": "advice_taking",
    "SniezekBuckley1995": "advice_taking",
    "HarveyFischer1997": "advice_taking",
    "SollLarrick2009": "advice_taking",
    "MillerRoss1975": "self_serving_attribution",
    "Bradley1978": "self_serving_attribution",
    "Weiner1985": "self_serving_attribution",
    "CampbellSedikides1999": "self_serving_attribution",
    "MezulisEtAl2004": "self_serving_attribution",
    "ShepperdMaloneSweeny2008": "self_serving_attribution",
    "Langer1975": "overconfidence_control",
    "ThompsonArmstrongThomas1998": "overconfidence_control",
    "MooreHealy2008": "overconfidence_control",
    "LarrickBursonSoll2007": "overconfidence_control",
    "Goodie2003": "overconfidence_control",
    "PrahlVanSwol2017": "algorithm_aversion",
    "LongoniBonezziMorewedge2019": "algorithm_aversion",
}

# Concept tags (from the user-provided summaries, plus our own tags)
CONCEPT_TAGS = {
    # advice_taking
    "YanivKleinberger2000": ["advice_taking", "egocentric_discounting", "advisor_reputation", "judge_advisor_paradigm"],
    "BonaccioDalal2006": ["advice_taking", "review", "advice_utilization", "advisor_expertise"],
    "SniezekBuckley1995": ["judge_advisor_system", "cognitive_conflict", "advice_cueing", "role_differentiation"],
    "HarveyFischer1997": ["advice_taking", "judgment_improvement", "responsibility_sharing", "weight_of_advice"],
    "SollLarrick2009": ["judgment_revision", "advice_weighting", "averaging_vs_choosing", "wisdom_of_crowds"],
    # self_serving_attribution
    "MillerRoss1975": ["self_serving_bias", "attribution", "success_failure_asymmetry", "self_protection"],
    "Bradley1978": ["self_serving_attribution", "success_failure_asymmetry", "defensive_attribution"],
    "Weiner1985": ["attribution_theory", "locus_stability_controllability", "achievement_motivation"],
    "CampbellSedikides1999": ["self_threat", "self_serving_bias", "meta_analysis"],
    "MezulisEtAl2004": ["self_serving_attribution", "positivity_bias", "meta_analysis"],
    "ShepperdMaloneSweeny2008": ["self_serving_bias", "motivated_reasoning", "self_enhancement"],
    # overconfidence_control
    "Langer1975": ["illusion_of_control", "perceived_control", "choice_familiarity"],
    "ThompsonArmstrongThomas1998": ["illusion_of_control", "control_heuristic", "intentionality_connection"],
    "MooreHealy2008": ["overestimation", "overplacement", "overprecision", "overconfidence"],
    "LarrickBursonSoll2007": ["social_comparison", "better_than_average_effect", "overplacement"],
    "Goodie2003": ["control", "betting", "calibration", "decision_value"],
    # algorithm_aversion
    "PrahlVanSwol2017": ["algorithm_aversion", "advice_discounting", "perceived_similarity"],
    "LongoniBonezziMorewedge2019": ["AI_resistance", "medical_AI", "uniqueness_neglect"],
    "VodrahalliEtAl2021": ["human_AI_advice", "activation_integration_model", "AI_advice_use"],
    # AI / LLM baseline
    "Vaswani2017": ["transformer", "attention_mechanism", "self_supervised_learning"],
    "Brown2020": ["few_shot_learning", "GPT_3", "language_model", "in_context_learning"],
    "Ouyang2022": ["RLHF", "instruction_tuning", "InstructGPT"],
    "Bender2021": ["stochastic_parrots", "language_model_limits", "linguistic_form_vs_meaning"],
    "BommasaniEtAl2021": ["foundation_models", "transfer_learning", "emergence", "homogenization"],
    "JiEtAl2023": ["hallucination", "NLG_survey", "factuality"],
    "HicksHumphriesSlater2024": ["ChatGPT", "bullshit", "AI_truthfulness", "philosophy_of_AI"],
    "Shanahan2024": ["LLM_reasoning", "anthropomorphism", "LLM_dialogue"],
    # Information design
    "KamenicaGentzkow2011": ["bayesian_persuasion", "information_design", "signal_structure"],
    "BergemannMorris2019": ["information_design", "unified_framework", "posterior_beliefs"],
    "deClippelZhang2022": ["non_bayesian_persuasion", "distortion_function", "signal_design"],
    # Rational inattention
    "Sims2003": ["rational_inattention", "information_cost", "entropy"],
    "CaplinDean2015": ["rational_inattention", "costly_information_acquisition", "revealed_preference"],
    "EnkeZimmermann2019": ["correlation_neglect", "belief_formation", "subjective_beliefs"],
    # Algorithm trust baseline
    "ParasuramanRiley1997": ["automation_use_abuse", "automation_paradox", "human_factors"],
    "LeeSee2004": ["trust_in_automation", "appropriate_reliance", "trust_calibration"],
    "Dietvorst2015": ["algorithm_aversion", "algorithm_error", "forecast_algorithm"],
    "Logg2019": ["algorithm_appreciation", "algorithmic_judgment", "AI_advice"],
    # HCI / anthropomorphism
    "ReevesNass1996": ["CASA", "media_equation", "human_computer_interaction"],
    "NassMoon2000": ["mindlessness", "social_response_to_computers"],
    "EpleyWaytzCacioppo2007": ["anthropomorphism", "three_factor_theory", "mind_attribution"],
    "Waytz2010": ["anthropomorphism", "individual_differences"],
    "SundarNass2000": ["source_orientation", "HCI", "social_actor"],
    "PuringtonEtAl2017": ["Alexa", "smart_speaker", "personification", "social_roles"],
    # Recommender systems baseline
    "ResnickVarian1997": ["recommender_systems", "collaborative_filtering", "information_filtering"],
    "AdomaviciusTuzhilin2005": ["recommender_systems_survey", "next_generation_recommender"],
    "Bozdag2013": ["algorithmic_bias", "filter_bubble", "personalization_ethics"],
    # Belief updating / cognition
    "Nickerson1998": ["confirmation_bias", "belief_persistence"],
    "LordRossLepper1979": ["biased_assimilation", "attitude_polarization", "prior_beliefs"],
    "PayneBettmanJohnson1993": ["adaptive_decision_maker", "judgment_strategies", "decision_process"],
    "Edwards1965": ["information_seeking", "optimal_strategy", "urn_experiment"],
    "KahnemanTversky1973": ["prediction_psychology", "intuitive_forecast", "calibration"],
    "RabinSchrag1999": ["first_impressions", "confirmatory_bias", "belief_formation"],
    "Grether1980": ["bayes_rule_descriptive", "representativeness_heuristic"],
    "Kruglanski2004": ["cognitive_closure", "closed_mindedness", "freezing"],
    "Gabaix2019": ["behavioral_inattention", "inattention_models"],
    "Edwards1968": ["conservatism", "information_processing"],
    "Benjamin2019": ["probabilistic_reasoning_errors", "judgment_biases", "behavioral_econ_review"],
    # Narrative
    "GreenBrock2000": ["narrative_transportation", "persuasion", "narrative_belief"],
    "WoodruffHewitt2026": ["epistemic_agency", "LLM_design_principles", "knowledge_building_AI"],
    "QiPan2026": ["LLM_evidence_based_medicine", "epistemic_limits", "LLM_judgment"],
    # Persuasion extensions
    "AlonsoCamara2016": ["bayesian_persuasion", "heterogeneous_priors"],
    "DworczakMartini2019": ["optimal_persuasion", "simple_economics"],
    # Filter bubble / exposure
    "BakshyMessingAdamic2015": ["exposure_diverse_news", "facebook", "ideological_diversity"],
    "GuzmanLewis2020": ["human_machine_communication", "AI_communication_agenda"],
    "KiddBirhane2023": ["AI_distort_beliefs", "Science_commentary"],
    "CasteloBosLehmann2019": ["task_dependent_algorithm_aversion", "subjective_vs_objective_tasks"],
    # Misc
    "WingerterStraubSchweitzer2025": ["automation_bias", "AI_nudges", "cognitive_reflection"],
}

for e in entries:
    e["category"] = CATEGORY_MAP.get(e["key"], "uncategorized")
    e["concepts"] = CONCEPT_TAGS.get(e["key"], [])
    e["has_pdf"] = False  # filled in later

# ---------- 3. Detect downloaded PDFs ----------
PAPERS_DIR = REPO / "defense_project" / "reference_materials" / "papers_originals"
for pdf in PAPERS_DIR.rglob("*.pdf"):
    key = pdf.stem  # filename without .pdf = bib key by convention
    for e in entries:
        if e["key"] == key:
            e["has_pdf"] = True
            e["pdf_path"] = str(pdf.relative_to(REPO))
            e["pdf_size_kb"] = pdf.stat().st_size // 1024
            break

# ---------- 4. Parse .tex files for citation usage ----------
cite_pat = re.compile(r"\\cite[a-z]*\*?(?:\[[^\]]*\])?\{([^}]+)\}")
file_usage = defaultdict(list)  # key -> [(file, line_no), ...]
for tex in (LATEX / "sections").rglob("*.tex"):
    text = tex.read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.split("\n"), 1):
        for cm in cite_pat.finditer(line):
            keys = [k.strip() for k in cm.group(1).split(",")]
            for k in keys:
                file_usage[k].append({"file": str(tex.relative_to(REPO)), "line": i})

for e in entries:
    e["cited_in"] = file_usage.get(e["key"], [])

# ---------- 5. Build a citation graph (paper -> cited paper) ----------
# Only for entries that cite other entries (intra-bib citations)
edge_set = set()
for e in entries:
    for c in e["cited_in"]:
        for ck in [k.strip() for k in c.get("keys", [])] if False else [c]:
            # c is already a single key dict in file_usage
            pass
# Use tex-level citation pattern, not file_usage which lost keys
tex_edges = set()
for tex in (LATEX / "sections").rglob("*.tex"):
    text = tex.read_text(encoding="utf-8", errors="replace")
    for cm in cite_pat.finditer(text):
        keys = [k.strip() for k in cm.group(1).split(",")]
        for i, k_from in enumerate(keys):
            for j, k_to in enumerate(keys):
                if i != j:
                    tex_edges.add((k_from, k_to))

# ---------- 6. Export papers.json ----------
with open(KG / "papers.json", "w", encoding="utf-8") as f:
    json.dump({
        "schema_version": "1.0",
        "generated_at": "2026-06-30",
        "source_bib": str(REFS.relative_to(REPO)),
        "paper_count": len(entries),
        "categories": sorted(set(CATEGORY_MAP.values())),
        "papers": entries,
    }, f, indent=2, ensure_ascii=False)
print(f"Wrote {KG / 'papers.json'}")

# ---------- 7. Export papers.csv ----------
def csv_escape(s):
    s = str(s) if s else ""
    if any(c in s for c in [",", "\"", "\n", "\r"]):
        return '"' + s.replace('"', '""') + '"'
    return s

with open(KG / "papers.csv", "w", encoding="utf-8") as f:
    cols = ["key", "type", "title", "first_author", "all_authors", "year", "venue", "volume", "number", "pages", "doi", "eprint", "category", "concepts", "has_pdf", "pdf_path", "cited_count"]
    f.write(",".join(cols) + "\n")
    for e in entries:
        row = [
            csv_escape(e["key"]),
            csv_escape(e["type"]),
            csv_escape(e["title"]),
            csv_escape(e["authors"][0] if e["authors"] else ""),
            csv_escape("; ".join(e["authors"])),
            csv_escape(e["year"]),
            csv_escape(e["venue"]),
            csv_escape(e["volume"]),
            csv_escape(e["number"]),
            csv_escape(e["pages"]),
            csv_escape(e["doi"]),
            csv_escape(e["eprint"]),
            csv_escape(e["category"]),
            csv_escape("; ".join(e["concepts"])),
            csv_escape(e["has_pdf"]),
            csv_escape(e.get("pdf_path", "")),
            csv_escape(len(e["cited_in"])),
        ]
        f.write(",".join(row) + "\n")
print(f"Wrote {KG / 'papers.csv'}")

# ---------- 8. Export citations_in_thesis.csv ----------
with open(KG / "citations_in_thesis.csv", "w", encoding="utf-8") as f:
    f.write("bib_key,tex_file,line\n")
    for e in entries:
        for c in e["cited_in"]:
            f.write(f"{e['key']},{csv_escape(c['file'])},{c['line']}\n")
print(f"Wrote {KG / 'citations_in_thesis.csv'}")

# ---------- 9. Export concepts.json ----------
concept_to_papers = defaultdict(list)
for e in entries:
    for c in e["concepts"]:
        concept_to_papers[c].append(e["key"])
# Hierarchical grouping by top-level concept
concept_groups = defaultdict(list)
for c in concept_to_papers:
    top = c.split("_")[0] if "_" in c else c
    concept_groups[top].append(c)

with open(KG / "concepts.json", "w", encoding="utf-8") as f:
    json.dump({
        "schema_version": "1.0",
        "generated_at": "2026-06-30",
        "concept_count": len(concept_to_papers),
        "concept_to_papers": dict(concept_to_papers),
        "concept_groups": dict(concept_groups),
    }, f, indent=2, ensure_ascii=False)
print(f"Wrote {KG / 'concepts.json'}")

# ---------- 10. Export categories.json ----------
cat_to_papers = defaultdict(list)
for e in entries:
    cat_to_papers[e["category"]].append(e["key"])
with open(KG / "categories.json", "w", encoding="utf-8") as f:
    json.dump({
        "schema_version": "1.0",
        "generated_at": "2026-06-30",
        "category_count": len(cat_to_papers),
        "category_to_papers": dict(cat_to_papers),
        "category_descriptions": {
            "foundational_theory": "Bayesian persuasion, information design, rational inattention",
            "information_acquisition": "Sequential sampling, belief updating, evidence weighting",
            "algorithms_trust_hci": "Algorithm aversion/appreciation, trust in automation, CASA, anthropomorphism",
            "recommender_genai": "Recommender systems, transformers, LLMs, RLHF, foundation models",
            "narrative_epistemic": "Narrative persuasion, epistemic agency, LLM epistemic limits",
            "newly_added_candidates": "Background literature candidates added to references.bib",
            "advice_taking": "Judge-advisor paradigm, advice discounting, weight of advice (2026-06-29 batch)",
            "self_serving_attribution": "Self-serving bias, attribution theory, self-protection (2026-06-29 batch)",
            "overconfidence_control": "Overconfidence, illusion of control, perceived control (2026-06-29 batch)",
            "algorithm_aversion": "Algorithm/AI aversion and resistance mechanisms (2026-06-29 batch)",
            "uncategorized": "Awaiting manual categorization",
        },
    }, f, indent=2, ensure_ascii=False)
print(f"Wrote {KG / 'categories.json'}")

# ---------- 11. Export co-citation edges ----------
with open(KG / "edges_cocitation.csv", "w", encoding="utf-8") as f:
    f.write("source_key,target_key,file,line\n")
    for tex in (LATEX / "sections").rglob("*.tex"):
        text = tex.read_text(encoding="utf-8", errors="replace")
        rel = str(tex.relative_to(REPO))
        for cm in cite_pat.finditer(text):
            keys = [k.strip() for k in cm.group(1).split(",")]
            line_no = text[:cm.start()].count("\n") + 1
            for i, k_from in enumerate(keys):
                for j, k_to in enumerate(keys):
                    if i < j:
                        f.write(f"{k_from},{k_to},{csv_escape(rel)},{line_no}\n")
print(f"Wrote {KG / 'edges_cocitation.csv'}")

# ---------- 12. Summary stats ----------
print()
print("=== Summary ===")
print(f"Papers: {len(entries)}")
print(f"With PDF: {sum(1 for e in entries if e['has_pdf'])}")
print(f"Cited in thesis: {sum(1 for e in entries if e['cited_in'])}")
print(f"Categories: {len(cat_to_papers)}")
print(f"Unique concepts: {len(concept_to_papers)}")
print()
print("By category:")
for cat in sorted(cat_to_papers):
    print(f"  {cat}: {len(cat_to_papers[cat])}")