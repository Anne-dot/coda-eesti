#!/usr/bin/env python3
import json
import os
from pathlib import Path

# Map filenames to country/site names
SITE_MAP = {
    'coda-org': ('USA/Rahvusvaheline', 'https://coda.org'),
    'codauk': ('Ühendkuningriik', 'https://codauk.org'),
    'coda-deutschland': ('Saksamaa', 'https://coda-deutschland.de'),
    'codaireland': ('Iirimaa', 'https://codaireland.com'),
    'codacanada': ('Kanada', 'https://codacanada.ca'),
    'coda-au': ('Austraalia', 'https://www.codependentsanonymous.org.au'),
    'coda-israel': ('Iisrael', 'https://coda-israel.org.il'),
    'coda-nl': ('Holland', 'https://www.codependents-anonymous.nl'),
    'divulgacion': ('Hispaania Outreach', 'https://divulgacioncoda.org'),
    'fincoda': ('Soome (FinCoda)', 'http://fincoda.blogspot.com'),
    'helsinki': ('Soome (Helsinki)', 'http://codahelsinki.blogspot.com'),
    'estonia': ('Eesti (vana leht)', 'https://codaestonia.wordpress.com'),
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
        return None

def main():
    lighthouse_dir = Path('/home/d0021/Automation/coda/lighthouse-testid')

    results = {}

    # Collect all results
    for site_key, (country, url) in SITE_MAP.items():
        # Try desktop
        desktop_file = lighthouse_dir / f'{site_key}-desktop.json'
        desktop_retry_file = lighthouse_dir / f'{site_key}-desktop-retry.json'

        # Prefer retry file if it exists
        if desktop_retry_file.exists():
            desktop_scores = parse_lighthouse_json(desktop_retry_file)
        elif desktop_file.exists():
            desktop_scores = parse_lighthouse_json(desktop_file)
        else:
            desktop_scores = None

        # Try mobile
        mobile_file = lighthouse_dir / f'{site_key}-mobile.json'
        mobile_scores = parse_lighthouse_json(mobile_file) if mobile_file.exists() else None

        if desktop_scores or mobile_scores:
            results[country] = {
                'url': url,
                'desktop': desktop_scores,
                'mobile': mobile_scores
            }

    # Sort by mobile performance (or desktop if mobile not available)
    def sort_key(item):
        country, data = item
        if data['mobile']:
            return data['mobile']['performance']
        elif data['desktop']:
            return data['desktop']['performance']
        return 0

    sorted_results = sorted(results.items(), key=sort_key, reverse=True)

    print("=" * 100)
    print("LIGHTHOUSE TULEMUSED - DESKTOP JA MOBILE")
    print("=" * 100)
    print()

    for country, data in sorted_results:
        print(f"{country} - {data['url']}")
        if data['desktop']:
            d = data['desktop']
            print(f"  Desktop:  Perf: {d['performance']:3d} | Acc: {d['accessibility']:3d} | BP: {d['best_practices']:3d} | SEO: {d['seo']:3d}")
        else:
            print(f"  Desktop:  [Ei testitud]")

        if data['mobile']:
            m = data['mobile']
            print(f"  Mobile:   Perf: {m['performance']:3d} | Acc: {m['accessibility']:3d} | BP: {m['best_practices']:3d} | SEO: {m['seo']:3d}")
        else:
            print(f"  Mobile:   [Ei testitud]")
        print()

    print("=" * 100)
    print("TOP 3 - MOBILE PERFORMANCE")
    print("=" * 100)
    mobile_results = [(c, d) for c, d in sorted_results if d['mobile']]
    for i, (country, data) in enumerate(mobile_results[:3], 1):
        m = data['mobile']
        print(f"{i}. {country}: Performance {m['performance']}, Accessibility {m['accessibility']}")

    print()
    print("=" * 100)
    print("TOP 3 - MOBILE ACCESSIBILITY")
    print("=" * 100)
    mobile_by_acc = sorted(mobile_results, key=lambda x: x[1]['mobile']['accessibility'], reverse=True)
    for i, (country, data) in enumerate(mobile_by_acc[:3], 1):
        m = data['mobile']
        print(f"{i}. {country}: Accessibility {m['accessibility']}, Performance {m['performance']}")

    print()
    print("=" * 100)
    print("HALVIMAD - MOBILE PERFORMANCE")
    print("=" * 100)
    for i, (country, data) in enumerate(reversed(mobile_results[-3:]), 1):
        m = data['mobile']
        print(f"{i}. {country}: Performance {m['performance']}, Accessibility {m['accessibility']}")

if __name__ == '__main__':
    main()
