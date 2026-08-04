"""Verify each PDF: %PDF header, valid structure, sample text."""
import os
import zlib
import re


PAPERS_DIR = r'e:/Info_AI/behavioral_economics_belief_search_literature/pdf'

files = sorted(os.listdir(PAPERS_DIR))
print('=== PDF VERIFICATION ===\n')

for f in files:
    path = os.path.join(PAPERS_DIR, f)
    size = os.path.getsize(path)
    print(f'{f}:')
    print(f'  Size: {size:,} bytes ({size // 1024} KB)')

    with open(path, 'rb') as fh:
        header = fh.read(8)
    is_pdf = header.startswith(b'%PDF-')
    print(f'  Header valid: {is_pdf} (got: {header[:8]!r})')

    # Read more to check structure
    with open(path, 'rb') as fh:
        content = fh.read()

    # Look for %%EOF marker
    eof_count = content.count(b'%%EOF')
    print(f'  %%EOF count: {eof_count}')

    # Check for compressed streams (typical for PDFs)
    has_streams = b'stream' in content and b'endstream' in content
    print(f'  Has streams: {has_streams}')

    # Try to find some readable text by looking for uncompressed text in metadata
    # Check for first page metadata
    title_meta = re.search(rb'/Title\s*\(([^)]+)\)', content)
    author_meta = re.search(rb'/Author\s*\(([^)]+)\)', content)

    if title_meta:
        try:
            print(f'  /Title: {title_meta.group(1).decode("latin-1")[:80]}')
        except:
            pass
    if author_meta:
        try:
            print(f'  /Author: {author_meta.group(1).decode("latin-1")[:80]}')
        except:
            pass

    # Look for Adobe Acrobat version info
    pdfver = re.search(rb'%PDF-(\d+\.\d+)', content)
    if pdfver:
        print(f'  PDF version: {pdfver.group(1).decode()}')

    # Status
    status = 'VALID' if is_pdf and eof_count >= 1 and has_streams else 'SUSPICIOUS'
    print(f'  STATUS: {status}\n')