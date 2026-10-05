from layout import page, ad, sidebar, faq_html, faq_ld, esc, lead_card, PARTNER, UPDATED

VIDEOS = [
 ("RcR5Jm1JPvo", "Red Envelope Etiquette: When, How, and Why to Give", "SteadyStep English", "Etiquette"),
 ("ICQi5pr2c2E", "Chinese New Year Red Envelopes | Giving and Receiving Etiquette", "Let's do a recap", "Etiquette"),
 ("hecCgKFZQJQ", "How to Give & Receive Red Envelopes | Wow! Taiwan", "TaiwanPlus", "Etiquette"),
 ("wn0OMMAByjk", "Hongbao: 8 Things You Should Know About The Lucky Red Envelope", "Innovatronix Tv", "Etiquette"),
 ("JgrZiQPO3_E", "The Hongbao Explained | Chinese Red Envelope", "Chinese Civilization Channel", "Etiquette"),
 ("q4HHhGQppYo", "Chinese Wedding Gift Guide 過大禮", "Off the Great Wall", "Weddings"),
 ("pT52hREAf18", "Chinese Lucky Numbers", "Numberphile", "Lucky numbers"),
 ("QwvlAbisiRc", "Most Lucky and Unlucky Numbers for Chinese People", "Off the Great Wall", "Lucky numbers"),
 ("42OAA04eft4", "Crack China's Number Code: 520 = Love, 666 = Awesome, 555 = Cry!", "Chinese Teacher - Red", "Number slang"),
 ("O6HaohkSBlk", "Chinese Special Numbers Explained: 520, 521, 1314, 555", "Xiao Xiao Chinese", "Number slang"),
 ("gXoC6oubwDM", "88, 520, 5201314 in Chinese — Meanings", "Everyday Chinese", "Number slang"),
 ("uH7FO_8LHQQ", "Chinese number characters in Capital (中文數字大寫)", "范姆斯特Vamst", "Financial numerals"),
 ("IK7xfi7e180", "中文数字大写 零壹贰叁肆伍陆柒捌玖拾", "Yuan Pinyin", "Financial numerals"),
]

def vid(v, r="./"):
    return f'<div><div class="vid" data-id="{v[0]}" data-title="{esc(v[1])}"></div><p class="vcap">{esc(v[1])}<small>{esc(v[2])} · {v[3]}</small></p></div>'

HP = '<div class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></div>'
REGIONS = "".join(f"<option>{x}</option>" for x in ["Mainland China", "Hong Kong / Macau", "Taiwan", "Singapore", "Malaysia", "USA", "Canada", "UK / Europe", "Australia / NZ", "Other"])

