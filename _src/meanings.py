from layout import page, ad, sidebar, faq_html, faq_ld, esc
from numdata import DIGITS, CODES

VERDICT = {
 "lucky": ("✅ Great for gifts, prices & numbers", "This is a positive number in Chinese culture — safe and welcome as a red-envelope amount, price ending, phone number or plate."),
 "love": ("💞 Romantic — perfect between couples", "Use it for anniversaries, 520 Day, proposals and wedding gifts. Less suited to business or elders."),
 "slang": ("💬 Chat slang — fun, not for gifts", "It’s internet shorthand. Fine in messages and usernames, but it carries no particular luck as an amount."),
 "unlucky": ("⛔ Avoid for gifts and numbers", "Its reading is negative. Don’t use it as a red-envelope amount, a price or a number you want to show off."),
 "mixed": ("⚖️ Depends on context", "Its meaning shifts with dialect and context — check how your audience reads it before using it commercially."),
 "neutral": ("➖ Neutral", "No strong luck either way; meaning comes from the digits around it."),
}

def code_dict(c):
    num, zh, py, en, luck, cat, desc, exzh, exen = c
    return dict(num=num, zh=zh, py=py, en=en, luck=luck, cat=cat, desc=desc, exzh=exzh, exen=exen)

def build():
    out = []
    codes = [code_dict(c) for c in CODES]
    r = "../"
    # index
    groups = {}
    for c in codes: groups.setdefault(c["cat"], []).append(c)
    digit_cards = "".join(f'<a class="num-card" href="{d}.html"><b>{d}</b><span class="zh">{DIGITS[d]["zh"]}</span> <span>{DIGITS[d]["py"]} · {DIGITS[d]["luck"]}</span></a>' for d in DIGITS)
    code_cards = "".join(f'<a class="num-card" href="{c["num"]}.html"><b>{c["num"]}</b><span class="zh">{esc(c["zh"])}</span><br><span>{esc(c["en"])}</span></a>' for c in codes)
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Dictionary</span><h1>Chinese number codes &amp; meanings</h1>
<p class="lead">From 555 (crying) and 520 (I love you) to 888 (triple prosperity) and 250 (idiot) — {len(codes)} number codes plus all ten digits, with pinyin, homophones and whether they’re safe for gifts.</p>
<input class="search" id="num-search" type="search" placeholder="Search a number or meaning… e.g. 520, love, prosper" aria-label="Search number codes"></div>
<div class="wrap"><h2>The ten digits</h2><div class="num-grid">{digit_cards}</div>{ad("inarticle")}
<h2 style="margin-top:28px">Number codes</h2><div class="num-grid">{code_cards}</div>
<div class="band" style="margin-top:32px"><div><h2>Got a number to decode?</h2><p>Phone number, licence plate, price, date or a mystery chat message — get the slang, homophones and luck score.</p></div><div><a class="btn gold" href="../tools/number-code-decoder.html">Open the decoder</a></div></div>{ad("footer")}</div>'''
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Chinese number codes", "hasDefinedTerm": [{"@type": "DefinedTerm", "name": c["num"], "description": c["en"]} for c in codes]}
    out.append(("meanings/index.html", page("meanings/index.html", "Chinese Number Meanings & Slang Dictionary — 555, 520, 1314, 888, 250 | 555185",
        "What numbers mean in Chinese: 555 crying, 520 I love you, 1314 forever, 666 awesome, 888 prosperity, 250 idiot, 4 death. Pinyin, homophones and gift safety for every code.", body, crumbs=[("", "Number codes")], ld=ld)))

    # digits
    for d, v in DIGITS.items():
        rel = [c for c in codes if d in c["num"]][:8]
        vt, vd = VERDICT[v["luck"]]
        faqs = [(f"What does the number {d} mean in Chinese?", f"{d} is {v['zh']} ({v['py']}). It sounds like {v['sounds']}. {v['note']}"),
                (f"Is {d} a lucky number in China?", f"{vt.split(' ',1)[1]}. {vd}")]
        content = f'''<div class="decode" style="text-align:center"><div class="big">{d}</div><div class="zh" style="font-size:2rem">{v["zh"]}</div><p class="mb0">{v["py"]}</p></div>
