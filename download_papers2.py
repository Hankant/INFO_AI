"""Probe more OA sources for each paper."""
import urllib.request
import os


PAPERS_DIR = r'e:/Info_AI/behavioral_economics_belief_search_literature/pdf'

# (filename, list of URLs to try)
papers = [
    ('2024_Graeber_Stories_Statistics_and_Memory.pdf', [
        # SSRN abstract page
        'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4291741',
        # NBER search for Graeber
        'https://www.nber.org/papers/w32017',
        'https://www.nber.org/papers/w31704',
        # Try direct from Google Scholar cached versions
        'https://scholar.googleusercontent.com/scholar?q=cache:Graeber+Roth+Zimmermann+2024+Stories+Statistics',
    ]),
    ('2019_Fryer_Updating_Beliefs.pdf', [
        # Stanford Jackson page direct PDFs
        'https://web.stanford.edu/~jacksonm/updating.pdf',
        'https://web.stanford.edu/~jacksonm/updating_beliefs.pdf',
        'https://web.stanford.edu/~jacksonm/fryer_harms_jackson.pdf',
        # Göttingen Harms page
        'https://www.uni-goettingen.de/de/document/download/58bbce80a3b386c9de06ea7f42a9f7b9.pdf/Harms_Fryer_Jackson_2019_Updating_Beliefs.pdf',
    ]),
    ('Liu_Counteracting_Narratives.pdf', [
        # Manwei Liu Nanjing Audit Univ
        'https://nau.edu.cn/__local/F/A9/E7/10F46D2C68F8BC8B5BC0BC33D55_F5E5F3D7_19FB46.pdf',
        # Sili Zhang LMU
        'https://www.econ.lmu.de/en/faculty/research/sili-zhang/research/index.html',
    ]),
    ('2011_Caplin_Search_and_Satisficing.pdf', [
        # NYU Caplin
        'https://www.nyu.edu/economics/user/bcaplin/papers/searchsatisficing.pdf',
        # AEA Open Access Papers program
        'https://www.aeaweb.org/articles?id=10.1257/aer.101.7.2899',
    ]),
    ('2006_Gabaix_Costly_Information_Acquisition.pdf', [
        # Harvard Laibson
        'https://scholar.harvard.edu/dlaibson/files/costly_information_acquisition.pdf',
        'https://scholar.harvard.edu/files/dlaibson/files/costly_information_acquisition.pdf',
        # AEA Open Access
        'https://www.aeaweb.org/articles?id=10.1257/aer.96.4.1043',
    ]),
    ('2023_Haaland_Designing_Information_Provision_Experiments.pdf', [
        # AEA JEL is generally open access
        'https://www.aeaweb.org/articles?id=10.1257/jel.20211658',
        # SSRN
        'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3644820',
    ]),
]


def fetch_meta(url):
    """Just return headers without downloading."""
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, dict(r.headers), r.headers.get('Content-Length', '?')
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), '?'
    except Exception as e:
        return None, None, type(e).__name__


def download(url, target):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=60) as r:
            ct = r.headers.get('Content-Type', '')
            data = r.read()
            if 'html' in ct.lower() and not data.startswith(b'%PDF'):
                return False, f'HTML page, {len(data)} bytes'
            if not data.startswith(b'%PDF'):
                return False, f'Not a PDF (first: {data[:30]!r})'
            if len(data) < 30000:
                return False, f'Too small ({len(data)} bytes)'
            with open(target, 'wb') as f:
                f.write(data)
            return True, f'{len(data) // 1024} KB'
    except Exception as e:
        return False, f'{type(e).__name__}: {str(e)[:80]}'


# Phase 1: probe URLs
print('=== PROBING URLs (HEAD requests) ===')
for filename, urls in papers:
    print(f'\n{filename}:')
    for url in urls:
        status, headers, cl = fetch_meta(url)
        if status == 200 and headers and 'pdf' in headers.get('Content-Type', '').lower():
            print(f'  [200 PDF] {url}')
        elif status == 200:
            print(f'  [200 HTML] {url} (cl={cl})')
        else:
            print(f'  [{status}] {url}')


# Phase 2: download what's plausible
print('\n\n=== DOWNLOAD ATTEMPTS ===')
results = []
for filename, urls in papers:
    target = os.path.join(PAPERS_DIR, filename)
    print(f'\n{filename}:')
    success = False
    for url in urls:
        ok, msg = download(url, target)
        if ok:
            print(f'  [OK {msg}] {url}')
            success = True
            break
        else:
            print(f'  [FAIL {msg[:50]}] {url[:80]}')
    results.append((filename, success, urls[0] if urls else None))

print('\n\n=== SUMMARY ===')
for f, ok, url in results:
    status = 'OK' if ok else 'FAIL'
    print(f'  [{status}] {f} | first URL: {url}')