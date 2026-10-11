import glob
import re
from collections import Counter, defaultdict

def audit():
    files = glob.glob('articles/*.html')
    print(f"Auditing {len(files)} files...")
    paras = Counter()
    para_files = defaultdict(list)
    h2s = Counter()
    h2_files = defaultdict(list)
    
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        
        # Extract body between article-meta-bar and footnote-section
        if '<div class="article-meta-bar">' in content and '<section class="footnote-section">' in content:
            body = content.split('<div class="article-meta-bar">')[1].split('<section class="footnote-section">')[0]
            # Paragraphs
            for p in re.findall(r'<p>(.*?)</p>', body, re.DOTALL):
                clean = ' '.join(re.sub(r'<[^>]+>', '', p).split())
                if len(clean) > 30:
                    paras[clean] += 1
                    para_files[clean].append(f)
            # H2s
            for h in re.findall(r'<h2>(.*?)</h2>', body, re.DOTALL):
                clean = ' '.join(re.sub(r'<[^>]+>', '', h).split())
                h2s[clean] += 1
                h2_files[clean].append(f)

    dups = [(text, count, para_files[text]) for text, count in paras.items() if count > 1]
    print(f"\nTotal duplicated paragraphs in body: {len(dups)}")
    for text, count, flist in sorted(dups, key=lambda x: x[1], reverse=True)[:15]:
        print(f"[{count} files] {text[:90]}...")
        print(f"   Example: {flist[0]}")

    dup_h2s = [(text, count, h2_files[text]) for text, count in h2s.items() if count > 1]
    print(f"\nTotal duplicated H2 headings: {len(dup_h2s)}")
    for text, count, flist in sorted(dup_h2s, key=lambda x: x[1], reverse=True)[:10]:
        print(f"[{count} files] H2: {text}")
        print(f"   Example: {flist[0]}")

if __name__ == '__main__':
    audit()
