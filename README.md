# 555185.com: red envelopes and Chinese number codes

**555 (呜呜呜, crying) → 185 (要发我, prosperity to me).** This is a static, monetisable hub for red-envelope (hongbao) etiquette and Chinese number meanings. It includes:
- 7 free tools
- 57 number-meaning pages
- 9 guides
- a multi-form lead generation hub
- donation, contest, career, advertising and video pages
- legal pages

It runs on the **GitHub Pages free plan**: plain HTML, CSS and JS, with no build step needed on the server.

## Structure
```
index.html                 home
quote.html                 lead generation hub (corporate gifting, weddings, market pricing, free plan, suppliers)
donate.html · contests.html · careers.html · advertise.html · videos.html
the-555185-story.html · about.html · contact.html · legal.html · privacy.html · terms.html · thank-you.html · 404.html
tools/       7 interactive tools + hub
meanings/    10 digits + 47 number codes + searchable dictionary
guides/      9 guides + hub
assets/css/style.css     design system (light and dark)
assets/js/config.js      ← the ONLY file to edit for AdSense, GA4, YouTube and donation links
assets/js/numbers.js     number engine (luck score, decoder, lucky amounts, 大写, zodiac)
assets/js/tools.js       tool user interfaces
assets/js/app.js         nav, theme, forms, ads, video, modal, countdown
assets/js/numdata.js     generated from _src/numdata.py
assets/data/cny.json     Lunar New Year dates 1920–2045
_src/ + build.py         page sources → `python3 build.py` regenerates every page and sitemap.xml
project-docs/            RESEARCH.md (findings and decision) · BUILD-PROMPTS.md (phase-wise prompts)
```

## Publish on GitHub Pages
In **Settings → Pages**, under **Build and deployment**, choose **Deploy from a branch**, then branch `main` and folder `/ (root)`, and save.
The site goes live at `https://webworksa1.github.io/555185-com/` because all links are relative.

## Go-live checklist
1. **Forms.** Submit any form once. FormSubmit sends a one-time activation email to the site inbox; click **Activate Form**. After that, every form is delivered there. The address never appears on the site: it is assembled at runtime from an obfuscated array in `config.js`.
2. **AdSense.** Once approved, set `ADSENSE_CLIENT` (and optional slot IDs) in `assets/js/config.js` and replace the placeholder in `ads.txt`. Until then, ad slots show house ads that promote quotes, sponsorship, donations and contests.
3. **Donations.** Add PayPal.me, Stripe Payment Link, Ko-fi, Buy Me a Coffee or GitHub Sponsors URLs to `DONATE` in `config.js`. Empty ones stay hidden, and the pledge form always works.
4. **Analytics and YouTube.** Set `GA4_ID` and `YOUTUBE_CHANNEL` in `config.js`.
5. **Custom domain.**
   - Add a file named `CNAME` containing `555185.com`.
   - At the registrar, create A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`, plus a `www` CNAME pointing to `webworksa1.github.io`.
   - Turn on **Enforce HTTPS**.
6. Submit `https://555185.com/sitemap.xml` in Google Search Console.

## Edit content
Edit `_src/*.py`, then run `python3 build.py` and commit. Lunar New Year data: `pip install lunardate` then
`python3 -c "from lunardate import LunarDate as L;import json;json.dump({y:L(y,1,1).to_solar_date().isoformat() for y in range(1920,2046)},open('assets/data/cny.json','w'))"`

## Legal
"555185" is used only as a descriptive numeral string. No trademark is claimed, and the site is not affiliated with anyone else who uses the digits. See `legal.html`.
