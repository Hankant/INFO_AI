"""Retry remaining 3 papers with longer timeouts and more sources."""
import urllib.request
import os
import time


PAPERS_DIR = r'e:/Info_AI/behavioral_economics_belief_search_literature/pdf'


def download_resume(url, target, timeout=180, max_retries=3):
    """Download with longer timeout and retry on IncompleteRead."""
    last_err = None
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/pdf,*/*',
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                ct = r.headers.get('Content-Type', '').lower()
                data = r.read()
                if 'html' in ct and not data.startswith(b'%PDF'):
                    return False, f'HTML page, {len(data)} bytes'
                if not data.startswith(b'%PDF'):
                    return False, f'Not PDF (first: {data[:30]!r})'
                if len(data) < 30000:
                    return False, f'Too small ({len(data)} bytes)'
                with open(target, 'wb') as f:
                    f.write(data)
                return True, f'{len(data) // 1024} KB'
        except Exception as e:
            last_err = f'{type(e).__name__}: {str(e)[:80]}'
            time.sleep(2)
    return False, last_err


# Remaining 3 papers
papers = [
    ('2019_Fryer_Updating_Beliefs.pdf', [
        # Try a few more SSRN IDs for Fryer Harms Jackson
        'https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3392968_code458271.pdf?abstractid=3392968',
        # Stanford alternative
        'https://web.stanford.edu/~jacksonm/papersarticles_files/updating.pdf',
        'https://web.stanford.edu/~jacksonm/papersarticles_files/updating_beliefs.pdf',
        'https://web.stanford.edu/~jacksonm/beliefs_open_interpretation.pdf',
        # Try CEPR / SSRN alternative
        'https://cepr.org/active/publications/discussion_papers/dp.php?dpno=13000',
        # Try direct
        'https://web.stanford.edu/~jacksonm/updating.pdf',
        # Try Google scholar PDF
        'https://scholar.google.com/scholar?q=Fryer+Harms+Jackson+Updating+Beliefs',
    ]),
    ('Liu_Counteracting_Narratives.pdf', [
        # Try Manwei Liu SSRN
        'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4532298',
        # Liu Nanjing Audit Univ
        'https://research.nau.edu.cn/en/persons/manwei-liu',
        # Sili Zhang LMU papers
        'https://www.ifo.org/en/publications/2023/working-paper/luis-and-the-effects-of-online-experiments',
        # ResearchGate Liu/Zhang
        'https://www.researchgate.net/publication/367342345',
        # OUP article (with referer header)
        'https://academic.oup.com/ej/article/136/673/125/7638746',
    ]),
    ('2011_Caplin_Search_and_Satisficing.pdf', [
        # NBER — the paper is Caplin/Dean/Martin
        'https://www.nber.org/system/files/working_papers/w17267/w17267.pdf',
        'https://www.nber.org/system/files/working_papers/w16729/w16729.pdf',
        # NYU Caplin page (alternate format)
        'https://wp.nyu.edu/econ/directory/andrew-caplin/',
        # Daniel Martin LSE
        'https://personal.lse.ac.uk/martidj/SearchSatisficing.pdf',
        'https://www.lse.ac.uk/economics/people/daniel-martin',
    ]),
]


print('=== RETRY REMAINING 3 PAPERS ===\n')
results = []
for filename, urls in papers:
    target = os.path.join(PAPERS_DIR, filename)
    if os.path.exists(target):
        os.remove(target)  # remove partial
    print(f'{filename}:')
    success = False
    for url in urls:
        ok, msg = download_resume(url, target, timeout=180)
        if ok:
            print(f'  [OK {msg}] {url}')
            success = True
            break
        else:
            print(f'  [FAIL {msg[:50]}] {url[:80]}')
    if not success and os.path.exists(target):
        try:
            os.remove(target)
        except:
            pass
    results.append((filename, success))
    print()

print('=== SUMMARY ===')
for f, ok in results:
    print(f'  [{"OK" if ok else "FAIL"}] {f}')