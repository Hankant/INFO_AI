"""Find the correct Liu/Zhang paper and replace the wrong file."""
import urllib.request
import urllib.parse
import json
import os


PAPERS_DIR = r'e:/Info_AI/behavioral_economics_belief_search_literature/pdf'


def crossref_query(query_params, top_n=5):
    base = 'https://api.crossref.org/works?'
    url = base + '&'.join(f'{k}={urllib.parse.quote_plus(v)}' for k, v in query_params.items()) + f'&rows={top_n}'
    req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
        return data.get('message', {}).get('items', [])
    except Exception as e:
        print(f'  ERROR: {e}')
        return []


# Look up Liu/Zhang DOI to find all related works (preprints, working papers)
print('=== Liu/Zhang all versions ===')
url = 'https://api.crossref.org/works/10.1093/ej/ueaf038'
req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    msg = data.get('message', {})
    print(f'Title: {msg.get("title", ["?"])[0]}')
    print(f'DOI: {msg.get("DOI")}')
    print(f'Authors: {[(a.get("given", "") + " " + a.get("family", "")).strip() for a in msg.get("author", [])]}')
    # Check link/relation fields
    print(f'Related works (is-referenced-by etc.): {msg.get("is-referenced-by-count", "?")}')
    # look at all link fields
    for link in msg.get('link', []):
        print(f'  Link: {link}')
    # check for SSRN preprint
    for subtype in msg.get('subtype', []):
        print(f'  Subtype: {subtype}')
except Exception as e:
    print(f'Error: {e}')


# Try different IZA paper IDs - Liu/Zhang Counteracting Narratives
print('\n=== IZA search ===')
items = crossref_query({
    'query.author': 'Liu Zhang',
    'query.title': 'Counteracting Narratives',
})
for item in items[:10]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    if 'counteract' in title.lower() or 'narrative' in title.lower():
        print(f'  *** {doi} | {title[:80]}')


# Try LMU Sili Zhang's actual page
print('\n=== LMU Sili Zhang page probe ===')
urls = [
    'https://www.econ.lmu.de/en/faculty/research/sili-zhang/research/index.html',
    'https://www.econ.lmu.de/en/faculty/research/sili-zhang/publications/index.html',
    'https://sites.google.com/view/sili-zhang',
]
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        print(f'  [{len(data)} bytes] {url}')
        # Look for PDF links
        import re
        pdf_links = re.findall(rb'href=["\']([^"\']*\.pdf[^"\']*)', data)
        for link in pdf_links[:5]:
            print(f'    PDF link: {link.decode("latin-1")[:80]}')
    except Exception as e:
        print(f'  [{type(e).__name__}] {url}')


# Try Manwei Liu Nanjing Audit
print('\n=== Manwei Liu page probe ===')
urls = [
    'https://research.nau.edu.cn/en/persons/manwei-liu/publications/',
    'https://nau.edu.cn',
    'https://www.sem.nau.edu.cn/en/Faculty/Show/33',
]
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        import re
        pdf_links = re.findall(rb'href=["\']([^"\']*\.pdf[^"\']*)', data)
        for link in pdf_links[:5]:
            print(f'  [{len(data)} bytes] {url}')
            print(f'    PDF link: {link.decode("latin-1")[:80]}')
            break
    except Exception as e:
        print(f'  [{type(e).__name__}] {url}')


# Try SSRN direct search by paper title
print('\n=== SSRN API search ===')
ssrn_url = 'https://api.ssrn.com/v1/papers/search?q=Counteracting+Narratives+Liu+Zhang'
try:
    req = urllib.request.Request(ssn_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r) if hasattr(r, 'read') else r.read()
    print(f'  Got data: {str(data)[:200]}')
except Exception as e:
    print(f'  Error: {e}')


# Try Semantic Scholar API
print('\n=== Semantic Scholar search ===')
ss_url = 'https://api.semanticscholar.org/graph/v1/paper/search?query=Counteracting+Narratives+Online+Experiment&limit=5'
try:
    req = urllib.request.Request(ss_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    for paper in data.get('data', []):
        print(f"  {paper.get('paperId')}: {paper.get('title')}")
        for ext in paper.get('externalIds', {}).items():
            print(f'    {ext}')
        if paper.get('openAccessPdf'):
            print(f"    Open PDF: {paper['openAccessPdf'].get('url')}")
except Exception as e:
    print(f'  Error: {e}')