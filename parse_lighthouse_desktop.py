#!/usr/bin/env python3
import json
import os
from pathlib import Path

# Map filenames to country/site names
SITE_MAP = {
    'coda-org-desktop.json': ('USA/Rahvusvaheline', 'https://coda.org'),
    'codauk-desktop.json': ('Ühendkuningriik', 'https://codauk.org'),
    'coda-deutschland-desktop.json': ('Saksamaa', 'https://coda-deutschland.de'),
    'codaireland-desktop.json': ('Iirimaa', 'https://codaireland.com'),
    'codacanada-desktop.json': ('Kanada', 'https://codacanada.ca'),
    'coda-au-desktop.json': ('Austraalia', 'https://www.codependentsanonymous.org.au'),
    'coda-israel-desktop.json': ('Iisrael', 'https://coda-israel.org.il'),
    'coda-nl-desktop.json': ('Holland', 'https://www.codependents-anonymous.nl'),
    'divulgacion-desktop.json': ('Hispaania Outreach', 'https://divulgacioncoda.org'),
    'fincoda-desktop.json': ('Soome (FinCoda)', 'http://fincoda.blogspot.com'),
    'helsinki-desktop.json': ('Soome (Helsinki)', 'http://codahelsinki.blogspot.com'),
    'estonia-desktop.json': ('Eesti (vana leht)', 'https://codaestonia.wordpress.com'),
}

def parse_lighthouse_json(filepath):
    """Parse Lighthouse JSON and extract scores."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        categories = data.get('categories', {})

        perf = categories.get('performance', {}).get('score')
        acc = categories.get('accessibility', {}).get('score')
        bp = categories.get('best-practices', {}).get('score')
        seo = categories.get('seo', {}).get('score')

        # Convert to percentages
        perf = int(perf * 100) if perf is not None else 0
        acc = int(acc * 100) if acc is not None else 0
        bp = int(bp * 100) if bp is not None else 0
        seo = int(seo * 100) if seo is not None else 0

        return {
            'performance': perf,
            'accessibility': acc,
            'best_practices': bp,
            'seo': seo
        }
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def main():
    lighthouse_dir = Path('/home/d0021/Automation/coda/lighthouse-testid')

    results = []

    for filename, (country, url) in SITE_MAP.items():
        filepath = lighthouse_dir / filename
        if filepath.exists():
            scores = parse_lighthouse_json(filepath)
            if scores:
                results.append({
                    'country': country,
                    'url': url,
                    'filename': filename,
                    **scores
                })

    # Sort by performance score (descending)
    results.sort(key=lambda x: x['performance'], reverse=True)

    print("=" * 80)
    print("LIGHTHOUSE DESKTOP TULEMUSED")
    print("=" * 80)
    print()

    for r in results:
        print(f"{r['country']} - {r['url']}")
        print(f"  Performance: {r['performance']} | Accessibility: {r['accessibility']} | Best Practices: {r['best_practices']} | SEO: {r['seo']}")
        print()

    print("=" * 80)
    print("PARIMAD LEHED (Performance)")
    print("=" * 80)
    top3 = results[:3]
    for i, r in enumerate(top3, 1):
        print(f"{i}. {r['country']} - Performance: {r['performance']}, Accessibility: {r['accessibility']}")

    print()
    print("=" * 80)
    print("HALVIMAD LEHED (Performance)")
    print("=" * 80)
    bottom3 = results[-3:]
    bottom3.reverse()
    for i, r in enumerate(bottom3, 1):
        print(f"{i}. {r['country']} - Performance: {r['performance']}, Accessibility: {r['accessibility']}")

if __name__ == '__main__':
    main()
