"""Find Fryer/Harms/Jackson correct DOI."""
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


# Try different combinations
print('=== Fryer/Harms/Jackson ===')
items = crossref_query({
    'query.author': 'Roland Fryer Philipp Harms Matthew Jackson',
    'query.title': 'Updating Beliefs',
})
for item in items[:8]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    print(f'  {doi} | {year} | {container[:40]} | {authors} | {title[:60]}')

# Try Jackson Fryer Harms with title
print('\n=== Try "Beliefs Evidence Interpretation" ===')
items = crossref_query({
    'query.title': 'Updating Beliefs Evidence Interpretation',
})
for item in items[:8]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'belief' in title.lower() or 'evidence' in title.lower():
        print(f'  {doi} | {year} | {container[:40]} | {authors} | {title[:80]}')

# Try via Google Scholar proxy
print('\n=== Try by Jackson Matthew ===')
items = crossref_query({
    'query.author': 'Jackson',
    'query.title': 'Beliefs Open Interpretation',
})
for item in items[:8]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'belief' in title.lower():
        print(f'  {doi} | {year} | {container[:40]} | {authors} | {title[:80]}')

# Now try direct doi.org lookup with likely DOIs
print('\n=== Trying likely DOIs ===')
for doi in [
    '10.1093/jeea/jvz020',  # guess from 2019
    '10.1093/jeea/jvy037',
    '10.1093/jeea/jvz040',
]:
    try:
        url = f'https://api.crossref.org/works/{doi}'
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        msg = data.get('message', {})
        title = msg.get('title', ['?'])[0]
        if 'belief' in title.lower() or 'evidence' in title.lower():
            print(f'  *** {doi}: {title}')
            print(f'      Container: {msg.get("container-title", ["?"])[0]}')
            print(f'      Authors: {[(a.get("given", "") + " " + a.get("family", "")).strip() for a in msg.get("author", [])]}')
            print(f'      Volume: {msg.get("volume")}, Issue: {msg.get("issue")}, Page: {msg.get("page")}')
    except Exception as e:
        pass  # silent

# Try to query by author name + year
print('\n=== Try with year filter ===')
items = crossref_query({
    'query.author': 'Fryer Harms Jackson',
    'query.bibliographic': '2019',
    'query.title': 'Beliefs',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    print(f'  {doi} | {year} | {container[:40]} | {authors} | {title[:80]}')