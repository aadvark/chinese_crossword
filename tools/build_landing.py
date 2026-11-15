"""Build landing/index.html from landing/src/template.html + strings.json.
繁體 strings are generated from 简体 with OpenCC (pip install opencc-python-reimplemented)."""
import json, pathlib, opencc
ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = 'https://claude.ai/artifact/2U8ZtL2ZL4TXFYvVh7JvN1'
cc = opencc.OpenCC('s2t')
strings = json.loads((ROOT / 'landing/src/strings.json').read_text(encoding='utf-8'))
for v in strings.values():
    v['t'] = cc.convert(v['s'])
def seal(size, uid):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true" style="transform:rotate(-6deg);flex:none">'
            f'<defs><filter id="w{uid}" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="7" result="n"/>'
            f'<feDisplacementMap in="SourceGraphic" in2="n" scale="2.6"/></filter><radialGradient id="p{uid}" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#fffbe6"/>'
            f'<stop offset=".5" stop-color="#ecc361"/><stop offset="1" stop-color="#a8741a"/></radialGradient></defs><g filter="url(#w{uid})"><rect x="4" y="4" width="56" height="56" rx="7" fill="#b8321f"/>'
            f'<rect x="9" y="9" width="46" height="46" rx="4" fill="none" stroke="#fbe9d0" stroke-width="2.2"/><text x="32" y="46" text-anchor="middle" font-family="Ma Shan Zheng, serif" font-size="38" fill="#fbe9d0">妙</text></g>'
            f'<circle cx="56" cy="56" r="7" fill="url(#p{uid})" stroke="#8a5a10" stroke-width=".6"/></svg>')
html = (ROOT / 'landing/src/template.html').read_text(encoding='utf-8')
html = (html.replace('__I18N__', json.dumps(strings, ensure_ascii=False)).replace('__APP__', APP)
            .replace('__SEAL40__', seal(40, 'a')).replace('__SEAL44__', seal(44, 'b')).replace('__SEAL64__', seal(64, 'c')))
assert '__' not in html.replace('__proto__', '')
(ROOT / 'landing/index.html').write_text(html, encoding='utf-8')
print('landing/index.html built,', len(strings), 'strings × 3 languages')
