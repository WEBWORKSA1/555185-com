# 555185.com: build prompts, phase by phase

These prompts rebuild or extend the site with any capable AI coding assistant. Run them in order. Each one assumes the previous phases are done.

**Global constraints (paste these at the top of every phase):**
- **Domain and concept.** The domain is 555185.com. The site is a red envelope (hongbao) and Chinese number-code hub, built around the story "555 = 呜呜呜 (crying) → 185 = 要发我 (prosperity to me)".
- **Hosting.** Static HTML, CSS and vanilla JS only, deployable on the GitHub Pages free plan. No server code. Include a `.nojekyll` file.
- **Top bar on every page.** Show this text: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership". Link it to https://web.works/contact.
- **Email handling.** All forms and email links go to ONE private inbox. The address must NEVER appear in HTML, text or the README. Store it obfuscated in `assets/js/config.js` (reversed char codes plus an offset). Assemble it only at runtime, either as the FormSubmit AJAX endpoint or a `mailto:` link that is built when the user clicks.
- **Trademark wording.** No trademark claims on "555185". Use it only as a descriptive numeral string. Include a full trademark and copyright disclosure page.
- **Design.** Mobile-first and responsive with no horizontal scroll at 375px. Light and dark themes. WCAG AA contrast. Relative links, so the site works both at `/555185-com/` and at the domain root.

---

## Phase 1: Foundation and design system
> Create the repo skeleton for 555185.com:
> - `assets/css/style.css`: a design system with these tokens:
>   - red `#C8102E`, gold `#C9A227`, jade, ink, paper `#FBF7F0`
>   - a dark-mode token set applied via `prefers-color-scheme` and `[data-theme]`
>   - Playfair Display headings, Inter body text, and a CJK font stack
> - Components:
>   - the sticky header with a mobile hamburger menu, plus the top bar described above
>   - cards and grids (2, 3 and 4 columns, collapsing on mobile), buttons (primary, gold, ghost)
>   - forms with chips, multi-step forms with a progress bar, tabs
>   - tool result panels, number "digit tiles", tables wrapped for horizontal scroll, FAQ `<details>`
>   - countdown, modal, sticky bottom CTA, ad slots, YouTube facade, footer
> - `build.py` plus a `_src/` folder of Python modules. A `page()` layout function outputs complete HTML documents with:
>   - title, meta description, canonical, Open Graph, Twitter card and JSON-LD (WebSite + BreadcrumbList)
>   - the top contact bar, header and nav, footer with newsletter, trademark note, lead-magnet modal and sticky CTA
>   - script includes
> - `config.js` holding: ADSENSE_CLIENT, ad slots, GA4_ID, YOUTUBE_CHANNEL, DONATE links (paypal, kofi, buymeacoffee, stripe, github) and the obfuscated inbox.

## Phase 2: Number engine and data
> Write `_src/numdata.py` with all ten digits. For each digit give pinyin, character, sound-alikes, luck class and a cultural note. Add 45+ number codes, each with: number, Chinese reading, pinyin, English meaning, luck class (lucky / love / slang / unlucky / mixed / neutral), category, description, example sentence and translation. Include at least: 555, 5555, 185, 555185, 520, 521, 1314, 5201314, 530, 3344, 9420, 770, 7758258, 88, 886, 666, 233, 748, 7456, 995, 94, 9494, 484, 584, 514, 14, 250, 13, 286, 51, 518, 168, 1688, 188, 888, 8888, 99, 999, 66, 18, 0437. Label 185 and 555185 honestly as constructed readings, not established slang.
>
> `build.py` emits `assets/js/numdata.js`. Then write `assets/js/numbers.js` with these pure functions:
> - `luck(str)`: a 0–100 score with explanatory notes. Scoring rules:
>   - 8 = +3; 6 and 9 = +2; 4 = −4
>   - 250 gives a penalty, and so do 14 and 74
>   - bonuses for famous sequences, repeating triples and an 8 ending
>   - love codes are exempt from the 4 penalty
> - `decode(str)`: longest-match, non-overlapping detection of slang codes, plus a digit breakdown.
> - `luckyAmounts(target, {parity, lo, hi})`: candidate amounts near the target with:
>   - no 4, no 250, the requested parity
>   - weighting toward 6, 8 and 9 and known lucky amounts
>   - penalties for "messy" digits and for distance from the target
> - `daxie(amount, {cur: CNY|HKD|TWD|none, trad, prefix})`: correct 大写 financial numerals with:
>   - grouping by 万 and 亿, and zero-collapsing rules
>   - units 元角分 (CNY) or 圓毫仙 (HKD), ending in 整
> - `lowerZh` (everyday Chinese numerals), `zodiacYear`, and `zodiacForDate` using a Lunar New Year date table for 1920–2045 (generate it with the `lunardate` Python package).