def build(codes, guides):
    out = []
    # ---------------- HOME ----------------
    tools = [("tools/hongbao-calculator.html", "🧧", "Red Envelope Planner", "Budget every envelope by region & relationship."),
             ("tools/wedding-red-envelope-calculator.html", "💍", "Wedding Gift Calculator", "How much to give at a Chinese wedding."),
             ("tools/number-code-decoder.html", "🔢", "Number Code Decoder", "555, 520, phone numbers, plates — decoded."),
             ("tools/chinese-financial-numerals.html", "壹", "大写 Converter", "Formal numerals for cheques & envelopes."),
             ("tools/lucky-amount-finder.html", "💰", "Lucky Amount Finder", "Snap any budget or price to a lucky number."),
             ("tools/greetings-generator.html", "🎊", "Greetings Generator", "Blessings with pinyin + downloadable cards.")]
    tcards = "".join(f'<a class="card" href="{p}"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p></a>' for p, i, n, d in tools)
    pop = ["555", "520", "1314", "666", "888", "168", "518", "250", "886", "233", "5201314", "748"]
    cmap = {c["num"]: c for c in codes}
    ncards = "".join(f'<a class="num-card" href="meanings/{n}.html"><b>{n}</b><span class="zh">{esc(cmap[n]["zh"])}</span><br><span>{esc(cmap[n]["en"])}</span></a>' for n in pop)
    gcards = "".join(f'<a class="card" href="guides/{g[0]}.html"><div class="ico">{g[1]}</div><h3>{g[2]}</h3><p>{g[3]}</p></a>' for g in guides[:6])
    vids = "".join(vid(v) for v in [VIDEOS[0], VIDEOS[8], VIDEOS[6]])
    home_faq = [("What does 555185 mean?", "Read in two halves: 555 (wǔ wǔ wǔ ≈ 呜呜呜) is Chinese texting slang for crying, and 185 (yāo bā wǔ ≈ 要发我) is a playful reading of ‘prosperity — to me!’. Together: from tears to fortune. It is a constructed homophone reading, not an official term."),
                ("How much money goes in a red envelope?", "It depends on region and relationship: roughly ¥100–200 for friends’ children in mainland China, HK$20–50 in Hong Kong, S$8–10 in Singapore and $10–20 in North America; parents receive much more. Our free planner calculates lucky amounts for your whole list."),
                ("When is Lunar New Year 2027?", "Saturday, 6 February 2027 — the start of the Year of the Fire Goat."),
                ("Are the tools free?", "Yes. All calculators, decoders and guides are free with no sign-up. We’re funded by advertising, sponsors, donations and optional quote services for businesses and weddings.")]
    body = f'''<section class="hero"><div class="wrap hero-grid"><div>
<span class="eyebrow">555 → 185 · From tears to fortune</span>
<h1>Red envelopes, lucky numbers &amp; the Chinese number code — decoded.</h1>
<p class="lead">How much to put in a hongbao. What 555, 520 and 1314 really mean. Which amounts bring luck and which quietly offend. Free calculators and guides for Lunar New Year 2027, Chinese weddings and doing business with Chinese-speaking customers.</p>
<div class="ctas"><a class="btn" href="tools/hongbao-calculator.html">🧧 Plan my red envelopes</a><a class="btn ghost" href="tools/number-code-decoder.html">Decode a number</a></div>
<div class="trust"><span>7 free tools</span><span>{len(codes) + 10} number meanings</span><span>8 regions covered</span><span>No sign-up</span></div></div>
<div class="decode"><p class="muted mt0" style="text-align:center;font-size:.85rem;letter-spacing:.1em;text-transform:uppercase">The number in our name</p>
<div class="digits"><div class="digit"><b>5</b><i>呜 wū</i></div><div class="digit"><b>5</b><i>呜 wū</i></div><div class="digit"><b>5</b><i>呜 wū</i></div><div class="digit g"><b>1</b><i>要 yāo</i></div><div class="digit g"><b>8</b><i>发 fā</i></div><div class="digit g"><b>5</b><i>我 wǒ</i></div></div>
<p style="text-align:center" class="mb0"><b class="zh">呜呜呜 … 要发我！</b><br><span class="muted">“Boo-hoo… now prosperity comes to me.” Stop crying about money — the red packet is on its way.</span></p>
<p style="text-align:center;margin:12px 0 0"><a href="the-555185-story.html">Read the 555185 story →</a></p></div></div></section>
<div class="wrap">{ad("top")}</div>
<section class="block"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Free tools</span><h2>Answer it in 10 seconds</h2></div><p>Built from published etiquette norms across mainland China, Hong Kong, Taiwan, Singapore, Malaysia and the diaspora.</p></div>
<div class="grid g3">{tcards}</div></div></section>
<section class="block" style="padding-top:0"><div class="wrap"><div class="card" id="home-dec"><div class="sec-head" style="margin-bottom:12px"><div><h2 class="mb0">Decode any number</h2></div><p>Phone number, plate, price or chat message.</p></div>
<div class="copy-out"><input id="home-dec-in" inputmode="numeric" value="555185" aria-label="Digits to decode"><button class="btn" id="home-dec-go" type="button">Decode</button></div><div class="result" id="home-dec-out" aria-live="polite"></div></div></div></section>
<section class="block" style="padding-top:0"><div class="wrap"><div class="band"><div><span class="eyebrow" style="background:rgba(255,255,255,.15);color:#FFD86B">Year of the Goat · 6 Feb 2027</span><h2>Lunar New Year 2027 countdown</h2><p>Order custom envelopes by early December, withdraw new notes in January, and plan every envelope before the reunion dinner.</p><div class="cd" data-countdown="2027-02-06" style="color:var(--ink)"></div></div><div><a class="btn gold block" href="guides/lunar-new-year-2027-planner.html">Open the 2027 planner</a><p style="margin-top:10px;font-size:.9rem">Need 100+ branded envelopes? <a href="quote.html#corporate" style="color:#FFD86B">Get quotes →</a></p></div></div></div></section>
<section class="block"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Number codes</span><h2>What Chinese numbers really mean</h2></div><a class="btn ghost sm" href="meanings/">All {len(codes)} codes →</a></div><div class="num-grid">{ncards}</div></div></section>
<div class="wrap">{ad("inarticle")}</div>
<section class="block"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">For business &amp; weddings</span><h2>Get it done — free quotes from vetted specialists</h2></div><p>Tell us once. We match your request with suitable suppliers and specialists, so you compare offers instead of chasing them.</p></div>
<div class="grid g4">
<a class="card" href="quote.html#corporate"><div class="ico">🏢</div><h3>Corporate CNY gifting</h3><p>Custom envelopes, hampers and staff 开工利是 — from 100 units.</p></a>
<a class="card" href="quote.html#wedding"><div class="ico">💍</div><h3>Chinese wedding vendors</h3><p>Banquet, tea ceremony, lion dance, décor, planners.</p></a>
<a class="card" href="quote.html#market"><div class="ico">📈</div><h3>Chinese-market pricing</h3><p>Lucky pricing, localisation and red-packet campaigns.</p></a>
<a class="card" href="quote.html#plan"><div class="ico">📝</div><h3>Free hongbao plan</h3><p>Personal amounts for your list + 2027 checklist.</p></a></div>
<p class="center" style="margin-top:22px"><a class="btn" href="quote.html">Get free quotes</a></p></div></section>
<section class="block"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Guides</span><h2>Know the etiquette</h2></div><a class="btn ghost sm" href="guides/">All guides →</a></div><div class="grid g3">{gcards}</div></div></section>
<section class="block"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Watch</span><h2>Videos worth your time</h2></div><a class="btn ghost sm" href="videos.html">Video library →</a></div><div class="grid g3">{vids}</div></div></section>
<section class="block"><div class="wrap grid g3">
<div class="card"><span class="tag">Contest</span><h3>2027 Red Envelope Design Contest</h3><p style="margin-bottom:14px">Design a Year of the Goat hongbao. Winners get prize money and their design printed.</p><a class="btn sm" href="contests.html">Enter / learn more</a></div>
<div class="card"><span class="tag">Support</span><h3>Send us a lucky hongbao</h3><p style="margin-bottom:14px">Keep the tools free and ad-light. From $8.88 — every gift funds content, contests and talent.</p><a class="btn sm gold" href="donate.html">Donate</a></div>
<div class="card"><span class="tag">Partner</span><h3>Sponsor, advertise or acquire</h3><p style="margin-bottom:14px">Reach people planning Lunar New Year and wedding spend — or talk to us about this domain.</p><a class="btn sm ghost" href="advertise.html">Advertise</a> <a class="btn sm ghost" href="{PARTNER}" target="_blank" rel="noopener">Contact</a></div></div></section>
<section class="block"><div class="wrap" style="max-width:860px"><h2 class="center">Quick answers</h2>{faq_html(home_faq)}{ad("footer")}</div></section>'''
    out.append(("index.html", page("index.html", "555185 — Red Envelope Calculator, Chinese Number Meanings & Lucky Amounts",
        "How much to put in a red envelope, what Chinese number codes like 555, 520 and 1314 mean, lucky and unlucky amounts, wedding gift calculator and Lunar New Year 2027 tools. Free, no sign-up.",
        body, ld=faq_ld(home_faq))))

    # ---------------- STORY ----------------
    story_faq = [("Is 555185 an official Chinese term?", "No. 555 is established slang for crying; reading 185 as 要发我 is our own playful homophone construction. We present it as a creative reading, not a fixed idiom."),
                 ("Does 555185 contain any unlucky digits?", "No — there is no 4. It has a memorable 555 rhythm and ends on 8-5, read as ‘prosper — me’."),
                 ("Is 555185 connected to a company, phone number or lottery?", "No. This site is independent and uses the digits only as a descriptive string. See our trademark and copyright disclosure.")]
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Our name</span><h1>The 555185 story: from tears to fortune</h1><p class="lead">Six digits, two moods, one very Chinese idea: the money worry ends when the red envelope arrives.</p></div>
<div class="wrap layout"><article class="prose">
<div class="decode"><div class="digits"><div class="digit"><b>5</b><i>wǔ</i></div><div class="digit"><b>5</b><i>wǔ</i></div><div class="digit"><b>5</b><i>wǔ</i></div><div class="digit g"><b>1</b><i>yāo</i></div><div class="digit g"><b>8</b><i>bā</i></div><div class="digit g"><b>5</b><i>wǔ</i></div></div><p class="center mb0 zh" style="font-size:1.4rem">呜呜呜 · 要发我</p></div>
<h2>Part one: 555 — 呜呜呜</h2><p>In Chinese chats, <a href="meanings/555.html">555</a> is the sound of crying. Each 5 (wǔ) echoes 呜 (wū), the written sob. People use it for everything from real heartbreak to the empty-wallet feeling right before payday or the New Year bills arrive.</p>
<h2>Part two: 185 — 要发我</h2><p>Read phone-style, <a href="meanings/185.html">185</a> is yāo-bā-wǔ. 1 (yāo) sounds like 要 (want / will), 8 (bā) carries 发 (fā, prosper) and 5 (wǔ) is 我 (wǒ, me). String them together and you get a cheeky 要发我 — “prosperity, to me!” — or, in red-packet season, “send me one!” It’s a constructed reading in the spirit of famous codes like <a href="meanings/518.html">518</a> (我要发, I will prosper) and <a href="meanings/168.html">168</a> (一路发).</p>
<h2>Why it fits this website</h2><p>Lunar New Year and wedding season are when money anxiety and money luck collide: How much should I give? Is this amount rude? What does that number mean? 555185 exists to turn the 555 moment into a 185 moment — with clear answers, lucky amounts and, when you need it, people who can help.</p>
<blockquote>Fun fact: in Thai, 555 means “hahaha” (5 is <i>ha</i>). So 555185 is crying in Chinese and laughing in Thai — the full emotional range of gift season.</blockquote>
{ad("inarticle")}
<h2>A number with no 4</h2><p>For a brand that lives on Chinese number culture, the absence of 4 matters. 555185 has no death-sounding digit, an easy rhythm (triple-five, then one-eight-five) and an 8 in the “prosper” position. Run it through the <a href="tools/number-code-decoder.html?n=555185">decoder</a> to see its luck score.</p>
<h2>FAQ</h2>{faq_html(story_faq)}</article>{sidebar("./")}</div>'''
    out.append(("the-555185-story.html", page("the-555185-story.html", "What Does 555185 Mean? 555 (Crying) + 185 (Prosperity to Me) | 555185",
        "The meaning of 555185 in Chinese number slang: 555 = 呜呜呜 (crying), 185 = 要发我 (prosperity to me). A playful homophone story from tears to fortune.",
        body, crumbs=[("", "The 555185 story")], ld=faq_ld(story_faq))))

    # ---------------- QUOTE / LEAD GEN ----------------
    def contact_step():
        return f'''<div class="row2"><div><label>Full name *</label><input name="name" required autocomplete="name"></div><div><label>Email *</label><input type="email" name="email" required autocomplete="email"></div></div>
