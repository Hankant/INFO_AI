"""Try direct PDF URLs from AEA pubs, NBER, and SSRN."""
import urllib.request
import os
import json


PAPERS_DIR = r'e:/Info_AI/behavioral_economics_belief_search_literature/pdf'

# (filename, urls to try) - more specific patterns
papers = [
    ('2024_Graeber_Stories_Statistics_and_Memory.pdf', [
        # NBER working paper direct PDF (try common numbers)
        'https://www.nber.org/system/files/working_papers/w31704/w31704.pdf',
        'https://www.nber.org/system/files/working_papers/w32017/w32017.pdf',
        'https://www.nber.org/system/files/working_papers/w31082/w31082.pdf',
        # QJE paper at OUP — open if it has open-access flag
        'https://academic.oup.com/qje/article-pdf/139/3/1107/57938680/qjae020.pdf',
        # SSRN delivery URL
        'https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4291741_code1311060.pdf?abstractid=4291741&mirid=1',
    ]),
    ('2019_Fryer_Updating_Beliefs.pdf', [
        # SSRN alternative pattern
        'https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3392968_code458271.pdf?abstractid=3392968&mirid=1',
        # OUP JEEA with academic cookie
        'https://academic.oup.com/jeea/article-pdf/17/4/1219/30048714/jvy025.pdf',
        # Harms Göttingen
        'https://www.uni-goettingen.de/de/document/download/59bbce80a3b386c9de06ea7f42a9f7b9.pdf/Updating_Beliefs_Fryer_Harms_Jackson_2019.pdf',
    ]),
    ('Liu_Counteracting_Narratives.pdf', [
        # OUP EJ open
        'https://academic.oup.com/ej/article-pdf/136/673/125/62137140/ueaf038.pdf',
        # LMU Sili Zhang page
        'https://www.econ.lmu.de/en/faculty/research/sili-zhang/research/index.html',
    ]),
    ('2011_Caplin_Search_and_Satisficing.pdf', [
        # AEA pubs PDF
        'https://pubs.aeaweb.org/doi/pdf/10.1257/aer.101.7.2899',
        # NBER papers (Caplin/Dean/Martin have NBER w17267)
        'https://www.nber.org/system/files/working_papers/w17267/w17267.pdf',
        'https://www.nber.org/system/files/working_papers/w16729/w16729.pdf',
    ]),
    ('2006_Gabaix_Costly_Information_Acquisition.pdf', [
        # NBER (Gabaix/Laibson/Moloche/Weinberg paper)
        'https://www.nber.org/system/files/working_papers/w11772/w11772.pdf',
        'https://www.nber.org/system/files/working_papers/w10988/w10988.pdf',
        # AEA pubs PDF
        'https://pubs.aeaweb.org/doi/pdf/10.1257/aer.96.4.1043',
    ]),
    ('2023_Haaland_Designing_Information_Provision_Experiments.pdf', [
        # AEA pubs PDF
        'https://pubs.aeaweb.org/doi/pdf/10.1257/jel.20211658',
        # NBER
        'https://www.nber.org/system/files/working_papers/w28600/w28600.pdf',
        # briq
        'https://www.briq-institute.org/global/wp-content/uploads/2022/01/Haaland-Roth-Wohlfart-Designing-Information-Provision-Experiments.pdf',
    ]),
]


def download(url, target):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=60) as r:
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
        return False, f'{type(e).__name__}: {str(e)[:80]}'


print('=== DOWNLOAD ATTEMPTS ===')
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
    if not success and os.path.exists(target):
        try:
            os.remove(target)
        except:
            pass
    results.append((filename, success))

print('\n\n=== SUMMARY ===')
for f, ok in results:
    print(f'  [{"OK" if ok else "FAIL"}] {f}')