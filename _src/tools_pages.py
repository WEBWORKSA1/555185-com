from layout import page, ad, sidebar, faq_html, faq_ld, esc, UPDATED

REGION_OPTS = ""  # filled by JS

def tool_page(path, title, h1, desc, intro, tool_html, content, faqs, name):
    r = "../"
    ld = [faq_ld(faqs), {"@context": "https://schema.org", "@type": "WebApplication", "name": name, "applicationCategory": "UtilitiesApplication",
                         "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": "https://555185.com/" + path}]
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Free tool</span><h1>{h1}</h1><p class="lead">{intro}</p></div>
<div class="wrap layout"><div class="prose">{tool_html}{ad("inarticle")}{content}<h2 id="faq">FAQ</h2>{faq_html(faqs)}
<h2>More free tools</h2><div class="grid g2">{related(r, path)}</div>{ad("footer")}</div>{sidebar(r)}</div>'''
    return path, page(path, title, desc, body, crumbs=[("tools/", "Tools"), ("", name)], ld=ld)

TOOLS = [
 ("tools/hongbao-calculator.html", "🧧", "Red Envelope Planner", "Budget every hongbao on your list, by region and relationship."),
 ("tools/wedding-red-envelope-calculator.html", "💍", "Wedding Red Envelope Calculator", "How much to give at a Chinese wedding — by city, venue and closeness."),
 ("tools/number-code-decoder.html", "🔢", "Number Code Decoder", "Decode 555, 520, phone numbers and plates — slang, homophones, luck score."),
 ("tools/chinese-financial-numerals.html", "壹", "大写 Financial Numeral Converter", "Write amounts in formal Chinese for cheques, invoices and envelopes."),
 ("tools/lucky-amount-finder.html", "💰", "Lucky Amount & Price Finder", "Snap any budget or price to the luckiest nearby number."),
 ("tools/greetings-generator.html", "🎊", "Chinese Greetings Generator", "New Year, wedding and business blessings with pinyin + share cards."),
 ("tools/zodiac-cny-countdown.html", "🐐", "Zodiac Finder & CNY Countdown", "Your true zodiac sign and the countdown to Lunar New Year 2027."),
]

def related(r, skip):
    return "".join(f'<a class="card" href="{r}{p}"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p></a>' for p, i, n, d in TOOLS if p != skip)[:100000]

def build():
    out = []
    # hub
    cards = "".join(f'<a class="card" href="../{p}"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p></a>' for p, i, n, d in TOOLS)
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Free tools</span><h1>Red envelope &amp; number tools</h1><p class="lead">Seven free calculators and decoders for Lunar New Year, Chinese weddings, lucky pricing and number slang. No sign-up, works on any phone.</p></div>
<div class="wrap"><div class="grid g3">{cards}<a class="card" href="../quote.html" style="border-color:var(--red)"><div class="ico">🏢</div><h3>Corporate CNY gifting</h3><p>100+ custom-printed envelopes or gift boxes? Get free supplier quotes.</p></a></div>{ad("footer")}</div>'''
    out.append(("tools/index.html", page("tools/index.html", "Free Red Envelope & Chinese Number Tools | 555185", "Free hongbao planner, Chinese wedding gift calculator, number code decoder, 大写 converter, lucky amount finder, greetings generator and zodiac finder.", body, crumbs=[("", "Tools")])))

    out.append(tool_page("tools/hongbao-calculator.html",
     "Red Envelope (Hongbao) Amount Calculator 2027 — How Much to Give | 555185",
     "Red envelope planner: how much to put in a hongbao",
     "Free hongbao calculator: how much money to put in red envelopes for kids, parents, employees and staff in China, Hong Kong, Taiwan, Singapore, Malaysia, US, UK and Australia.",
     "Add everyone on your list, pick your region and generosity level — we suggest a lucky amount per envelope (no 4s, no 250) and your total budget.",
     '''<div class="tool" id="hb-tool"><div class="row2"><div><label for="hb-region">Where are you giving?</label><select id="hb-region"></select></div>
<div><label for="hb-level">Generosity</label><select id="hb-level"><option value="0">Modest</option><option value="0.45" selected>Typical</option><option value="0.85">Generous</option><option value="1">Very generous</option></select></div></div>
<div style="margin-top:14px"><label>Who are you giving to? <span class="muted">(type · how many)</span></label><div id="hb-list"></div>
<button type="button" class="btn sm ghost" id="hb-add">+ Add recipient</button></div>
<label class="check" style="margin-top:12px"><input type="checkbox" id="hb-married"> I’m married (married couples are expected to give)</label>
<button type="button" class="btn" id="hb-go" style="margin-top:14px">Calculate my red envelopes</button><div class="result" id="hb-out" aria-live="polite"></div></div>''',
     '''<h2>How the planner decides an amount</h2><p>Each recipient type has an indicative range for your region, drawn from widely published etiquette guides (e.g. ¥100–200 for friends’ young children and ¥500–2,000 for parents in mainland China; S$8–10 for children in Singapore). Your generosity setting picks a point in that range, and the result is <b>snapped to the nearest lucky amount</b>: even, no digit 4, never 250, with extra weight for 6, 8 and 9.</p>
<div class="tbl"><table><thead><tr><th>Recipient</th><th>Mainland China</th><th>Hong Kong</th><th>Singapore</th><th>USA / Canada</th></tr></thead><tbody>
<tr><td>Friends’ young children</td><td>¥100–200</td><td>HK$20–50</td><td>S$8–10</td><td>$10–20</td></tr>
<tr><td>Nieces &amp; nephews</td><td>¥200–500</td><td>HK$50–100</td><td>S$10–28</td><td>$20–50</td></tr>
<tr><td>Own children</td><td>¥200–1,000</td><td>HK$100–500</td><td>S$20–88</td><td>$20–100</td></tr>
<tr><td>Parents &amp; grandparents</td><td>¥500–2,000</td><td>HK$500–2,000</td><td>S$100–888</td><td>$100–500</td></tr>
<tr><td>Employees</td><td>¥100–1,000</td><td>HK$50–200</td><td>S$10–50</td><td>$20–100</td></tr></tbody></table></div>
<p class="note">Indicative norms only — family custom, local cost of living and your relationship always come first. Hong Kong lai see for acquaintances are famously small; mainland amounts are larger.</p>
<h2>Five rules the calculator follows</h2><ol><li><b>No 4.</b> 四 (sì) sounds like 死 (death).</li><li><b>Even amounts</b> for happy occasions — good things come in pairs.</li><li><b>Avoid 250</b> — 二百五 means “idiot”.</li><li><b>Prefer 6, 8, 9</b> — smooth, prosperous, long-lasting.</li><li><b>New, crisp notes</b> in a red envelope; give and receive with both hands.</li></ol>
<p>Read the full <a href="../guides/red-envelope-etiquette.html">red envelope etiquette guide</a> or see <a href="../guides/how-much-to-give-by-region.html">amounts by country</a>.</p>''',
     [("How much money should I put in a red envelope?", "For children of friends, roughly ¥100–200 in mainland China, HK$20–50 in Hong Kong, S$8–10 in Singapore or $10–20 in North America. Parents and grandparents get the most (often ¥500–2,000). Always choose an even, lucky amount without the digit 4."),
      ("Do single adults give red envelopes?", "Traditionally, no — married people give to children and unmarried younger relatives. Working adults commonly give to parents and grandparents regardless of marital status."),
      ("Can I give red envelopes digitally?", "Yes. WeChat and Alipay digital red packets (launched in 2014) are now mainstream in mainland China, and e-lai see is common in Hong Kong. The same number rules apply."),
      ("Is 1,314 acceptable even though it has a 4?", "Yes. 1314 reads as 一生一世 (forever), so it’s a romantic exception used between couples and at weddings.")],
     "Red Envelope Planner"))

    out.append(tool_page("tools/wedding-red-envelope-calculator.html",
     "Chinese Wedding Red Envelope Calculator — How Much to Give (2027) | 555185",
     "Chinese wedding red envelope calculator",
     "How much to give at a Chinese wedding: calculate the right red envelope by city, banquet venue, closeness and number of guests. Lucky even amounts for China, HK, Taiwan, Singapore, Malaysia, US, UK.",
     "The classic rule: your gift should cover your seat at the banquet — then adjust for closeness. We do the maths and round to a lucky, even number.",
     '''<div class="tool" id="wd-tool"><div class="row2"><div><label for="wd-region">Wedding location</label><select id="wd-region"></select></div>
<div><label for="wd-tier">Banquet venue</label><select id="wd-tier"><option value="0">Restaurant / community hall</option><option value="1" selected>Mid-range hotel</option><option value="2">Luxury hotel / destination</option></select></div></div>
<div class="row2" style="margin-top:14px"><div><label for="wd-perhead">Estimated cost per seat (<span id="wd-cur"></span>)</label><input type="number" id="wd-perhead" min="1"></div>
<div><label for="wd-people">Guests in your party</label><input type="number" id="wd-people" value="1" min="1" max="12"></div></div>
<div class="row2" style="margin-top:14px"><div><label for="wd-close">Your relationship</label><select id="wd-close"><option value="0.9">Acquaintance / colleague</option><option value="1" selected>Friend</option><option value="1.3">Close friend</option><option value="1.5">Relative</option><option value="2.5">Close family</option></select></div>
<div><label for="wd-attend">Attending?</label><select id="wd-attend"><option value="yes">Yes, attending the banquet</option><option value="no">No, sending a gift only</option></select></div></div>
<button type="button" class="btn" id="wd-go" style="margin-top:14px">Calculate my wedding gift</button><div class="result" id="wd-out" aria-live="polite"></div></div>''',
     '''<h2>Common wedding amounts by region</h2><div class="tbl"><table><thead><tr><th>Region</th><th>Typical guest range</th><th>Local favourites</th></tr></thead><tbody>
<tr><td>Mainland China</td><td>¥600–2,000+ (higher in tier-1 cities)</td><td>¥666, ¥888, ¥1,314, ¥1,688</td></tr>
<tr><td>Hong Kong</td><td>Roughly the banquet cost per head, often HK$1,000–2,000</td><td>HK$1,088, HK$1,388, HK$1,688</td></tr>
<tr><td>Taiwan</td><td>NT$1,600–3,600</td><td>NT$1,600, 2,200, 2,600, 3,600, 6,600</td></tr>
<tr><td>Singapore</td><td>The venue’s “market rate” per guest, often S$120–250+</td><td>S$128, 168, 188, 228</td></tr>
<tr><td>USA / Canada</td><td>$100–300 per guest</td><td>$108, $128, $168, $188, $288</td></tr></tbody></table></div>
<p class="note">Indicative ranges compiled from published wedding etiquette guides (2025–2026). Venues and cities vary a lot — when unsure, ask a mutual friend what’s customary.</p>
<h2>Wedding envelope etiquette in one minute</h2><ul><li>Write your name (and a blessing like 百年好合, bǎi nián hǎo hé — “a hundred years of harmony”) on the envelope.</li><li>Hand it in at the reception table on arrival; it is usually logged by family.</li><li>Use new notes and an even total; avoid 4 anywhere.</li><li>Close family give much more — and the betrothal (聘金) and tea-ceremony envelopes follow different rules. See our <a href="../guides/chinese-wedding-red-envelope-guide.html">complete Chinese wedding red envelope guide</a>.</li></ul>''',
     [("How much should I give at a Chinese wedding?", "Aim to at least cover the cost of your seat at the banquet, then add more for closer relationships. That works out to roughly ¥600–2,000 in mainland China, HK$1,000–2,000 in Hong Kong, S$120–250 in Singapore and $100–300 in North America."),
      ("Should couples give one envelope or two?", "Usually one envelope from the couple, sized for two seats. In some Hong Kong and Macau families, each spouse gives separately for Lunar New Year — but for weddings one joint envelope is standard."),
      ("What if I can’t attend the wedding?", "It’s polite to still send a red envelope, typically somewhat less than if you attended (we use about 60%)."),
      ("Which amounts should I avoid?", "Anything containing 4, odd amounts (associated with funerals) and 250 (二百五 = idiot).")],
     "Wedding Red Envelope Calculator"))

    out.append(tool_page("tools/number-code-decoder.html",
     "Chinese Number Code Decoder — 555, 520, 1314 & Lucky Number Checker | 555185",
     "Chinese number code decoder &amp; luck checker",
     "Decode any number in Chinese: internet slang (555, 520, 1314, 886, 666), digit homophones and a luck score for phone numbers, licence plates, prices and dates.",
     "Type any digits — a phone number, licence plate, price, date or a mysterious chat message — and see the slang codes, homophones and luck score.",
     '''<div class="tool" id="dec-tool"><label for="dec-in">Enter digits</label><div class="copy-out"><input id="dec-in" inputmode="numeric" placeholder="e.g. 555185" maxlength="24"><button class="btn" id="dec-go" type="button">Decode</button></div>
<div class="pills" style="margin-top:10px"><span class="muted" style="align-self:center">Try:</span><button class="pill" data-try="555185">555185</button><button class="pill" data-try="5201314">5201314</button><button class="pill" data-try="1688">1688</button><button class="pill" data-try="13800138000">13800138000</button><button class="pill" data-try="748">748</button><button class="pill" data-try="886">886</button></div>
<div class="result" id="dec-out" aria-live="polite"></div></div>''',
     '''<h2>How Chinese number codes work</h2><p>Chinese has many syllables that sound alike. Because each digit is one syllable, a string of digits can be “read” as a phrase: <b>5-2-0</b> (wǔ èr líng) ≈ 我爱你 (wǒ ài nǐ, I love you); <b>5-5-5</b> (wǔ wǔ wǔ) ≈ 呜呜呜 (crying). In phone numbers 1 is read <i>yāo</i>, giving 要 (want / will) — so <b>518</b> = 我要发 “I will prosper”.</p>
<h2>How the luck score is calculated</h2><p>Each digit adds or subtracts points (8 and 6/9 add; 4 subtracts heavily). Famous sequences (888, 168, 518), repeating triples and an 8 ending add points; 250, 14 and 74 subtract. Recognised love codes like 1314 are exempt from the 4-penalty. The score is a cultural heuristic for fun and naming decisions — not a prediction.</p>
<p>Browse the full <a href="../meanings/">number code dictionary</a>.</p>''',
     [("What does 555 mean in Chinese?", "555 (wǔ wǔ wǔ) imitates 呜呜呜, the sound of crying — it’s the Chinese texting equivalent of ‘boo-hoo’. In Thai, 555 means ‘hahaha’."),
      ("What does 520 mean?", "520 means ‘I love you’ (我爱你). May 20 is celebrated online in China as a romantic day."),
      ("Are phone numbers with 8 really more expensive in China?", "Yes — numbers and licence plates heavy in 8s and 6s are widely sold at premiums, and auctions for repeat-8 plates have made headlines for decades."),
      ("Why is 1 read as ‘yāo’?", "When reading phone and room numbers aloud, Mandarin speakers say yāo (幺) for 1 to avoid confusing yī with qī (7). That’s why 1 often stands for 要 in codes.")],
     "Number Code Decoder"))

    out.append(tool_page("tools/chinese-financial-numerals.html",
     "大写 Converter — Chinese Financial Numerals for Cheques & Invoices (壹贰叁) | 555185",
     "大写 converter: write amounts in Chinese financial numerals",
     "Convert numbers to Chinese financial (capital) numerals 大写 — 壹贰叁肆伍陆柒捌玖拾 — for RMB, HKD and TWD cheques, invoices, contracts and red envelopes. Simplified and Traditional.",
     "Formal “capital” numerals (大写) can’t be altered with a pen stroke, so they’re required on cheques, receipts and contracts — and look elegant on a red envelope.",
     '''<div class="tool" id="dx-tool"><div class="row2"><div><label for="dx-in">Amount</label><input id="dx-in" inputmode="decimal" value="1688.50" placeholder="e.g. 8888.88"></div>
<div><label for="dx-cur">Currency / style</label><select id="dx-cur"><option value="CNY">RMB (元 角 分)</option><option value="HKD">HKD (圓 毫 仙)</option><option value="TWD">TWD (元 角 分)</option><option value="none">Number only</option></select></div></div>
<div class="chips" style="margin:12px 0"><label class="check"><input type="checkbox" id="dx-trad"> Traditional characters</label><label class="check"><input type="checkbox" id="dx-prefix"> Add currency prefix (人民币…)</label></div>
<label>Financial numerals (大写)</label><div class="copy-out"><output id="dx-out" class="zh"></output><button class="btn" type="button" data-copy="#dx-out">Copy</button></div>
<p style="margin-top:12px"><span class="muted">Everyday numerals (小写):</span> <b class="zh" id="dx-lower"></b></p></div>''',
     '''<h2>The 大写 numerals</h2><div class="tbl"><table><thead><tr><th>Value</th><th>Everyday</th><th>大写 (Simplified)</th><th>大寫 (Traditional)</th></tr></thead><tbody>
<tr><td>0</td><td>零</td><td>零</td><td>零</td></tr><tr><td>1</td><td>一</td><td>壹</td><td>壹</td></tr><tr><td>2</td><td>二</td><td>贰</td><td>貳</td></tr><tr><td>3</td><td>三</td><td>叁</td><td>參</td></tr><tr><td>4</td><td>四</td><td>肆</td><td>肆</td></tr><tr><td>5</td><td>五</td><td>伍</td><td>伍</td></tr><tr><td>6</td><td>六</td><td>陆</td><td>陸</td></tr><tr><td>7</td><td>七</td><td>柒</td><td>柒</td></tr><tr><td>8</td><td>八</td><td>捌</td><td>捌</td></tr><tr><td>9</td><td>九</td><td>玖</td><td>玖</td></tr>
<tr><td>10 / 100 / 1,000</td><td>十 / 百 / 千</td><td>拾 / 佰 / 仟</td><td>拾 / 佰 / 仟</td></tr><tr><td>10,000 / 10⁸</td><td>万 / 亿</td><td>万 / 亿</td><td>萬 / 億</td></tr></tbody></table></div>
<h2>Rules the converter applies</h2><ul><li>Groups of four digits (万, 亿) — Chinese counts in ten-thousands, not thousands.</li><li>Inner zeros collapse to a single 零: 1,005 → 壹仟零伍.</li><li>Amounts with no fen end in <b>整</b> (“exactly”), so nothing can be added.</li><li>RMB uses 元 角 分; Hong Kong cheques use 圓 毫 仙.</li><li>Financial writing keeps the leading 壹 in 壹拾 (10).</li></ul>
<p class="note">Always double-check legal and banking documents against your bank’s own requirements.</p>''',
     [("What is 大写 in Chinese?", "大写 (dàxiě, ‘capital writing’) are complex forms of the numerals (壹贰叁…) used on financial documents because simple strokes like 一 or 二 are easy to alter."),
      ("How do I write 10,000 yuan on a cheque?", "人民币壹万元整 — ‘RMB ten thousand yuan exactly’."),
      ("Why does the result end with 整?", "整 means ‘whole / exactly’ and is added when there are no smaller units, preventing anyone from appending extra digits."),
      ("Is 肆 (4) unlucky on a red envelope?", "It’s still 4, so avoid amounts containing it on gifts. On invoices and contracts it’s perfectly normal.")],
     "大写 Converter"))

    out.append(tool_page("tools/lucky-amount-finder.html",
     "Lucky Amount & Price Finder — Best Chinese Lucky Numbers Near Your Budget | 555185",
     "Lucky amount &amp; price finder",
     "Find the luckiest amount near any budget for red envelopes, weddings and condolence money, or the best price ending for Chinese-speaking customers (8, 88, 168, 188, 888).",
     "Enter a budget or price. We return the luckiest nearby options — even for celebrations, odd for condolences, and optimised endings for retail pricing.",
     '''<div class="tool" id="la-tool"><div class="row2"><div><label for="la-in">Budget or price</label><input id="la-in" type="number" min="1" value="500"></div>
<div><label for="la-mode">Use</label><select id="la-mode"><option value="gift">Red envelope / gift (even)</option><option value="price">Retail price for Chinese customers</option><option value="funeral">Condolence money (odd)</option></select></div></div>
<div class="row2" style="margin-top:14px"><div><label for="la-cur">Currency symbol</label><select id="la-cur"><option value="¥">¥</option><option value="$">$</option><option value="HK$">HK$</option><option value="S$">S$</option><option value="RM">RM</option><option value="NT$">NT$</option><option value="£">£</option><option value="€">€</option></select></div><div style="align-self:end"><button class="btn block" id="la-go" type="button">Find lucky amounts</button></div></div>
<div class="result" id="la-out" aria-live="polite"></div></div>''',
     '''<h2>Why lucky pricing matters</h2><p>Number preferences are a real commercial force in Chinese-speaking markets: brands launch on the 8th, price at 168 or 888, and avoid the digit 4 in model numbers, floors and phone lines. If you sell to Chinese-speaking customers — e-commerce, real estate, luxury, weddings, Lunar New Year promotions — a price ending in 8 or 6 signals prosperity, while a 4 quietly costs you conversions.</p>
<h2>Quick reference</h2><ul><li><b>Gift ladder:</b> 66 · 88 · 168 · 188 · 288 · 388 · 520 · 666 · 888 · 1,314 · 1,688 · 8,888</li><li><b>Avoid:</b> any 4, 250, 14, 74 and odd numbers for happy occasions</li><li><b>Condolence (帛金):</b> odd amounts such as 101, 301, 501 in a white envelope</li></ul>
<p>Selling into China, Hong Kong, Taiwan or Singapore? <a href="../quote.html#market">Get a Chinese-market pricing &amp; localisation review</a>.</p>''',
     [("What is the luckiest amount to give?", "Amounts made of 8s (88, 888, 8,888) are considered the most prosperous. 6s (smooth) and 9s (long-lasting) are close behind, and 520 / 1,314 are romantic choices."),
      ("Why odd numbers for funerals?", "Even numbers are for joyful occasions (good things come in pairs). Condolence money uses odd amounts so that the sorrow doesn’t ‘pair up’."),
      ("Does lucky pricing work outside China?", "It matters wherever your customers are Chinese-speaking: Singapore, Malaysia, Hong Kong, Taiwan, Vancouver, Toronto, Sydney, the Bay Area and more.")],
     "Lucky Amount Finder"))

    out.append(tool_page("tools/greetings-generator.html",
     "Chinese New Year Greetings Generator with Pinyin — 2027 Year of the Goat | 555185",
     "Chinese greetings generator (with pinyin)",
     "Copy Chinese New Year, wedding, birthday and business greetings with pinyin and English meaning — and download a shareable red greeting card. Includes Year of the Goat 2027 blessings.",
     "Pick an occasion, get a blessing with pinyin and English, then copy it or download a red card for WeChat, WhatsApp or Instagram.",
     '''<div class="tool" id="gr-tool"><div class="row2"><div><label for="gr-cat">Occasion</label><select id="gr-cat"><option value="">All occasions</option></select></div><div style="align-self:end"><button class="btn block" type="button" id="gr-go">Give me another</button></div></div>
<div class="result on" style="text-align:center"><div class="big zh" id="gr-zh"></div><p style="font-size:1.15rem;margin:.4em 0" id="gr-py"></p><p class="muted" id="gr-en"></p>
<div class="pills" style="justify-content:center"><button class="btn sm" type="button" id="gr-copy">Copy text</button><button class="btn sm gold" type="button" id="gr-card">Download card (PNG)</button></div></div>
<h3 style="margin-top:22px">All greetings in this category</h3><div class="tbl"><table><thead><tr><th>Chinese</th><th>Pinyin</th><th>Meaning</th></tr></thead><tbody id="gr-list"></tbody></table></div></div>''',
     '''<h2>How to use Chinese greetings</h2><p>Say or write the blessing when you hand over a red envelope, at a wedding banquet toast, or in a WeChat message. Pair <b>恭喜发财</b> (gōngxǐ fācái — wishing you prosperity) with a red envelope at New Year; write <b>百年好合</b> on a wedding envelope; use <b>生意兴隆</b> for a business opening.</p>
<p>2027 is the <b>Year of the Goat</b> (羊年, from 6 February 2027). The classic pun is <b>三羊开泰</b> (sān yáng kāi tài), a play on 三阳开泰 — “three yang bring peace and prosperity”.</p>''',
     [("What do you say when giving a red envelope?", "The most common phrase is 恭喜发财 (gōngxǐ fācái), ‘wishing you prosperity’. Children often reply 恭喜发财，红包拿来 — ‘prosperity to you, now hand over the red packet!’"),
      ("Is ‘Gong Hei Fat Choy’ the same thing?", "Yes — it’s the Cantonese pronunciation of 恭喜发财, common in Hong Kong, Guangdong and many overseas communities."),
      ("What greeting fits the Year of the Goat?", "羊年大吉 (yáng nián dà jí — great luck in the Year of the Goat) and 三羊开泰 (sān yáng kāi tài) are perfect for 2027.")],
     "Greetings Generator"))

    out.append(tool_page("tools/zodiac-cny-countdown.html",
     "Chinese Zodiac Finder & Lunar New Year 2027 Countdown (Year of the Goat) | 555185",
     "Zodiac finder &amp; Lunar New Year countdown",
     "Find your real Chinese zodiac sign and element (adjusted for the Lunar New Year date) and count down to Lunar New Year 2027 — the Year of the Fire Goat, 6 February 2027.",
     "Lunar New Year 2027 falls on Saturday 6 February — the start of the Year of the Fire Goat (丁未). Find your sign using the exact New Year date for your birth year.",
     '''<div class="tool" id="zd-tool"><h3 class="mt0">Countdown to Lunar New Year 2027</h3><div class="cd" data-countdown="2027-02-06"></div>
<hr style="border:0;border-top:1px solid var(--line);margin:20px 0">
<div class="row2"><div><label for="zd-in">Your date of birth</label><input type="date" id="zd-in" value="1990-01-20" min="1920-02-20" max="2045-12-31"></div><div style="align-self:end"><button class="btn block" type="button" id="zd-go">Find my sign</button></div></div>
<div class="result" id="zd-out" aria-live="polite"></div>
<h3 style="margin-top:22px">Upcoming Lunar New Years</h3><div class="tbl"><table><thead><tr><th>Year</th><th>New Year’s Day</th><th>Sign</th></tr></thead><tbody id="zd-table"></tbody></table></div></div>''',
     '''<h2>Why your sign may not match your birth year</h2><p>The zodiac year starts on Lunar New Year, which moves between 21 January and 20 February. Someone born on 20 January 1990 is a <b>Snake</b> (1989’s year), not a Horse, because the 1990 New Year began on 27 January. This tool uses a 1920–2045 table of New Year dates to get it right.</p>
<h2>Planning for Lunar New Year 2027</h2><ul><li><b>Now–December:</b> order custom red envelopes and corporate gifts (print lead times run 2–6 weeks).</li><li><b>January:</b> withdraw new notes from the bank, plan your <a href="hongbao-calculator.html">red envelope budget</a>.</li><li><b>5 Feb (Eve):</b> reunion dinner; <b>6 Feb:</b> New Year’s Day; <b>20 Feb:</b> Lantern Festival ends the season.</li></ul>''',
     [("When is Chinese New Year 2027?", "Saturday, 6 February 2027. It begins the Year of the Goat (Fire Goat, 丁未)."),
      ("What is the zodiac animal for 2026?", "2026 (from 17 February 2026) is the Year of the Horse — the Fire Horse."),
      ("Is it the Year of the Goat or the Sheep?", "羊 (yáng) covers goats, sheep and rams, so all three translations are used. ‘Goat’ is the most common in English.")],
     "Zodiac Finder"))
    return out