<div class="row2"><div><label>Phone / WhatsApp / WeChat</label><input name="phone" autocomplete="tel"></div><div><label>Country / region *</label><select name="region" required>{REGIONS}</select></div></div>
<div><label>How did you hear about us?</label><select name="source"><option>Google search</option><option>YouTube</option><option>Social media</option><option>Friend / colleague</option><option>Other</option></select></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the <a href="privacy.html">privacy policy</a>. *</label>'''
    bar = lambda n: '<div class="steps-bar">' + "<span></span>" * n + "</div>"
    nav = lambda first=False, last=False: '<div class="step-nav">' + ("" if first else '<button type="button" class="btn ghost" data-prev>← Back</button>') + ('<button type="submit" class="btn">Get my free quotes →</button>' if last else '<button type="button" class="btn" data-next>Continue →</button>') + "</div>"
    corp = f'''<form class="form" data-form="Quote — Corporate CNY gifting" data-steps>{HP}{bar(3)}
<div class="step"><h3 class="mt0">1 · What do you need?</h3><div data-chips="multi"><label>Products (pick any)</label><div class="chips"><button type="button" class="chip" data-v="Custom red envelopes">Custom red envelopes</button><button type="button" class="chip" data-v="Gift boxes / hampers">Gift boxes / hampers</button><button type="button" class="chip" data-v="Staff red envelope program">Staff 开工 envelopes</button><button type="button" class="chip" data-v="Branded digital red packets">Digital red-packet campaign</button><button type="button" class="chip" data-v="Other merchandise">Other merch</button></div><input type="hidden" name="products"></div>
<div class="row2"><div><label>Quantity *</label><select name="quantity" required><option value="">Choose…</option><option>100–249</option><option>250–499</option><option>500–999</option><option>1,000–2,499</option><option>2,500–9,999</option><option>10,000+</option></select></div><div><label>Needed by *</label><input type="date" name="deadline" required></div></div>{nav(True)}</div>
<div class="step"><h3 class="mt0">2 · Customisation &amp; budget</h3><div class="row2"><div><label>Finish</label><select name="finish"><option>Gold foil</option><option>Red/gold print only</option><option>Embossed + foil</option><option>Not sure — advise me</option></select></div><div><label>Budget (total)</label><select name="budget"><option>Under $500</option><option>$500–$1,999</option><option>$2,000–$4,999</option><option>$5,000–$19,999</option><option>$20,000+</option></select></div></div>
<div><label>Logo / artwork link (Drive, Dropbox…)</label><input type="url" name="artwork_url" placeholder="https://"></div><div><label>Design notes</label><textarea name="notes" placeholder="Brand colours, zodiac Goat motif, blessing text, delivery addresses…"></textarea></div>
<div class="row2"><div><label>Company *</label><input name="company" required autocomplete="organization"></div><div><label>Job title</label><input name="title"></div></div>{nav()}</div>
<div class="step"><h3 class="mt0">3 · Where should we send quotes?</h3>{contact_step()}{nav(last=True)}</div><p class="form-msg"></p></form>'''
    wed = f'''<form class="form" data-form="Quote — Wedding vendor match" data-steps>{HP}{bar(3)}
<div class="step"><h3 class="mt0">1 · Your celebration</h3><div class="row2"><div><label>Event *</label><select name="event" required><option>Wedding banquet</option><option>Tea ceremony</option><option>Betrothal (过大礼)</option><option>Full-month / 100-day party</option><option>Milestone birthday</option><option>Business opening</option></select></div><div><label>Date</label><input type="date" name="date"></div></div>
<div class="row2"><div><label>City *</label><input name="city" required placeholder="e.g. Toronto, Singapore"></div><div><label>Guests</label><select name="guests"><option>Under 50</option><option>50–149</option><option>150–299</option><option>300+</option></select></div></div>{nav(True)}</div>
<div class="step"><h3 class="mt0">2 · What do you need?</h3><div data-chips="multi"><div class="chips"><button type="button" class="chip">Banquet venue</button><button type="button" class="chip">Chinese wedding planner</button><button type="button" class="chip">Tea ceremony set</button><button type="button" class="chip">Lion / dragon dance</button><button type="button" class="chip">Qipao / Qun Kwa</button><button type="button" class="chip">Custom red envelopes</button><button type="button" class="chip">Photographer / video</button><button type="button" class="chip">Décor &amp; invitations</button><button type="button" class="chip">Emcee (bilingual)</button></div><input type="hidden" name="services"></div>
<div class="row2"><div><label>Style</label><select name="style"><option>Traditional Chinese</option><option>Cantonese</option><option>Modern fusion</option><option>Cross-cultural</option></select></div><div><label>Total budget</label><select name="budget"><option>Under $10k</option><option>$10k–$25k</option><option>$25k–$60k</option><option>$60k+</option></select></div></div>
<div><label>Anything else?</label><textarea name="notes"></textarea></div>{nav()}</div>
<div class="step"><h3 class="mt0">3 · Your details</h3>{contact_step()}{nav(last=True)}</div><p class="form-msg"></p></form>'''
    mkt = f'''<form class="form" data-form="Quote — Chinese-market pricing & localisation" data-steps>{HP}{bar(2)}
