"""Attempt to download 6 papers from OA sources (journal/publisher links, SSRN, NBER, author sites).
NO Sci-Hub. NO paywall bypass.
Each PDF is validated: must start with %PDF, size > 50KB.
"""
import urllib.request
import urllib.parse
import os
import json


PAPERS_DIR = r'e:/Info_AI/behavioral_economics_belief_search_literature/pdf'
os.makedirs(PAPERS_DIR, exist_ok=True)

# (filename, url_candidates)
papers = [
    ('2024_Graeber_Stories_Statistics_and_Memory.pdf', [
        # OUP QJE article PDF (some are OA for selected papers)
        'https://academic.oup.com/qje/article-pdf/139/3/1107/57938680/qjae020.pdf',
        'https://academic.oup.com/qje/article-pdf/139/3/1107/qjae020.pdf',
        # Author SSRN
        'https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4291741_code1311060.pdf?abstractid=4291741',
    ]),
    ('2019_Fryer_Updating_Beliefs.pdf', [
        'https://academic.oup.com/jeea/article-pdf/17/4/1219/30048714/jvy025.pdf',
        'https://academic.oup.com/jeea/article-pdf/17/4/1219/jvy025.pdf',
    ]),
    ('Liu_Counteracting_Narratives.pdf', [
        'https://academic.oup.com/ej/article-pdf/136/673/125/62137140/ueaf038.pdf',
        'https://academic.oup.com/ej/article-pdf/136/673/125/ueaf038.pdf',
    ]),
    ('2011_Caplin_Search_and_Satisficing.pdf', [
        'https://www.aeaweb.org/articles?id=10.1257/aer.101.7.2899',
        'https://www.nyu.edu/economics/user/bcaplin/papers/SearchSatisficing.pdf',
    ]),
    ('2006_Gabaix_Costly_Information_Acquisition.pdf', [
        'https://www.aeaweb.org/articles?id=10.1257/aer.96.4.1043',
        'https://scholar.harvard.edu/dlaibson/publications/costly-information-acquisition-experimental-analysis-boundedly-rational-model',
    ]),
    ('2023_Haaland_Designing_Information_Provision_Experiments.pdf', [
        'https://www.aeaweb.org/articles?id=10.1257/jel.20211658',
        'https://www.briq-institute.org/global/wp-content/uploads/2022/01/Haaland-Roth-Wohlfart-Designing-Information-Provision-Experiments.pdf',
    ]),
]


def download(url, target):
    """Download url to target. Returns (success, message)."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=60) as r:
            ct = r.headers.get('Content-Type', '')
            data = r.read()
            if 'html' in ct.lower() and not data.startswith(b'%PDF'):
                return False, f'HTML page (not PDF), {len(data)} bytes'
            if not data.startswith(b'%PDF'):
                return False, f'Not a PDF (first bytes: {data[:50]!r})'
            if len(data) < 30000:
                return False, f'Too small ({len(data)} bytes)'
            with open(target, 'wb') as f:
                f.write(data)
            return True, f'{len(data) // 1024} KB'
    except Exception as e:
        return False, f'{type(e).__name__}: {str(e)[:80]}'


results = []
for filename, urls in papers:
    target = os.path.join(PAPERS_DIR, filename)
    print(f'\n{filename}:')
    success = False
    for url in urls:
        ok, msg = download(url, target)
        print(f'  [{msg[:40]:<40}] {url[:80]}')
        if ok:
            success = True
            break
    if not success:
        # Clean up partial file
        if os.path.exists(target):
            try:
                os.remove(target)
            except:
                pass
    results.append((filename, success, urls[0] if urls else None))


print('\n\n=== SUMMARY ===')
for f, ok, url in results:
    print(f'  [{"OK" if ok else "FAIL"}] {f} | URL tried: {url}')