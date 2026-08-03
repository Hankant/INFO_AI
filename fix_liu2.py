"""Find Liu/Zhang via Semantic Scholar with rate limiting."""
import urllib.request
import urllib.parse
import json
import os
import time


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        return data
    except Exception as e:
        print(f'Error: {e}')
        return None


# Semantic Scholar search
print('=== Semantic Scholar search for Counteracting Narratives ===')
time.sleep(3)
url = 'https://api.semanticscholar.org/graph/v1/paper/search?query=Counteracting+Narratives+Online+Experiment&limit=10&fields=title,externalIds,openAccessPdf,authors,year,venue'
data = fetch(url)
if data:
    for paper in data.get('data', []):
        print(f"  {paper.get('paperId')}: {paper.get('title')[:70]}")
        print(f"    Year: {paper.get('year')}, Venue: {paper.get('venue')}")
        ext = paper.get('externalIds', {})
        print(f"    DOI: {ext.get('DOI')}, ArXiv: {ext.get('ArXiv')}")
        if paper.get('openAccessPdf'):
            print(f"    Open PDF: {paper['openAccessPdf'].get('url')}")
        authors = paper.get('authors', [])
        if authors:
            print(f"    Authors: {[a.get('name') for a in authors[:3]]}")
        print()


# Try IZA papers for Counteracting Narratives by Liu and Zhang
print('\n=== Search IZA Discussion Papers site ===')
time.sleep(2)
url = 'https://www.iza.org/publications/dps?search=Counteracting+Narratives'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        html = r.read()
    import re
    # find IZA paper numbers
    paper_ids = re.findall(rb'/publications/dp/(\d+)', html)
    print(f'  Found IZA DP IDs: {[p.decode() for p in paper_ids[:10]]}')
except Exception as e:
    print(f'  Error: {e}')


# Try Sili Zhang's homepage via Google scholar
time.sleep(2)
print('\n=== Try Google Scholar cached PDF ===')
url = 'https://scholar.googleusercontent.com/scholar?q=cache:sili+zhang+counteracting+narratives'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    print(f'  Got {len(data)} bytes from Google Scholar')
    import re
    pdfs = re.findall(rb'href=["\']([^"\']*\.pdf)', data)
    print(f'  PDF links: {[p.decode("latin-1")[:80] for p in pdfs[:5]]}')
except Exception as e:
    print(f'  Error: {e}')


# Direct: try SSRN abstract page for the Liu/Zhang paper
time.sleep(2)
print('\n=== Try SSRN search interface ===')
ssrn_search_url = 'https://papers.ssrn.com/sol3/results.cfm?txtSelected=Counteracting+Narratives+Liu+Zhang'
try:
    req = urllib.request.Request(ssrn_search_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    import re
    # find SSRN paper IDs (5-digit numbers)
    paper_ids = re.findall(rb'abstract_id=(\d+)', data)
    print(f'  Found abstract IDs: {[p.decode() for p in paper_ids[:5]]}')
except Exception as e:
    print(f'  Error: {e}')