<div class="step"><h3 class="mt0">1 · Your business</h3><div class="row2"><div><label>Company / website *</label><input name="company" required></div><div><label>Industry</label><select name="industry"><option>E-commerce / retail</option><option>Real estate</option><option>Luxury / jewellery</option><option>Food &amp; beverage</option><option>Finance / fintech</option><option>Travel / hospitality</option><option>Education</option><option>Other</option></select></div></div>
<div data-chips="multi"><label>Help with</label><div class="chips"><button type="button" class="chip">Lucky pricing review</button><button type="button" class="chip">Phone / SKU / address numbers</button><button type="button" class="chip">Lunar New Year campaign</button><button type="button" class="chip">Red-packet promotions</button><button type="button" class="chip">Chinese copy &amp; naming</button><button type="button" class="chip">Launch date selection</button></div><input type="hidden" name="help"></div>
<div class="row2"><div><label>Target market</label><select name="target">{REGIONS}</select></div><div><label>Monthly budget</label><select name="budget"><option>Under $1k</option><option>$1k–$5k</option><option>$5k–$20k</option><option>$20k+</option><option>One-off project</option></select></div></div>{nav(True)}</div>
<div class="step"><h3 class="mt0">2 · Your details</h3>{contact_step()}{nav(last=True)}</div><p class="form-msg"></p></form>'''
    plan = f'''<form class="form" data-form="Lead — Free Hongbao Plan">{HP}<h3 class="mt0">Your free personalised hongbao plan</h3>
<p class="muted mt0">Tell us who’s on your list. We’ll email lucky amounts per person, a budget total and the printable 2027 checklist.</p>
<div class="row2"><div><label>First name *</label><input name="name" required></div><div><label>Email *</label><input type="email" name="email" required></div></div>
<div class="row2"><div><label>Where you give *</label><select name="region" required>{REGIONS}</select></div><div><label>Approx. total budget</label><input name="budget" placeholder="e.g. ¥3,000 / $400"></div></div>
<div><label>Your list</label><textarea name="list" placeholder="e.g. 2 parents, 3 nieces (8–14 yrs), 4 colleagues’ kids, 1 building manager"></textarea></div>
<label class="check"><input type="checkbox" name="newsletter" value="yes" checked> Send me occasional tips before Lunar New Year and wedding season</label>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I accept the <a href="privacy.html">privacy policy</a>. *</label><button class="btn" type="submit">Email me my plan</button><p class="form-msg"></p></form>'''
    vendor = f'''<form class="form" data-form="Vendor / supplier application">{HP}<h3 class="mt0">List your business</h3><p class="muted mt0">Printers, gift suppliers, wedding vendors, translators and agencies — receive matched leads.</p>