<h2>Sounds like</h2><p>{esc(v["sounds"])}</p><h2>Meaning &amp; culture</h2><p>{esc(v["note"])}</p>
<div class="note"><b>{vt}</b><br>{vd}</div>{ad("inarticle")}
<h2>Codes that contain {d}</h2><div class="num-grid">{"".join(f'<a class="num-card" href="{c["num"]}.html"><b>{c["num"]}</b><span>{esc(c["en"])}</span></a>' for c in rel) or "<p>None in the dictionary yet.</p>"}</div>
<h2>FAQ</h2>{faq_html(faqs)}'''
        body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Digit</span><h1>Number {d} in Chinese: {v["zh"]} ({v["py"]})</h1><p class="lead">{esc(v["note"].split(". ")[0])}.</p></div>
<div class="wrap layout"><article class="prose">{content}</article>{sidebar(r)}</div>'''
        out.append((f"meanings/{d}.html", page(f"meanings/{d}.html", f"Number {d} Meaning in Chinese ({v['zh']} {v['py']}) — Lucky or Unlucky? | 555185",
            f"What does {d} mean in Chinese? {v['zh']} ({v['py']}) sounds like {v['sounds']}. Luck, culture and codes that use {d}.", body,
            crumbs=[("meanings/", "Number codes"), ("", f"Digit {d}")], ld=faq_ld(faqs))))

    # codes
    for c in codes:
        rel = [x for x in codes if x["cat"] == c["cat"] and x["num"] != c["num"]][:6]
        if len(rel) < 4: rel += [x for x in codes if x["luck"] == c["luck"] and x not in rel and x["num"] != c["num"]][:6 - len(rel)]
        vt, vd = VERDICT[c["luck"]]
        rows = "".join(f'<tr><td><b>{ch}</b></td><td class="zh">{DIGITS[ch]["zh"]}</td><td>{DIGITS[ch]["py"]}</td><td>{esc(DIGITS[ch]["sounds"])}</td></tr>' for ch in dict.fromkeys(c["num"]))
        faqs = [(f"What does {c['num']} mean in Chinese?", f"{c['num']} means “{c['en']}” — it is read as {c['zh']} ({c['py']}). {c['desc'].split('. ')[0]}."),
                (f"Can I use {c['num']} as a red envelope amount?", f"{vt.split(' ',1)[1]}. {vd}"),
                (f"How do you pronounce {c['num']}?", f"Digit by digit in Mandarin: {' '.join(DIGITS[ch]['py'].split(' / ')[0] for ch in c['num'])}. The phrase it imitates is {c['zh']} ({c['py']}).")]
        story = '<p><a class="btn" href="../the-555185-story.html">Read the full 555185 story</a></p>' if c["num"] in ("555", "185", "555185") else ""
        content = f'''<div class="decode" style="text-align:center"><div class="digits">{"".join(f'<div class="digit{" g" if DIGITS[ch]["luck"]=="lucky" else ""}"><b>{ch}</b><i>{DIGITS[ch]["py"].split(" / ")[0]}</i></div>' for ch in c["num"])}</div>
<div class="zh" style="font-size:2rem">{esc(c["zh"])}</div><p class="mb0">{esc(c["py"])} — <b>{esc(c["en"])}</b></p></div>
<h2>What {c["num"]} means</h2><p>{esc(c["desc"])}</p>{story}
<blockquote><span class="zh">{esc(c["exzh"])}</span><br><i>{esc(c["exen"])}</i></blockquote>
<div class="note"><b>{vt}</b><br>{vd}</div>{ad("inarticle")}
<h2>Digit breakdown</h2><div class="tbl"><table><thead><tr><th>Digit</th><th>Character</th><th>Pinyin</th><th>Sounds like</th></tr></thead><tbody>{rows}</tbody></table></div>
<p><a class="btn sm ghost" href="../tools/number-code-decoder.html?n={c["num"]}">Analyse {c["num"]} in the decoder →</a></p>
<h2>Related codes</h2><div class="num-grid">{"".join(f'<a class="num-card" href="{x["num"]}.html"><b>{x["num"]}</b><span>{esc(x["en"])}</span></a>' for x in rel)}</div>
<h2>FAQ</h2>{faq_html(faqs)}'''
        body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">{esc(c["cat"])} code</span><h1>What does {c["num"]} mean in Chinese?</h1><p class="lead"><b>{c["num"]}</b> = <span class="zh">{esc(c["zh"])}</span> ({esc(c["py"])}) — {esc(c["en"])}.</p></div>
<div class="wrap layout"><article class="prose">{content}</article>{sidebar(r)}</div>'''
        out.append((f"meanings/{c['num']}.html", page(f"meanings/{c['num']}.html", f"{c['num']} Meaning in Chinese — {c['zh']} ({c['en']}) | 555185",
            f"What does {c['num']} mean in Chinese? {c['num']} = {c['zh']} ({c['py']}): {c['en']}. Pronunciation, usage examples and whether it’s lucky.", body,
            crumbs=[("meanings/", "Number codes"), ("", c["num"])], ld=faq_ld(faqs))))
    return out, codes
