# 妙语连珠 · Chinese crossword

An endless Chinese crossword of 成语, 俗语, 谚语 and 歇后语, made for parents to keep their minds sharp.
Each solved phrase pops up its meaning and is read aloud, and every phrase learned is kept in 已学 for review.

- **Endless levels**: puzzles are generated from 1,024 phrases, new phrases first; difficulty keeps rising slowly.
- **简体 / 繁體**: chosen on first play, changeable in 设置 (converted with OpenCC).
- **Four seasons of 山水画** backgrounds, guzheng-style music, large tap targets, three difficulty levels.
- **Free, no ads, no data collected, works offline.**

## Download

- **Website:** https://aadvark.github.io/chinese_crossword/ (landing page; play in the browser at https://aadvark.github.io/chinese_crossword/www/)
- **Android:** [miaoyulianzhu.apk](https://github.com/aadvark/chinese_crossword/raw/main/apk/miaoyulianzhu.apk) (v1.2, Android 7.0+). Install steps in [apk/README.md](apk/README.md).

## Layout

```
landing/             Bilingual landing page (EN / 简 / 繁); build with tools/build_landing.py
www/                 The game: one page (index.html) + bg/ paintings + fonts/ (trimmed woff2)
android/             Capacitor Android project (com.kithandkeen.miaoyulianzhu, targets API 36)
apk/                 Signed Android APK for direct download
assets/              Icon and splash sources (generated into android/ by @capacitor/assets)
tools/build.py       Build targets: web (www/ as is) and android (offline copy, no Google Fonts)
tools/subset_fonts.py  Re-trim fonts after changing phrases or UI text (source TTFs not committed)
tools/data*.txt      Phrase lists with meanings (simplified; traditional is generated)
```

## Web

`www/` is a static site; open `www/index.html` or host the folder anywhere.
`landing/` is the landing page, served by GitHub Pages from `main` (root `index.html` redirects to it). On GitHub Pages its Play buttons open `../www/`; elsewhere the published claude.ai game link.

## Android

Needs Node 22+, JDK 21 and the Android SDK (API 36).

```
npm install
npm run build:android        # copies www/ to dist/android-www and syncs into android/
cd android && ./gradlew assembleDebug
```

On Android the page detects Capacitor and uses native text-to-speech, the back button,
haptics and keep-screen-on. The app has no internet permission.

## Credits

- Fonts: Noto Serif SC, Ma Shan Zheng, LXGW WenKai TC (SIL Open Font License), from google/fonts.
- Traditional conversion: OpenCC.
- Concept and direction: Lee Wen Yang (Mike) · Kith + Keen.
