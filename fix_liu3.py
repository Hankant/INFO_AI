"""Try more URLs for Liu/Zhang."""
import urllib.request
import json
import os
import re


def fetch(url, binary=True):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        return data
    except Exception as e:
        return None


PAPERS_DIR = r'e:/Info_AI/behavioral_economics_belief_search_literature/pdf'
target = os.path.join(PAPERS_DIR, 'Liu_Counteracting_Narratives.pdf')

# Delete the wrong file
if os.path.exists(target):
    os.remove(target)
    print('Removed wrong IZA file\n')

# Try a comprehensive set of URLs
urls = [
    # IZA papers with various IDs - Liu/Zhang might use a different DP number
    'https://ftp.iza.org/dp16200.pdf',
    'https://ftp.iza.org/dp16488.pdf',
    'https://ftp.iza.org/dp16876.pdf',
    'https://ftp.iza.org/dp17149.pdf',
    'https://ftp.iza.org/dp17200.pdf',
    # Manwei Liu Nanjing Audit
    'https://research.nau.edu.cn/ws/portlet/file/download?fileId=21523',
    # LMU Sili Zhang publication list page
    'https://www.econ.lmu.de/en/faculty/research/sili-zhang/index.html',
    # Try Google Scholar PDF cache
    'https://scholar.googleusercontent.com/scholar?q=cache:Manwei+Liu+Sili+Zhang+counteracting+narratives',
    # CESifo working paper
    'https://www.cesifo.org/DocDL/cesifo1_wp9988.pdf',
    'https://www.cesifo.org/DocDL/cesifo1_wp10234.pdf',
    'https://www.cesifo.org/DocDL/cesifo1_wp10495.pdf',
    'https://www.cesifo.org/DocDL/cesifo1_wp10666.pdf',
    # Munich Center for the Economics of Aging
    'https://mea.mpisoc.mpg.de/4843864/research_papers',
]

for url in urls:
    data = fetch(url)
    if data is None:
        continue
    is_pdf = data.startswith(b'%PDF')
    is_html = b'<html' in data[:1000].lower()
    if is_pdf and len(data) > 30000:
        # Check title to ensure it's not another paper
        title_meta = re.search(rb'/Title\s*\(([^)]+)\)', data)
        title = title_meta.group(1).decode('latin-1', errors='replace') if title_meta else '?'
        if 'counteract' in title.lower() or 'narrative' in title.lower():
            with open(target, 'wb') as f:
                f.write(data)
            print(f'  [OK MATCHED {len(data) // 1024} KB] {url}')
            print(f'    Title: {title[:80]}')
            break
        else:
            print(f'  [PDF but title mismatch: {title[:60]}] {url}')
    elif is_html:
        # Look for PDF link in the HTML
        pdfs = re.findall(rb'href=["\']([^"\']*\.pdf)', data)
        if pdfs:
            print(f'  [HTML with PDF links: {len(pdfs)}] {url}')
            for p in pdfs[:3]:
                print(f'    PDF link: {p.decode("latin-1")[:80]}')
    else:
        print(f'  [OTHER {len(data)} bytes] {url}')

# If still not found, check IZA direct with semantic scholar for SSRN ID
print('\n\n=== Try Semantic Scholar one more time (after wait) ===')
import time
time.sleep(5)
try:
    req = urllib.request.Request(
        'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1093/ej/ueaf038?fields=title,externalIds,openAccessPdf,authors,year',
        headers={'User-Agent': 'mailto:test@example.com'}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    print(f'Title: {data.get("title")}')
    print(f'Authors: {[a.get("name") for a in data.get("authors", [])]}')
    print(f'Year: {data.get("year")}')
    ext = data.get('externalIds', {})
    print(f'External IDs: {ext}')
    if data.get('openAccessPdf'):
        print(f'OA PDF: {data["openAccessPdf"]}')
except Exception as e:
    print(f'Error: {e}')

# Check the file again
if os.path.exists(target):
    size = os.path.getsize(target)
    print(f'\n[FINAL] {target}: {size:,} bytes ({size // 1024} KB)')
    with open(target, 'rb') as f:
        title = re.search(rb'/Title\s*\(([^)]+)\)', f.read())
        if title:
            print(f'Title: {title.group(1).decode("latin-1")}')
else:
    print(f'\n[FINAL] No PDF downloaded for Liu/Zhang')