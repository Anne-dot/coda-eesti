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
    lighthouse_dir = Path('/home/d0021/Automation/coda/research/lighthouse-tests')

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

    # MOBILE KATEGOORIA
    print("=" * 100)
    print("MOBILE - TOP 3 PERFORMANCE")
    print("=" * 100)
    mobile_results = [(c, d) for c, d in sorted_results if d['mobile']]
    mobile_by_perf = sorted(mobile_results, key=lambda x: x[1]['mobile']['performance'], reverse=True)
    for i, (country, data) in enumerate(mobile_by_perf[:3], 1):
        m = data['mobile']
        print(f"{i}. {country}: Performance {m['performance']}, Accessibility {m['accessibility']}")

    print()
    print("=" * 100)
    print("MOBILE - TOP 3 ACCESSIBILITY")
    print("=" * 100)
    mobile_by_acc = sorted(mobile_results, key=lambda x: x[1]['mobile']['accessibility'], reverse=True)
    for i, (country, data) in enumerate(mobile_by_acc[:3], 1):
        m = data['mobile']
        print(f"{i}. {country}: Accessibility {m['accessibility']}, Performance {m['performance']}")

    print()
    print("=" * 100)
    print("MOBILE - BOTTOM 3 PERFORMANCE")
    print("=" * 100)
    for i, (country, data) in enumerate(reversed(mobile_by_perf[-3:]), 1):
        m = data['mobile']
        print(f"{i}. {country}: Performance {m['performance']}, Accessibility {m['accessibility']}")

    print()
    print("=" * 100)
    print("MOBILE - BOTTOM 3 ACCESSIBILITY")
    print("=" * 100)
    for i, (country, data) in enumerate(reversed(mobile_by_acc[-3:]), 1):
        m = data['mobile']
        print(f"{i}. {country}: Accessibility {m['accessibility']}, Performance {m['performance']}")

    # DESKTOP KATEGOORIA
    print()
    print("=" * 100)
    print("DESKTOP - TOP 3 PERFORMANCE")
    print("=" * 100)
    desktop_results = [(c, d) for c, d in sorted_results if d['desktop']]
    desktop_by_perf = sorted(desktop_results, key=lambda x: x[1]['desktop']['performance'], reverse=True)
    for i, (country, data) in enumerate(desktop_by_perf[:3], 1):
        d = data['desktop']
        print(f"{i}. {country}: Performance {d['performance']}, Accessibility {d['accessibility']}")

    print()
    print("=" * 100)
    print("DESKTOP - BOTTOM 3 PERFORMANCE")
    print("=" * 100)
    for i, (country, data) in enumerate(reversed(desktop_by_perf[-3:]), 1):
        d = data['desktop']
        print(f"{i}. {country}: Performance {d['performance']}, Accessibility {d['accessibility']}")

    # KOKKUVÕTE
    print()
    print("=" * 100)
    print("KOKKUVÕTE - TOP 3 ÜLDINE (keskmine desktop + mobile performance)")
    print("=" * 100)
    # Arvuta keskmine performance
    overall = []
    for country, data in results.items():
        desktop_perf = data['desktop']['performance'] if data['desktop'] else 0
        mobile_perf = data['mobile']['performance'] if data['mobile'] else 0
        # Kui mõlemad olemas, keskmine; kui üks, siis see
        if data['desktop'] and data['mobile']:
            avg = (desktop_perf + mobile_perf) / 2
        elif data['desktop']:
            avg = desktop_perf
        elif data['mobile']:
            avg = mobile_perf
        else:
            avg = 0
        overall.append((country, avg, data))

    overall.sort(key=lambda x: x[1], reverse=True)

    for i, (country, avg, data) in enumerate(overall[:3], 1):
        d_perf = data['desktop']['performance'] if data['desktop'] else 'N/A'
        m_perf = data['mobile']['performance'] if data['mobile'] else 'N/A'
        print(f"{i}. {country}: Keskmine {avg:.1f} (Desktop: {d_perf}, Mobile: {m_perf})")

    print()
    print("=" * 100)
    print("KOKKUVÕTE - BOTTOM 3 ÜLDINE (keskmine desktop + mobile performance)")
    print("=" * 100)
    for i, (country, avg, data) in enumerate(reversed(overall[-3:]), 1):
        d_perf = data['desktop']['performance'] if data['desktop'] else 'N/A'
        m_perf = data['mobile']['performance'] if data['mobile'] else 'N/A'
        print(f"{i}. {country}: Keskmine {avg:.1f} (Desktop: {d_perf}, Mobile: {m_perf})")

if __name__ == '__main__':
    main()
