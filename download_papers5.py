"""Find the remaining 2 papers via CrossRef SSRN lookup and direct page probes."""
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


# Fryer/Harms/Jackson — search for SSRN ID specifically
print('=== Fryer/Harms/Jackson SSRN search ===')
items = crossref_query({
    'query.author': 'Fryer Harms Jackson',
    'query.bibliographic': '2019',
})
for item in items[:8]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    if 'ssrn' in doi.lower() or 'nber' in doi.lower():
        year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
        year = year_parts[0] if year_parts else '?'
        container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
        print(f'  {doi} | {year} | {container} | {title[:80]}')
    # also show all
    if 'updating' in title.lower() or 'belief' in title.lower():
        print(f'  -> {doi} | {title[:80]}')


# Liu/Zhang SSRN search
print('\n=== Liu/Zhang SSRN search ===')
items = crossref_query({
    'query.title': 'Counteracting Narratives Online',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    if 'counteract' in title.lower() or 'narrative' in title.lower():
        print(f'  {doi} | {title[:80]}')


# Try direct fetch of OUP ej article (with proper referer header)
def fetch_with_referer(url, target):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0',
            'Accept': 'application/pdf,text/html,*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://academic.oup.com/',
        })
        with urllib.request.urlopen(req, timeout=60) as r:
            ct = r.headers.get('Content-Type', '').lower()
            data = r.read()
            if 'pdf' in ct and data.startswith(b'%PDF'):
                if len(data) > 30000:
                    with open(target, 'wb') as f:
                        f.write(data)
                    return True, f'{len(data) // 1024} KB'
                return False, f'Too small ({len(data)} bytes)'
            elif 'html' in ct:
                return False, f'HTML page'
            else:
                return False, f'Not PDF (first: {data[:30]!r})'
    except Exception as e:
        return False, f'{type(e).__name__}: {str(e)[:80]}'


# Final attempts for Fryer
print('\n=== Final attempts for Fryer/Harms/Jackson ===')
fryer_urls = [
    # Try SSRN with different format
    'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3392968',
    # IZA Discussion Paper (Göttingen is IZA affiliate)
    'https://www.iza.org/publications/dp/12458',
    'https://docs.iza.org/dp12458.pdf',
    'https://ftp.iza.org/dp12458.pdf',
    # Try CEPR
    'https://cepr.org/active/publications/discussion_papers/dp.php?dpno=13156',
    # Try Philipp Harms' Göttingen (with pdf folder structure)
    'https://www.uni-goettingen.de/de/document/download/Updating_Beliefs.pdf',
]
target = os.path.join(PAPERS_DIR, '2019_Fryer_Updating_Beliefs.pdf')
for url in fryer_urls:
    ok, msg = fetch_with_referer(url, target)
    if ok:
        print(f'  [OK {msg}] {url}')
        break
    else:
        print(f'  [FAIL {msg}] {url[:70]}')


# Final attempts for Liu/Zhang
print('\n=== Final attempts for Liu/Zhang ===')
liu_urls = [
    # LMU Sili Zhang page
    'https://www.econ.lmu.de/en/faculty/research/sili-zhang/research/publications/index.html',
    # IZA discussion paper
    'https://docs.iza.org/dp17616.pdf',
    'https://ftp.iza.org/dp17616.pdf',
    'https://www.iza.org/publications/dp/17616',
    # CESifo
    'https://www.cesifo.org/DocDL/cesifo1_wp10495.pdf',
    'https://www.cesifo.org/node/70978',
    # ResearchGate
    'https://www.researchgate.net/publication/376961694_Counteracting_Narratives_Evidence_from_an_Online_Experiment',
    # try the abstract page and look for download link
    'https://academic.oup.com/ej/article-abstract/136/673/125/7638746',
]
target = os.path.join(PAPERS_DIR, 'Liu_Counteracting_Narratives.pdf')
for url in liu_urls:
    ok, msg = fetch_with_referer(url, target)
    if ok:
        print(f'  [OK {msg}] {url}')
        break
    else:
        print(f'  [FAIL {msg}] {url[:70]}')


# Final summary
print('\n=== FINAL FILES ===')
for f in sorted(os.listdir(PAPERS_DIR)):
    path = os.path.join(PAPERS_DIR, f)
    size = os.path.getsize(path) // 1024
    print(f'  {size:>7} KB  {f}')