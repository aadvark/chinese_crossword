"""Re-trim the bundled fonts to exactly the characters in www/index.html.
Run after changing phrases or UI text. Needs: pip install fonttools brotli
Source fonts (OFL) from github.com/google/fonts: put them in tools/fonts-src/.
"""
import subprocess, pathlib
from fontTools.varLib import instancer
from fontTools.ttLib import TTFont
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'tools' / 'fonts-src'
html = (ROOT / 'www' / 'index.html').read_text(encoding='utf-8')
chars = {c for c in html if ord(c) > 127} | {chr(i) for i in range(32, 127)} | set('，。！？、：；“”‘’（）《》·—…')
(SRC / 'chars.txt').write_text(''.join(sorted(chars)), encoding='utf-8')
noto = instancer.instantiateVariableFont(TTFont(SRC / 'NotoSerifSC[wght].ttf'), {'wght': (500, 900)})
noto.save(SRC / 'noto-limited.ttf')
def sub(src, out, **kw):
    args = ['pyftsubset', str(src), '--flavor=woff2', '--layout-features=*', '--no-hinting', f'--output-file={ROOT / "www" / "fonts" / out}']
    args.append(f'--text-file={SRC / "chars.txt"}' if 'all' in kw else f'--text={kw["text"]}')
    subprocess.run(args, check=True)
sub(SRC / 'noto-limited.ttf', 'noto-serif-sc.woff2', all=True)
sub(SRC / 'MaShanZheng-Regular.ttf', 'ma-shan-zheng.woff2', text='妙语连珠')
sub(SRC / 'LXGWWenKaiTC-Bold.ttf', 'lxgw-wenkai-tc.woff2', text='妙語連珠')
print('fonts re-trimmed for', len(chars), 'characters')
