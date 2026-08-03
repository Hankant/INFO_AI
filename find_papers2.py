"""Retry failed queries and find Liu/Zhang full names."""
import urllib.request
import urllib.parse
import json


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


# Find full author names for Liu/Zhang via direct DOI lookup
print('=== Liu/Zhang full names (DOI lookup) ===')
url = 'https://api.crossref.org/works/10.1093/ej/ueaf038'
req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    msg = data.get('message', {})
    print(f'Title: {msg.get("title", ["?"])[0]}')
    print(f'Subtitle: {msg.get("subtitle", ["?"])}')
    print(f'Container: {msg.get("container-title", ["?"])[0]}')
    print(f'DOI: {msg.get("DOI")}')
    print(f'Authors:')
    for a in msg.get('author', []):
        given = a.get('given', '')
        family = a.get('family', '')
        aff = a.get('affiliation', [])
        aff_names = [x.get('name', '') for x in aff]
        print(f'  {given} {family} | {aff_names}')
    print(f'Volume: {msg.get("volume")}')
    print(f'Issue: {msg.get("issue")}')
    print(f'Page: {msg.get("page")}')
    print(f'Year: published = {msg.get("published", {})}')
    print(f'Issue date: {msg.get("issue-date-parts", {})}')
    print(f'Publisher: {msg.get("publisher")}')
    print(f'Type: {msg.get("type")}')
    print(f'URL: {msg.get("URL")}')
except Exception as e:
    print(f'Error: {e}')

# Fryer/Harms/Jackson retry
print('\n=== Fryer/Harms/Jackson (retry) ===')
items = crossref_query({
    'query.author': 'Fryer Harms Jackson',
    'query.bibliographic': '2019',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'updating' in title.lower() or 'evidence' in title.lower():
        print(f'  *** {doi} | {year} | {container} | {authors} | {title[:80]}')

# Caplin/Dean/Martin retry
print('\n=== Caplin/Dean/Martin (retry) ===')
items = crossref_query({
    'query.author': 'Caplin Dean Martin',
    'query.title': 'Search Satisficing',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'search' in title.lower() and 'satisficing' in title.lower():
        print(f'  *** {doi} | {year} | {container} | {authors} | {title[:80]}')

# Gabaix/Laibson retry
print('\n=== Gabaix/Laibson (retry) ===')
items = crossref_query({
    'query.author': 'Gabaix Laibson',
    'query.title': 'Costly Information Acquisition',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'costly' in title.lower() or 'information' in title.lower():
        print(f'  *** {doi} | {year} | {container} | {authors} | {title[:80]}')

# Haaland/Roth/Wohlfart retry
print('\n=== Haaland/Roth/Wohlfart (retry) ===')
items = crossref_query({
    'query.author': 'Haaland Roth Wohlfart',
    'query.title': 'Designing Information Provision',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'information' in title.lower() and 'experiment' in title.lower():
        print(f'  *** {doi} | {year} | {container} | {authors} | {title[:80]}')

# Direct DOI lookups (more reliable than title search)
print('\n=== Direct DOI lookups ===')
dois = {
    'Fryer/Harms/Jackson': '10.1093/jeea/jvz009',
    'Caplin/Dean/Martin': '10.1257/aer.101.7.2462',
    'Gabaix/Laibson': '10.1257/aer.96.4.1023',
    'Haaland/Roth/Wohlfart': '10.1257/jel.20231616',
}
for label, doi in dois.items():
    print(f'\n  {label} ({doi}):')
    try:
        url = f'https://api.crossref.org/works/{doi}'
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        msg = data.get('message', {})
        print(f'    Title: {msg.get("title", ["?"])[0]}')
        print(f'    Container: {msg.get("container-title", ["?"])[0]}')
        print(f'    Authors: {[(a.get("given", "") + " " + a.get("family", "")).strip() for a in msg.get("author", [])]}')
        print(f'    Volume: {msg.get("volume")}, Issue: {msg.get("issue")}, Page: {msg.get("page")}')
        print(f'    Year: {msg.get("published-print", msg.get("published-online", {})).get("date-parts", [[None]])[0]}')
        print(f'    OA URL: {[u.get("URL") for u in msg.get("resource", {}).get("OA", []) if u.get("URL")]}')
        # Also check links
        for link in msg.get('link', []):
            print(f'    Link: {link.get("URL")} (content-type={link.get("content-type")})')
    except Exception as e:
        print(f'    ERROR: {e}')