"""Verify all 6 papers via CrossRef API and find DOIs."""
import urllib.request
import json
import os
import re


def crossref_query(query_params, top_n=5):
    base = 'https://api.crossref.org/works?'
    url = base + '&'.join(f'{k}={urllib.parse.quote_plus(v)}' for k, v in query_params.items()) + f'&rows={top_n}'
    req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        return data.get('message', {}).get('items', [])
    except Exception as e:
        print(f'  ERROR: {e}')
        return []


import urllib.parse

print('=== Liu & Zhang "Counteracting Narratives" ===')
items = crossref_query({
    'query.title': 'Counteracting Narratives',
    'query.container-title': 'The Economic Journal',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:3]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'narrative' in title.lower() or 'counter' in title.lower():
        print(f'  *** {doi} | {year} | {container} | {authors} | {title[:60]}')
    else:
        print(f'  --  {doi} | {year} | {container} | {authors} | {title[:60]}')

print('\n=== Graeber/Roth/Zimmermann 2024 QJE ===')
items = crossref_query({
    'query.author': 'Graeber Roth Zimmermann',
    'query.title': 'Stories Statistics Memory',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    print(f'  {doi} | {year} | {container} | {authors} | {title[:60]}')

print('\n=== Fryer/Harms/Jackson 2019 JEEA ===')
items = crossref_query({
    'query.author': 'Fryer Harms Jackson',
    'query.title': 'Updating Beliefs Evidence',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    print(f'  {doi} | {year} | {container} | {authors} | {title[:60]}')

print('\n=== Caplin/Dean/Martin 2011 AER ===')
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
    print(f'  {doi} | {year} | {container} | {authors} | {title[:60]}')

print('\n=== Gabaix/Laibson/Moloche/Weinberg 2006 ===')
items = crossref_query({
    'query.author': 'Gabaix Laibson Moloche Weinberg',
})
for item in items[:5]:
    title = item.get('title', ['?'])[0]
    doi = item.get('DOI', 'no-doi')
    authors = ', '.join([(a.get('family', '') or '') for a in item.get('author', [])[:5]])
    year_parts = item.get('published-print', item.get('published-online', {})).get('date-parts', [[None]])[0]
    year = year_parts[0] if year_parts else '?'
    container = item.get('container-title', ['?'])[0] if item.get('container-title') else '?'
    if 'costly' in title.lower() or 'information' in title.lower():
        print(f'  *** {doi} | {year} | {container} | {authors} | {title[:60]}')
    else:
        print(f'  --  {doi} | {year} | {container} | {authors} | {title[:60]}')

print('\n=== Haaland/Roth/Wohlfart 2023 JEL ===')
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
    print(f'  {doi} | {year} | {container} | {authors} | {title[:60]}')