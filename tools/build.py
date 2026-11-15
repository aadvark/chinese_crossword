"""Build targets from the single source page in www/.

web      -> www/ is published as is (Google Fonts link kept as a fallback).
android  -> dist/android-www/: same files, minus the Google Fonts links,
            so the app never touches the network (fonts are bundled in www/fonts).
"""
import re, shutil, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
target = sys.argv[1] if len(sys.argv) > 1 else 'web'
if target == 'android':
    out = ROOT / 'dist' / 'android-www'
    if out.exists(): shutil.rmtree(out)
    shutil.copytree(ROOT / 'www', out)
    html = (out / 'index.html').read_text(encoding='utf-8')
    html, n = re.subn(r'<link[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>\n?', '', html)
    (out / 'index.html').write_text(html, encoding='utf-8')
    print(f'android web assets -> {out} (removed {n} Google Fonts links)')
else:
    print('web: publish www/ as is')