<div class="row2"><div><label>Business name *</label><input name="company" required></div><div><label>Website *</label><input type="url" name="website" required placeholder="https://"></div></div>
<div class="row2"><div><label>Category *</label><select name="category" required><option>Red envelope / print supplier</option><option>Corporate gifts &amp; hampers</option><option>Wedding venue / planner</option><option>Lion dance / performers</option><option>Photo / video</option><option>Translation / localisation</option><option>Marketing agency</option><option>Other</option></select></div><div><label>Service area *</label><input name="area" required placeholder="Cities / countries / worldwide"></div></div>
<div class="row2"><div><label>Contact name *</label><input name="name" required></div><div><label>Email *</label><input type="email" name="email" required></div></div>
<div><label>Minimums, lead times, price range</label><textarea name="details"></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="terms.html">terms</a> and <a href="privacy.html">privacy policy</a>. *</label><button class="btn" type="submit">Apply to be listed</button><p class="form-msg"></p></form>'''
    qfaq = [("Is it free to request quotes?", "Yes. Requesting quotes and the hongbao plan is free and there’s no obligation to buy."),
            ("How fast will I hear back?", "We aim to reply within 1–2 business days. In peak season (December–January) give yourself extra time for production."),
            ("Who are the suppliers?", "Independent businesses that apply to be listed. We check basic details, but please review any supplier’s terms before ordering."),
            ("Do you share my details?", "Only with the suppliers relevant to your request, and only to respond to it. See our privacy policy.")]
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Free quotes · No obligation</span><h1>Get it done right — free quotes &amp; plans</h1><p class="lead">Custom red envelopes, corporate Lunar New Year gifting, Chinese wedding vendors, Chinese-market pricing — or a free personal hongbao plan. Tell us once; compare offers.</p>
<div class="trust"><span>Free to request</span><span>Reply in 1–2 business days</span><span>Your details go only to matched specialists</span><span>Order deadline for CNY 2027: early December</span></div></div>
<div class="wrap layout"><div><div class="tabs" data-tabs role="tablist"><button class="tab" role="tab" data-tab="corporate" aria-selected="true">🏢 Corporate gifting</button><button class="tab" role="tab" data-tab="wedding">💍 Wedding &amp; events</button><button class="tab" role="tab" data-tab="market">📈 Chinese-market pricing</button><button class="tab" role="tab" data-tab="plan">📝 Free hongbao plan</button><button class="tab" role="tab" data-tab="vendor">🤝 I’m a supplier</button></div>
<div class="card"><div class="panel on" id="corporate">{corp}</div><div class="panel" id="wedding">{wed}</div><div class="panel" id="market">{mkt}</div><div class="panel" id="plan">{plan}</div><div class="panel" id="vendor">{vendor}</div></div>
<h2 style="margin-top:32px">How it works</h2><div class="grid g3"><div class="card"><div class="stat">1</div><h3>Tell us once</h3><p>Two minutes, three short steps.</p></div><div class="card"><div class="stat">2</div><h3>We match</h3><p>Your brief goes to suitable specialists only.</p></div><div class="card"><div class="stat">3</div><h3>You compare</h3><p>Choose the offer that fits — or none at all.</p></div></div>
<h2>Questions</h2>{faq_html(qfaq)}</div>
<aside class="side"><div class="sticky"><div class="card"><h3>Why order early?</h3><ul><li>Printing + proofs: 2–4 weeks</li><li>Shipping: 1–3 weeks</li><li>Factories pause for the holiday</li></ul><p style="margin-top:10px"><b>Lunar New Year 2027: 6 Feb.</b></p></div>
<div class="card"><h3>Prefer to talk?</h3><p style="margin-bottom:12px">Message us and we’ll get back to you.</p><a class="btn block ghost" href="contact.html">Contact us</a></div>{ad("sidebar")}</div></aside></div>'''
    out.append(("quote.html", page("quote.html", "Free Quotes: Custom Red Envelopes, Corporate CNY Gifts & Chinese Wedding Vendors | 555185",
        "Request free quotes for custom-printed red envelopes, corporate Lunar New Year gifting, Chinese wedding vendors and Chinese-market pricing — or get a free personalised hongbao plan.",
        body, crumbs=[("", "Get a free quote")], ld=faq_ld(qfaq), sticky=False)))

    # ---------------- DONATE ----------------
    tiers = [("8.88", "Lucky 8", "Covers a day of hosting and tools", False), ("18.88", "要发发", "Funds one new guide or meaning page", True), ("88", "发发", "Pays toward a contest prize", False), ("188", "要发发 Patron", "Sponsors a freelance translator or designer brief", False)]
    tcards = "".join(f'<div class="card tier{" pop" if pop else ""}"><span class="tag">{esc(n)}</span><div class="price">${p}</div><p style="margin:6px 0 14px">{esc(d)}</p><button class="btn block{" ghost" if not pop else ""}" type="button" onclick="document.getElementById(\'don-amt\').value=\'{p}\';document.getElementById(\'pledge\').scrollIntoView({{behavior:\'smooth\'}})">Choose ${p}</button></div>' for p, n, d, pop in tiers)
    alloc = [("Operations &amp; hosting", 30), ("Content, research &amp; translation", 25), ("Hiring creative talent", 20), ("Contests &amp; prizes", 15), ("Promotion &amp; marketing", 10)]
    abars = "".join(f'<div style="margin-bottom:12px"><div style="display:flex;justify-content:space-between"><b>{n}</b><span>{v}%</span></div><div class="bar"><i style="width:{v}%"></i></div></div>' for n, v in alloc)
    dfaq = [("How do I pay?", "Use any payment button shown above. If none is shown yet, send a pledge with the form and we’ll reply with secure payment options."),
            ("Is my donation tax-deductible?", "No — 555185.com is an independent publication, not a registered charity, so support is not tax-deductible."),
            ("Can my company sponsor instead?", "Yes — sponsors get logo placement and reporting. See the <a href=\"advertise.html\">advertise page</a> or contact us via web.works/contact.")]
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Support 555185</span><h1>Send us a lucky hongbao 🧧</h1><p class="lead">Every tool and guide here is free. Your support keeps it that way — and funds new content, contests with real prizes, and paid work for writers, translators and designers.</p></div>
<div class="wrap"><div class="grid g4">{tcards}</div>
<div class="grid g2" style="margin-top:28px"><div class="card" id="pledge"><h2 class="mt0">Give now</h2>
<div class="pills"><a class="btn" data-donate="paypal" target="_blank" rel="noopener">PayPal</a><a class="btn" data-donate="stripe" target="_blank" rel="noopener">Card (Stripe)</a><a class="btn gold" data-donate="buymeacoffee" target="_blank" rel="noopener">Buy Me a Coffee</a><a class="btn gold" data-donate="kofi" target="_blank" rel="noopener">Ko-fi</a><a class="btn ghost" data-donate="github" target="_blank" rel="noopener">GitHub Sponsors</a></div>
<p class="note" data-donate-none>Online payment buttons are being set up. Send a pledge below and we’ll reply with secure payment options within 1–2 business days.</p>
<form class="form" data-form="Donation pledge" style="margin-top:14px">{HP}<div class="row2"><div><label>Amount (USD) *</label><input id="don-amt" name="amount" required value="18.88"></div><div><label>Frequency</label><select name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="row2"><div><label>Name *</label><input name="name" required></div><div><label>Email *</label><input type="email" name="email" required></div></div>
<div><label>Direct my gift to</label><select name="allocation"><option>Wherever it’s needed most</option><option>Operations &amp; hosting</option><option>Content &amp; translation</option><option>Hiring talent</option><option>Contests &amp; prizes</option><option>Promotion &amp; marketing</option></select></div>
<div><label>Message (optional)</label><textarea name="message" placeholder="A blessing for the community 🧧"></textarea></div><label class="check"><input type="checkbox" name="public" value="yes"> You may list my first name as a supporter</label>
<button class="btn" type="submit">Send pledge</button><p class="form-msg"></p></form></div>
<div class="card"><h2 class="mt0">Where the money goes</h2>{abars}<p class="muted" style="font-size:.88rem">Target allocation. We publish a short supporter update each Lunar New Year.</p>
<h3>Supporter perks</h3><ul class="check-list"><li>Name on the supporters wall (optional)</li><li>Early access to printable envelopes &amp; cheat sheets</li><li>Vote on the next tools we build</li><li>Patron ($188+): thank-you credit in a guide</li></ul></div></div>
<h2 style="margin-top:32px">FAQ</h2>{faq_html(dfaq)}{ad("footer")}</div>'''
    out.append(("donate.html", page("donate.html", "Donate — Support Free Red Envelope & Number Tools | 555185",
        "Support 555185.com with a lucky donation from $8.88. Funds operations, content, hiring talent, promotion, contests and prizes.", body, crumbs=[("", "Donate")], ld=faq_ld(dfaq))))

    # ---------------- CONTESTS ----------------
    cfaq = [("Who can enter?", "Anyone 18+ (or with a parent/guardian’s consent) where such contests are legal. Void where prohibited."),
            ("Do I keep the rights to my entry?", "Yes. You grant 555185.com a non-exclusive licence to display and promote your entry; winners agree to a separate licence if their design is printed."),
            ("Are the prizes confirmed?", "The prize pool is set out in the official rules published when each contest opens and may grow with sponsors. No purchase or donation is required to enter or win."),
            ("How are winners chosen?", "A judging panel scores entries (creativity 40%, cultural authenticity 30%, craft 30%), with a public-vote People’s Choice award.")]
    contests = [("🎨", "Red Envelope Design Contest 2027", "Design a Year of the Goat hongbao (front + back).", "Prize pool: $888 · 1st $388 · 2nd $188 · 3rd $88 · People’s Choice $88 · Merit $136 shared", "Entries close 15 Dec 2026"),
                ("🎥", "Best New Year Greeting Video", "60-second video: your family’s greeting, tradition or red-envelope moment.", "Prize pool: $500 · winners featured on our YouTube & homepage", "Entries close 31 Jan 2027"),
                ("✍️", "My Lucky Number Story", "500–800 words: a number that changed your luck (phone, plate, date, price).", "Prize pool: $300 · winning stories published", "Rolling — quarterly winners")]
    ccards = "".join(f'<div class="card"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p><p style="margin-top:10px"><b>{p}</b></p><span class="tag red">{dl}</span></div>' for i, n, d, p, dl in contests)
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Contests &amp; prizes</span><h1>Create something lucky — win prizes</h1><p class="lead">Design contests, video challenges and story prizes for the Year of the Goat. Free to enter; winners are featured across 555185.com.</p>
<div class="cd" data-countdown="2026-12-15"></div><p class="muted" style="margin-top:6px">Countdown to the design contest deadline</p></div>
<div class="wrap"><div class="grid g3">{cards_or(ccards)}</div>{ad("inarticle")}
<div class="grid g2"><div class="card"><h2 class="mt0">Enter a contest</h2><form class="form" data-form="Contest entry">{HP}
<div><label>Contest *</label><select name="contest" required>{"".join(f"<option>{c[1]}</option>" for c in contests)}</select></div>
<div class="row2"><div><label>Name *</label><input name="name" required></div><div><label>Email *</label><input type="email" name="email" required></div></div>
<div class="row2"><div><label>Country *</label><input name="country" required></div><div><label>Age group *</label><select name="age" required><option>18+</option><option>Under 18 (guardian consent)</option></select></div></div>
<div><label>Entry title *</label><input name="title" required></div><div><label>Link to your entry * (Drive, Dropbox, YouTube, Google Doc)</label><input type="url" name="entry_url" required placeholder="https://"></div>
<div><label>Short description</label><textarea name="description"></textarea></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> My entry is my own original work, doesn’t copy anyone else’s design or trademark, and I accept the rules below. *</label>
<button class="btn" type="submit">Submit entry</button><p class="form-msg"></p></form></div>
<div class="card"><h2 class="mt0">Rules in brief</h2><ul><li>Free entry. No purchase or donation necessary.</li><li>One entry per person per contest.</li><li>Original work only — no copyrighted characters, logos or trademarks (including any third-party use of “555185”).</li><li>AI-assisted work must be disclosed.</li><li>Judging: creativity 40% · cultural authenticity 30% · craft 30%.</li><li>Winners announced within 30 days of closing and contacted by email.</li><li>Prizes paid by PayPal or bank transfer; winners handle any local taxes.</li><li>Void where prohibited. Full rules are published when each contest opens.</li></ul>
<h3>Sponsor a prize</h3><p>Put your brand on a contest prize and gallery. <a href="advertise.html">See sponsorship packages</a>.</p></div></div>
<h2 style="margin-top:28px">FAQ</h2>{faq_html(cfaq)}{ad("footer")}</div>'''
    out.append(("contests.html", page("contests.html", "Contests & Prizes — Red Envelope Design Contest 2027 | 555185",
        "Enter the 2027 Year of the Goat red envelope design contest, the best New Year greeting video challenge and the lucky number story prize. Free entry.", body, crumbs=[("", "Contests")], ld=faq_ld(cfaq))))

    # ---------------- CAREERS ----------------
    roles = [("Chinese–English content writer", "Freelance · Remote", "Write guides and meaning pages; native-level Mandarin or Cantonese plus fluent English."),
             ("YouTube / short-video creator", "Freelance · Remote", "Script, film or edit explainers on red envelopes, number slang and etiquette."),
             ("Illustrator / envelope designer", "Freelance · Remote", "Create zodiac and printable red envelope designs; foil-ready artwork a plus."),
             ("SEO &amp; growth marketer", "Part-time · Remote", "Own keyword strategy, seasonal campaigns and AdSense / RPM optimisation."),
             ("Partnerships &amp; sales (commission)", "Remote · Commission", "Bring on suppliers, sponsors and advertisers for Lunar New Year and wedding season."),
             ("Translator (Cantonese / Hokkien / Taiwanese)", "Freelance · Remote", "Localise guides for Hong Kong, Singapore, Malaysia and Taiwan audiences."),
             ("Community moderator", "Volunteer / paid stipend", "Moderate contest galleries and comments; help run giveaways.")]
    rcards = "".join(f'<div class="card"><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for n, t, d in roles)
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Careers &amp; talent</span><h1>Work with 555185</h1><p class="lead">We hire writers, creators, designers, translators and growth people — remote, flexible, paid per project. Bilingual and bicultural talent especially welcome.</p></div>
<div class="wrap"><div class="grid g3">{rcards}</div>
<div class="grid g2" style="margin-top:28px"><div class="card"><h2 class="mt0">Apply</h2><form class="form" data-form="Careers application">{HP}
<div><label>Role *</label><select name="role" required>{"".join(f"<option>{r[0]}</option>" for r in roles)}<option>Other / open application</option></select></div>
<div class="row2"><div><label>Name *</label><input name="name" required></div><div><label>Email *</label><input type="email" name="email" required></div></div>
<div class="row2"><div><label>Location / time zone *</label><input name="location" required></div><div><label>Languages</label><input name="languages" placeholder="e.g. English, Mandarin, Cantonese"></div></div>
<div><label>Portfolio / LinkedIn / CV link *</label><input type="url" name="portfolio" required placeholder="https://"></div>
<div class="row2"><div><label>Availability</label><select name="availability"><option>Under 10 h/week</option><option>10–20 h/week</option><option>20+ h/week</option><option>Project-based</option></select></div><div><label>Rate expectation</label><input name="rate" placeholder="per hour / per piece"></div></div>
<div><label>Why you?</label><textarea name="pitch"></textarea></div><button class="btn" type="submit">Send application</button><p class="form-msg"></p></form></div>
<div class="card"><h2 class="mt0">How we work</h2><ul class="check-list"><li>Remote, async, project-based</li><li>Clear briefs, fair rates, fast payment</li><li>Credit on published work</li><li>Seasonal peaks: Oct–Feb (Lunar New Year) and Apr–Oct (weddings)</li></ul><p>Funded partly by <a href="donate.html">supporters</a> — donations directly create paid briefs.</p></div></div>{ad("footer")}</div>'''
    out.append(("careers.html", page("careers.html", "Careers — Writers, Creators, Designers & Translators | 555185",
        "Remote freelance and part-time roles at 555185.com: Chinese–English writers, video creators, illustrators, SEO marketers, translators, partnerships and moderators.", body, crumbs=[("", "Careers")])))

    # ---------------- ADVERTISE ----------------
    pk = [("Seasonal takeover", "Lunar New Year (Nov–Feb)", ["Homepage &amp; tool hero placement", "Sponsored “Presented by” on the hongbao planner", "Newsletter feature", "Contest prize branding"]),
          ("Sponsored tool", "Quarterly", ["Your brand on one calculator", "Contextual CTA in results", "Monthly performance report"]),
          ("Directory &amp; leads", "Monthly", ["Priority supplier listing", "Matched quote requests in your area", "Profile in relevant guides"]),
          ("Content partnership", "Per project", ["Co-branded guide or video", "Disclosure-compliant sponsored content", "Social amplification"])]
    pcards = "".join(f'<div class="card tier{" pop" if i == 0 else ""}"><h3>{n}</h3><p class="muted">{t}</p><ul class="check-list">{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for i, (n, t, xs) in enumerate(pk))
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Advertise · Sponsor · Partner</span><h1>Reach people planning their Lunar New Year &amp; wedding spend</h1><p class="lead">Our visitors arrive with money decisions to make: how much to give, what to buy, whom to hire. Sponsorships, tool placements, supplier listings and content partnerships available.</p>
<p><a class="btn" href="{PARTNER}" target="_blank" rel="noopener">Contact via web.works/contact</a> <a class="btn ghost" href="#adform">Send a brief</a></p></div>
<div class="wrap"><div class="grid g4">{pcards}</div>
<div class="grid g3" style="margin-top:28px"><div class="card"><h3>Audience</h3><p>Diaspora families, couples, HR &amp; office managers, marketers and learners of Chinese across Asia, North America, the UK and Australia.</p></div><div class="card"><h3>Peak intent</h3><p>Lunar New Year (Oct–Feb), 520 Day (20 May), Qixi, wedding season and Singles’ Day.</p></div><div class="card"><h3>Brand-safe</h3><p>Family-friendly content, clear ad labelling, no gambling or lottery promotion.</p></div></div>
<div class="card" id="adform" style="margin-top:28px"><h2 class="mt0">Send an advertising / partnership brief</h2><form class="form" data-form="Advertising / sponsorship enquiry">{HP}
<div class="row2"><div><label>Company *</label><input name="company" required></div><div><label>Website</label><input type="url" name="website" placeholder="https://"></div></div>
<div class="row2"><div><label>Name *</label><input name="name" required></div><div><label>Email *</label><input type="email" name="email" required></div></div>
<div class="row2"><div><label>Interest *</label><select name="interest" required><option>Seasonal takeover</option><option>Sponsored tool</option><option>Directory &amp; leads</option><option>Content partnership</option><option>Contest prize sponsorship</option><option>Domain / website acquisition</option><option>Other partnership</option></select></div><div><label>Budget</label><select name="budget"><option>Under $1k</option><option>$1k–$5k</option><option>$5k–$20k</option><option>$20k+</option></select></div></div>
<div><label>Goals &amp; timing</label><textarea name="brief"></textarea></div><button class="btn" type="submit">Send brief</button><p class="form-msg"></p></form></div>{ad("footer")}</div>'''
    out.append(("advertise.html", page("advertise.html", "Advertise, Sponsor or Partner with 555185",
        "Sponsorships, tool placements, supplier listings and content partnerships reaching people planning Lunar New Year, wedding and Chinese-market spend.", body, crumbs=[("", "Advertise")])))

    # ---------------- VIDEOS ----------------
    cats = {}
    for v in VIDEOS: cats.setdefault(v[3], []).append(v)
    sections = "".join(f'<h2 style="margin-top:28px">{c}</h2><div class="grid g3">{"".join(vid(v) for v in vs)}</div>' + (ad("inarticle") if i == 1 else "") for i, (c, vs) in enumerate(cats.items()))
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Video library</span><h1>Red envelope &amp; Chinese number videos</h1><p class="lead">Hand-picked explainers on hongbao etiquette, weddings, lucky numbers, number slang and 大写 numerals. Videos load only when you press play (privacy-enhanced mode).</p><p><a class="btn sm" data-yt-channel target="_blank" rel="noopener">Subscribe on YouTube</a></p></div>
<div class="wrap">{sections}<p class="note" style="margin-top:24px">Videos are embedded from YouTube and remain the property of their creators. Creators: want your video featured or removed? <a href="contact.html">Contact us</a>.</p>{ad("footer")}</div>'''
    out.append(("videos.html", page("videos.html", "Videos: Red Envelope Etiquette, Chinese Lucky Numbers & Number Slang | 555185",
        "Watch the best videos on red envelope etiquette, Chinese wedding gifts, lucky and unlucky numbers, 520/555 number slang and Chinese financial numerals.", body, crumbs=[("", "Videos")])))

    # ---------------- ABOUT ----------------
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">About</span><h1>About 555185</h1><p class="lead">An independent guide to red envelopes, Chinese number culture and the money etiquette of Lunar New Year and weddings.</p></div>
<div class="wrap layout"><article class="prose"><h2>What we do</h2><p>We answer the questions people actually type at 11 pm before a family visit or a wedding banquet: <i>How much should I give? Is this number rude? What does 520 mean?</i> — with free tools, clear guides and honest ranges rather than one-size-fits-all rules.</p>
<h2>How we research</h2><ul><li>We compare published etiquette guides, community practice and regional differences (mainland China, Hong Kong, Taiwan, Singapore, Malaysia and the diaspora).</li><li>We present amounts as <b>ranges</b>, label them indicative, and update them each season.</li><li>Number meanings note when a reading is established slang versus a playful construction (like our own name).</li></ul>
<h2>How we’re funded</h2><p>Display advertising (clearly labelled), sponsorships, reader donations, and optional quote services that connect businesses and couples with suppliers. Sponsors never decide what our guides say.</p>
<h2>Corrections</h2><p>Spot something wrong or a regional custom we missed? <a href="contact.html">Tell us</a> — we credit helpful readers.</p>
<h2>Interested in this website or domain?</h2><p>For acquisition, sponsorship, advertising or partnership, please use <a href="{PARTNER}" target="_blank" rel="noopener">web.works/contact</a>.</p></article>{sidebar("./")}</div>'''
    out.append(("about.html", page("about.html", "About 555185 — Red Envelope & Chinese Number Guide", "About 555185.com: an independent guide to red envelopes, Chinese number culture and Lunar New Year and wedding money etiquette.", body, crumbs=[("", "About")])))

    # ---------------- CONTACT ----------------
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Contact</span><h1>Contact us</h1><p class="lead">Questions, corrections, partnership ideas or press — send a message and we’ll reply within 1–2 business days.</p></div>
<div class="wrap layout"><div class="card"><form class="form" data-form="Contact form">{HP}
<div class="row2"><div><label>Name *</label><input name="name" required autocomplete="name"></div><div><label>Email *</label><input type="email" name="email" required autocomplete="email"></div></div>
<div><label>Topic *</label><select name="topic" required><option>General question</option><option>Correction / suggestion</option><option>Quote request</option><option>Advertising / sponsorship</option><option>Domain / website acquisition</option><option>Partnership</option><option>Press</option><option>Contest</option><option>Careers</option></select></div>
<div><label>Message *</label><textarea name="message" required></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I accept the <a href="privacy.html">privacy policy</a>. *</label><button class="btn" type="submit">Send message</button><p class="form-msg"></p></form>
<p class="muted" style="margin-top:16px">Prefer your own email app? <a href="#" data-mail="555185.com enquiry">Email us</a>.</p></div>
<aside class="side"><div class="card"><h3>Domain, sponsorship, advertising or partnership</h3><p style="margin-bottom:12px">Interested in this website or the 555185.com domain?</p><a class="btn block" href="{PARTNER}" target="_blank" rel="noopener">web.works/contact</a></div>
<div class="card"><h3>Need a quote?</h3><p style="margin-bottom:12px">Use the dedicated form for faster matching.</p><a class="btn block ghost" href="quote.html">Get free quotes</a></div></aside></div>'''
    out.append(("contact.html", page("contact.html", "Contact 555185", "Contact 555185.com for questions, corrections, quotes, advertising, sponsorship, partnership or domain enquiries.", body, crumbs=[("", "Contact")], sticky=False)))

    # ---------------- LEGAL ----------------
    legal_body = f'''<h2 id="tm">Trademark disclosure</h2><p>“555185” is used on this website solely as a <b>descriptive numeral string</b> and as the subject of a cultural homophone reading (555 = crying in Chinese texting slang; 185 read playfully as 要发我). No trademark, service mark or exclusive right in the number “555185” or its component numbers (including 555, 185, 520, 1314, 888 or any other number code) is claimed, and none is implied.</p>
<p>This website is <b>independent</b>. It is not affiliated with, endorsed by or sponsored by any company, brand, product, telephone number, postal code, lottery, game or organisation that uses the same or similar digits. Any third-party trademarks, platform names (such as WeChat, Alipay, YouTube, PayPal, Ko-fi, Buy Me a Coffee and Stripe) and brand names mentioned belong to their respective owners and are used only for identification and description (nominative use).</p>
<h2 id="copyright">Copyright notice</h2><p>© 2026 555185.com. Original text, tool code, page design and compilations on this website are protected by copyright. You may quote short excerpts with a link back. Number codes, digit pronunciations, traditional customs and greetings are public cultural knowledge and are not claimed as proprietary. Embedded videos remain the property of their creators and are shown via YouTube’s standard embed. Open-source fonts are used under their licences.</p>
<h2 id="dmca">Copyright &amp; trademark complaints</h2><p>If you believe content here infringes your rights, please use our <a href="contact.html">contact form</a> with: the material concerned, its URL, your rights, and your contact details. We review and respond promptly and remove infringing material where appropriate.</p>
<h2 id="info">Information disclaimer</h2><p>Red-envelope amounts, wedding gift guidance and number meanings are <b>indicative cultural norms</b> compiled from published sources and community practice. They vary by family, region and occasion and are not financial, legal or religious advice. The luck score is a cultural heuristic for entertainment and naming decisions, not a prediction. Always verify formal financial numerals with your bank for cheques and contracts.</p>
<h2 id="affiliate">Advertising &amp; sponsorship disclosure</h2><p>This site displays advertising (e.g. Google AdSense), may feature sponsors and may earn referral fees when you request quotes from suppliers. Sponsored content is labelled. Contest participation and quotes never require a donation or purchase.</p>
<h2 id="domain">Domain enquiries</h2><p>For enquiries about this website, the domain name, sponsorship, advertising or partnership: <a href="{PARTNER}" target="_blank" rel="noopener">web.works/contact</a>.</p>'''
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Legal</span><h1>Trademark &amp; copyright disclosure</h1><p class="meta">Last updated {UPDATED}</p></div><div class="wrap layout"><article class="prose">{legal_body}</article>{sidebar("./")}</div>'''
    out.append(("legal.html", page("legal.html", "Trademark & Copyright Disclosure | 555185", "Trademark and copyright disclosure for 555185.com: no trademark claimed in the number 555185; independent site; copyright, takedown and disclaimer information.", body, crumbs=[("", "Legal")])))

    privacy = f'''<p>This policy explains what 555185.com collects and why.</p><h2>What we collect</h2><ul><li><b>Form submissions</b> (quotes, contact, contests, careers, donations, newsletter): the details you enter. Forms are delivered to our private inbox via the FormSubmit service.</li><li><b>Analytics</b> (if enabled): anonymised usage data via Google Analytics 4.</li><li><b>Advertising</b>: Google AdSense may use cookies to serve and measure ads, including personalised ads where permitted. Learn more at <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">Google’s ad policies</a>; manage settings at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ad Settings</a>.</li><li><b>Embedded video</b>: YouTube videos use privacy-enhanced mode and load only when you press play.</li><li><b>Local preferences</b>: theme choice is stored in your browser only.</li></ul>
<h2>How we use it</h2><p>To answer you, match quote requests with relevant suppliers (only the details needed), run contests, process applications and send newsletters you opted into. We never sell personal data.</p>
<h2>Your rights</h2><p>You can request access, correction or deletion of your data, or unsubscribe at any time, via the <a href="contact.html">contact form</a>. Residents of the EU/UK (GDPR), California (CCPA/CPRA), Canada (PIPEDA) and other jurisdictions have rights under local law, which we honour.</p>
<h2>Retention</h2><p>Enquiries are kept up to 24 months; contest and applicant data up to 12 months after the event, unless you ask us to delete it sooner.</p><h2>Children</h2><p>The site is general-audience. Contest entrants under 18 need guardian consent.</p><h2>Changes</h2><p>We’ll update this page and the date above when the policy changes.</p>'''
    out.append(("privacy.html", page("privacy.html", "Privacy Policy | 555185", "Privacy policy for 555185.com: forms, analytics, AdSense cookies, YouTube embeds and your data rights.",
        f'<div class="wrap page-hero">{{{{CRUMBS}}}}<h1>Privacy policy</h1><p class="meta">Last updated {UPDATED}</p></div><div class="wrap layout"><article class="prose">{privacy}</article>{sidebar("./")}</div>', crumbs=[("", "Privacy")])))
    terms = f'''<h2>Use of the site</h2><p>The tools and content are provided free, “as is”, for personal and business information. Don’t misuse the site, scrape it at scale or submit unlawful content.</p><h2>No advice</h2><p>Amounts, meanings and luck scores are indicative cultural information, not financial, legal or religious advice.</p><h2>Quotes &amp; suppliers</h2><p>Suppliers are independent. Any order is a contract between you and the supplier; review their terms. We may receive referral fees.</p><h2>Donations</h2><p>Donations support an independent publication, are voluntary and are not tax-deductible. Refunds on request within 14 days.</p><h2>Contests</h2><p>Governed by the official rules published for each contest. No purchase necessary. Void where prohibited.</p><h2>User submissions</h2><p>You confirm you own what you submit and grant us a non-exclusive licence to display it for the stated purpose.</p><h2>Liability</h2><p>To the extent permitted by law we’re not liable for indirect losses arising from use of the site.</p><h2>Contact</h2><p>Questions: <a href="contact.html">contact form</a>. Domain / partnership: <a href="{PARTNER}" target="_blank" rel="noopener">web.works/contact</a>.</p>'''
    out.append(("terms.html", page("terms.html", "Terms of Use | 555185", "Terms of use for 555185.com tools, content, quotes, donations, contests and submissions.",
        f'<div class="wrap page-hero">{{{{CRUMBS}}}}<h1>Terms of use</h1><p class="meta">Last updated {UPDATED}</p></div><div class="wrap layout"><article class="prose">{terms}</article>{sidebar("./")}</div>', crumbs=[("", "Terms")])))

    out.append(("thank-you.html", page("thank-you.html", "Thank you | 555185", "Your submission was received.",
        '''<div class="wrap page-hero center" style="padding:70px 16px"><div style="font-size:3.5rem">🧧</div><h1>Received — thank you!</h1><p class="lead">Your <b id="ty-form">message</b> is with us. We aim to reply within 1–2 business days.</p><p>From 555 to 185 — the good news is on its way.</p><div class="pills" style="justify-content:center"><a class="btn" href="tools/">Explore the free tools</a><a class="btn ghost" href="meanings/">Number codes</a><a class="btn ghost" href="donate.html">Support us</a></div>''' + ad("footer") + "</div>", sticky=False, noexit=True)))
    out.append(("404.html", page("404.html", "Page not found | 555185", "This page could not be found.",
        '''<div class="wrap page-hero center" style="padding:70px 16px"><div class="big">555…</div><h1>This page is crying (呜呜呜)</h1><p class="lead">We couldn’t find it. Try one of these instead:</p><div class="pills" style="justify-content:center"><a class="btn" href="./">Home</a><a class="btn ghost" href="tools/">Tools</a><a class="btn ghost" href="meanings/">Number codes</a><a class="btn ghost" href="guides/">Guides</a></div></div>''', sticky=False, noexit=True)))
    return out

def cards_or(x): return x