## Phase 3: Seven interactive tools (tools/*.html)
> Build each tool page with this layout: hero, then the tool card, then an ad, then SEO explainer content, then an FAQ (with FAQPage JSON-LD and WebApplication JSON-LD), then related tools. The sidebar holds a lead form, popular tools, an ad and a quote CTA.
> 1. **Red Envelope Planner.**
>    - Inputs: region (CN, HK, TW, SG, MY, US/CA, UK, AU) and generosity level.
>    - A dynamic recipient list with type × quantity rows (friends' kids, nieces/nephews, own children, parents, unmarried adults, employees, service staff).
>    - Uses indicative ranges per region. Outputs a lucky amount per envelope, alternative amounts, the total budget and the total in 大写. Includes a married-couple note for HK, SG and MY.
>    - CTAs: "email me this plan" and "corporate quote".
> 2. **Wedding Red Envelope Calculator.**
>    - Inputs: region, venue tier (which sets a default editable cost per seat), party size, closeness multiplier, attending or not.
>    - Outputs a lucky even amount with alternatives, the calculation shown step by step, and the amount in 大写.
>    - CTA: wedding vendor match.
> 3. **Number Code Decoder.** Digit tiles, luck score bar, notes, slang matches linking to meaning pages and a digit-by-digit list. Supports `?n=` and "try" chips.
> 4. **大写 Converter.** Currency style, Traditional toggle, prefix toggle, copy button, everyday numerals and a reference table.
> 5. **Lucky Amount and Price Finder.** Modes for gift (even), retail price and condolence (odd). The price mode links to the Chinese-market pricing lead form.
> 6. **Greetings Generator.** Thirty blessings across categories (New Year, Year of the Goat 2027, wedding, birthday, business, baby, exams). Includes a random pick, a copy button and a 1080×1350 PNG card download drawn on canvas.
> 7. **Zodiac Finder and CNY Countdown.** A live countdown to 2027-02-06, sign plus element plus yin/yang adjusted for the New Year date, and a table of the next 10 years.

## Phase 4: Programmatic meaning pages (meanings/)
> Generate `meanings/index.html` with a live search filter and a grid of digits and codes, carrying DefinedTermSet JSON-LD. For every digit and every code, generate a page with:
> - an H1 "What does N mean in Chinese?"
> - digit tiles, the reading, the description, an example quote, and a gift-safety verdict by luck class
> - a digit breakdown table, a decoder deep link, related codes and a three-question FAQ with FAQPage JSON-LD
>
> The pages for 555, 185 and 555185 link to the story page.

## Phase 5: Pillar guides (guides/)
> Write 8 long-form guides. Each needs: a table of contents, amount tables, internal links to tools and meaning pages, an FAQ with JSON-LD, ad slots and a lead-generation band. The guides are:
> - red envelope etiquette (pillar)
> - the Chinese wedding red envelope guide: guest gift 礼金, door games, tea ceremony, 改口费, betrothal 聘金
> - amounts by region
> - digital red packets (WeChat, Alipay)
> - number slang
> - lucky and unlucky numbers
> - the corporate CNY gifting guide (B2B lead generation)
> - 12 red envelope mistakes
> - the Lunar New Year 2027 planner
>
> Also write a guides hub and "The 555185 story" page.

## Phase 6: Lead generation (quote.html), the main revenue page
> Build a tabbed lead hub. Tab state is linkable via hash: `#corporate`, `#wedding`, `#market`, `#plan`, `#vendor`.
> - **Corporate gifting.** A 3-step form:
>   1. Products (multi-select chips), quantity band and deadline.
>   2. Finish, budget, artwork URL, notes, company and job title.
>   3. Contact details, region, source and a required consent box.
> - **Wedding vendor match.** A 3-step form covering event, date, city, guests, services (chips), style, budget and contact details.
> - **Chinese-market pricing and localisation.** A 2-step form.
> - **Free hongbao plan.** A single-step email capture.
> - **Supplier listing application.**
>
> Add trust bullets, a "how it works" section in 3 steps, an FAQ, and a sidebar on order lead times. Every form has a honeypot field, posts as JSON to FormSubmit AJAX using the runtime-assembled inbox, fires a GA4 `generate_lead` event, and redirects to `thank-you.html`. On failure, show a fallback `mailto:` link that is built only when clicked. Add a site-wide exit-intent modal (desktop only, once per session) offering the "2027 red-envelope cheat sheet", plus a dismissible sticky mobile CTA.

## Phase 7: Monetisation pages
> - **donate.html.**
>   - Lucky tiers: $8.88, $18.88 (most popular), $88, $188.
>   - Payment buttons driven by config, each hidden when its link is empty.
>   - A pledge form as fallback: amount, frequency, allocation, message, public-credit opt-in.
>   - Bars showing the fund allocation: operations 30%, content 25%, hiring talent 20%, contests and prizes 15%, promotion 10%.
>   - Supporter perks and an FAQ stating that donations are not tax-deductible.
> - **contests.html.**
>   - Three contests: Red Envelope Design ($888 pool), Greeting Video ($500) and Lucky Number Story ($300).
>   - A deadline countdown and an entry form (link-based uploads).
>   - Rules: no purchase necessary, original work only, no trademarks, AI disclosure, judging weights, void where prohibited.
>   - A prize-sponsorship CTA.
> - **careers.html.** Seven remote roles and an application form.
> - **advertise.html.**
>   - Four packages: seasonal takeover, sponsored tool, directory and leads, content partnership.
>   - Audience, peak-intent and brand-safety cards.
>   - A brief form, plus a web.works/contact button.
> - **videos.html.** A YouTube privacy-enhanced facade (thumbnail first, iframe loads on click), with 13 verified video IDs grouped by topic and a creator credit and takedown note.
> - **Ads.** Place `.ad[data-slot]` slots (top, inarticle, sidebar, footer). When `ADSENSE_CLIENT` is set, inject the AdSense script and `<ins>` units. Otherwise rotate labelled house ads that promote quotes, vendors, sponsorship, donations and contests.

## Phase 8: Trust, legal and SEO
> - about, contact (form, a click-to-email link that never displays the address, and a web.works/contact card)
> - legal (trademark disclosure, copyright, takedown process, information disclaimer, advertising and affiliate disclosure, domain enquiries)
> - privacy (FormSubmit, GA4, AdSense cookies, YouTube, GDPR, CCPA, PIPEDA rights) and terms
> - thank-you and a 404 page that fixes its `<base>` at runtime for project-path hosting
> - sitemap.xml with lastmod and priority values, robots.txt, ads.txt placeholder, web manifest, an SVG favicon and a 1200×630 Open Graph image

## Phase 9: Quality assurance
> Use Playwright on Chromium to check:
> - Every page loads with 0 JS errors.
> - No page is wider than 375px at a 375px viewport.
> - The tool outputs are correct, including the 大写 edge cases 20000.3, 100.05, 10005 and 100000010, and zodiac dates around New Year.
>
> Then grep the whole repo to confirm the inbox address appears nowhere in plain text, and click through the forms.

## Phase 10: Deploy and grow
> 1. Push to `WEBWORKSA1/555185-com` (main branch).
> 2. In Settings → Pages, choose Deploy from a branch → main → / (root).
> 3. Submit the first form once and click FormSubmit's activation email.
> 4. Custom domain: add a `CNAME` file containing `555185.com`. At the registrar, create A records 185.199.108.153, .109.153, .110.153 and .111.153, plus a `www` CNAME pointing to `webworksa1.github.io`. Then turn on Enforce HTTPS.
> 5. Apply for AdSense, then fill in `config.js` and `ads.txt`.
> 6. Submit the sitemap to Google Search Console.
> 7. **Growth roadmap:**
>    - Launch a YouTube Shorts series ("Decode a number in 15 seconds").
>    - Before 15 November, publish CNY landing pages for HK, SG, MY, Vancouver, Toronto and Sydney.
>    - Add Simplified and Traditional Chinese versions with hreflang.
>    - Sell printable red-envelope templates.
>    - Sign up supplier partners for paid lead delivery.
>    - Publish 520 Day and Qixi campaign pages in April and July.
