import json, html
DOMAIN = "https://555185.com"
PARTNER = "https://web.works/contact"
UPDATED = "October 2026"
JEKYLL = True  # emit Jekyll pages (front matter + body) using _layouts/default.html and _includes/sidebar.html

NAV = [("tools/", "Tools"), ("meanings/", "Number Codes"), ("guides/", "Guides"), ("videos.html", "Videos"),
       ("contests.html", "Contests"), ("donate.html", "Donate")]

def esc(s): return html.escape(s, quote=True)

def root_for(path):
    depth = path.count("/")
    return "../" * depth if depth else "./"

def ad(slot="inarticle"):
    return f'<div class="ad" data-slot="{slot}" aria-label="Advertisement"></div>'

def lead_card(r, title="Get your free Hongbao Plan", sub="Personalised amounts for everyone on your list + printable 2027 checklist."):
    return f'''<div class="card"><span class="tag red">Free</span><h3>{title}</h3><p style="margin-bottom:12px">{sub}</p>
<form class="form" data-form="Sidebar lead — Hongbao Plan"><div class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></div>
<input name="name" placeholder="First name" required aria-label="First name"><input type="email" name="email" placeholder="Email" required aria-label="Email">
<select name="region" aria-label="Region"><option>Mainland China</option><option>Hong Kong / Macau</option><option>Taiwan</option><option>Singapore</option><option>Malaysia</option><option>USA / Canada</option><option>UK / Europe</option><option>Australia / NZ</option></select>
<button class="btn block" type="submit">Send my plan</button><p class="form-msg muted" style="font-size:.78rem;margin:0">No spam. Unsubscribe anytime.</p></form></div>'''

def sidebar(r):
    if JEKYLL and not r.startswith("{{"):
        return '{% endraw %}{% include sidebar.html r="' + r + '" %}{% raw %}'
    return sidebar_html(r)

def sidebar_html(r):
    return f'''<aside class="side"><div class="sticky">{lead_card(r)}
<div class="card"><h3>Popular tools</h3><ul>
<li><a href="{r}tools/hongbao-calculator.html">Red envelope planner</a></li>
<li><a href="{r}tools/wedding-red-envelope-calculator.html">Wedding gift calculator</a></li>
<li><a href="{r}tools/number-code-decoder.html">Number code decoder</a></li>
<li><a href="{r}tools/chinese-financial-numerals.html">大写 numeral converter</a></li>
<li><a href="{r}tools/lucky-amount-finder.html">Lucky amount & price finder</a></li></ul></div>
{ad("sidebar")}
<div class="card"><h3>Business or wedding?</h3><p style="margin-bottom:12px">Custom-printed envelopes, corporate CNY gifting and vetted wedding vendors.</p><a class="btn block" href="{r}quote.html">Get free quotes</a></div>
</div></aside>'''

def faq_html(faqs):
    return "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in faqs)

def faq_ld(faqs):
    import re
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]}

def page(path, title, desc, body, *, crumbs=None, ld=None, sticky=True, noexit=False, og_type="website", hero=None):
    r = root_for(path)
    url = DOMAIN + "/" + (path[:-10] if path.endswith("index.html") else path)
    ld_all = [{"@context": "https://schema.org", "@type": "WebSite", "name": "555185", "url": DOMAIN + "/",
               "potentialAction": {"@type": "SearchAction", "target": DOMAIN + "/tools/number-code-decoder.html?n={n}", "query-input": "required name=n"}}]
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
        for i, (u, n) in enumerate(crumbs):
            items.append({"@type": "ListItem", "position": i + 2, "name": n, "item": DOMAIN + "/" + u if u else url})
        ld_all.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if ld: ld_all += ld if isinstance(ld, list) else [ld]
    crumb_html = ""
    if crumbs:
        parts = [f'<a href="{r}">Home</a>'] + [f'<a href="{r}{u}">{esc(n)}</a>' if u else esc(n) for u, n in crumbs]
        crumb_html = '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(parts) + "</nav>"
    body = body.replace("{{CRUMBS}}", crumb_html).replace("{{R}}", r)
    ld_script = '<script type="application/ld+json">' + json.dumps(ld_all, ensure_ascii=False) + '</script>'
    section = next((u.rstrip("/") for u, n in NAV if path.startswith(u.rstrip("/"))), "")
    if JEKYLL:
        fm = dict(layout="default", title=title, description=desc, canonical=url, r=("" if path == "404.html" else r), og_type=og_type,
                  sticky=sticky, noexit=noexit, section=section, is404=(path == "404.html"))
        return "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fm.items()) + "---\n{% raw %}" + ld_script + "\n" + body + "{% endraw %}\n"
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{r}{u}"{cur if u.rstrip("/") == section else ""}>{n}</a>' for u, n in NAV)
    sticky_html = STICKY if sticky else ""
    return shell(r, esc(title), esc(desc), url, og_type, ld_script, nav, body, sticky_html, " data-no-exit" if noexit else "", "")

STICKY = '<div class="sticky-cta" role="complementary"><span>🧧 Free 2027 red-envelope cheat sheet</span><a class="btn sm gold" href="#" data-open-modal>Get it</a><button aria-label="Dismiss">✕</button></div>'

def layout_file():
    nav = "".join(f'<a href="{{{{ page.r }}}}{u}"{{% if page.section == "{u.rstrip("/")}" %}} aria-current="page"{{% endif %}}>{n}</a>' for u, n in NAV)
    base404 = '{% if page.is404 %}<script>document.write(\'<base href="\'+(location.pathname.indexOf("/555185-com/")===0?"/555185-com/":"/")+\'">\')</script>{% endif %}'
    return shell("{{ page.r }}", "{{ page.title | escape }}", "{{ page.description | escape }}", "{{ page.canonical }}", "{{ page.og_type }}", "",
                 nav, "{{ content }}", "{% if page.sticky %}" + STICKY + "{% endif %}", "{% if page.noexit %} data-no-exit{% endif %}", base404)

def include_sidebar():
    return sidebar_html("{{ include.r }}")

def shell(r, title, desc, url, og_type, ld_script, nav, body, sticky_html, noexit_attr, head_extra):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">{head_extra}
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="555185">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#C8102E">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{ld_script}
</head>
<body data-root="{r}"{noexit_attr}>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a href="{PARTNER}" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{r}" aria-label="555185 home"><span class="mark">🧧</span><span>555185<small>RED ENVELOPE &amp; NUMBER CODES</small></span></a>
<button class="icon-btn menu-btn" aria-label="Menu" aria-expanded="false">☰</button>
<nav class="nav" aria-label="Main">{nav}<a class="btn sm" href="{r}quote.html">Get a Free Quote</a><button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode" style="margin-left:6px">◐</button></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="ftr"><div class="wrap">
<div class="cols">
<div><a class="logo" href="{r}" style="color:#fff"><span class="mark">🧧</span><span>555185<small style="color:#aaa">FROM 555 TO 185</small></span></a>
<p style="margin-top:12px">Free red-envelope calculators, Chinese number-code meanings and Lunar New Year etiquette — plus vetted help for weddings and business gifting.</p>
<form class="news" data-form="Newsletter"><div class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></div><input type="email" name="email" placeholder="Your email" required aria-label="Email for newsletter"><button class="btn sm" type="submit">Join</button></form>
<p class="form-msg" style="font-size:.8rem;margin-top:6px"></p></div>
<div><h4>Tools</h4><ul><li><a href="{r}tools/hongbao-calculator.html">Red envelope planner</a></li><li><a href="{r}tools/wedding-red-envelope-calculator.html">Wedding gift calculator</a></li><li><a href="{r}tools/number-code-decoder.html">Number decoder</a></li><li><a href="{r}tools/chinese-financial-numerals.html">大写 converter</a></li><li><a href="{r}tools/lucky-amount-finder.html">Lucky amounts</a></li><li><a href="{r}tools/greetings-generator.html">Greetings</a></li><li><a href="{r}tools/zodiac-cny-countdown.html">Zodiac &amp; CNY</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{r}meanings/">Number code dictionary</a></li><li><a href="{r}guides/">All guides</a></li><li><a href="{r}guides/red-envelope-etiquette.html">Hongbao etiquette</a></li><li><a href="{r}guides/chinese-wedding-red-envelope-guide.html">Wedding envelopes</a></li><li><a href="{r}the-555185-story.html">The 555185 story</a></li><li><a href="{r}videos.html">Videos</a></li></ul></div>
<div><h4>Get involved</h4><ul><li><a href="{r}quote.html">Get a free quote</a></li><li><a href="{r}donate.html">Donate</a></li><li><a href="{r}contests.html">Contests &amp; prizes</a></li><li><a href="{r}careers.html">Careers / talent</a></li><li><a href="{r}advertise.html">Advertise &amp; sponsor</a></li><li><a href="{PARTNER}" target="_blank" rel="noopener">Buy / partner on this domain</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{r}about.html">About</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{r}legal.html">Trademark &amp; copyright</a></li><li><a href="{r}privacy.html">Privacy</a></li><li><a href="{r}terms.html">Terms</a></li><li><a href="{r}sitemap.xml">Sitemap</a></li></ul></div>
</div>
<div class="legal-note">© <span data-year>2026</span> 555185.com. “555185” is used here only as a descriptive numeral string and homophone reading; no trademark rights in the number are claimed, and this site is not affiliated with any company, product, phone number or lottery that uses the same digits. Third-party names and video content belong to their owners. Etiquette amounts are indicative norms, not financial advice. <a href="{r}legal.html">Full disclosure</a>.</div>
</div></footer>
<div class="modal" id="lead-modal" role="dialog" aria-modal="true" aria-labelledby="lm-t"><div class="box"><button class="x" aria-label="Close">×</button>
<span class="tag red">Free download</span><h2 id="lm-t" style="font-size:1.6rem">The 2027 Year of the Goat red-envelope cheat sheet</h2>
<p>Amounts by relationship for 8 regions, the lucky/unlucky number list, 30 greetings with pinyin and a printable checklist. Lunar New Year 2027 is on <b>6 February</b>.</p>
<form class="form" data-form="Lead magnet — 2027 cheat sheet"><div class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></div><input name="name" placeholder="First name" required aria-label="First name"><input type="email" name="email" placeholder="Email address" required aria-label="Email"><label class="check"><input type="checkbox" name="b2b" value="yes"> I also buy red envelopes / gifts for a business</label><button class="btn block" type="submit">Send me the cheat sheet</button><p class="form-msg muted" style="font-size:.8rem;margin:0">We send it by email. No spam, unsubscribe anytime.</p></form></div></div>
{sticky_html}
<script src="{r}assets/js/config.js"></script>
<script src="{r}assets/js/numdata.js"></script>
<script src="{r}assets/js/numbers.js"></script>
<script src="{r}assets/js/app.js"></script>
<script src="{r}assets/js/tools.js"></script>
</body>
</html>
'''

def article(path, title, h1, desc, crumbs, intro, content, *, faqs=None, extra_ld=None, eyebrow="Guide", toc=None):
    ld = []
    ld.append({"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc, "dateModified": "2026-10-05",
               "author": {"@type": "Organization", "name": "555185 Editorial"}, "publisher": {"@type": "Organization", "name": "555185"}})
    if faqs: ld.append(faq_ld(faqs))
    if extra_ld: ld += extra_ld
    r = root_for(path)
    toc_html = ""
    if toc:
        toc_html = '<nav class="toc" aria-label="Contents"><b>On this page</b><ol>' + "".join(f'<li><a href="#{a}">{esc(t)}</a></li>' for a, t in toc) + "</ol></nav>"
    faq_block = f'<h2 id="faq">Frequently asked questions</h2>{faq_html(faqs)}' if faqs else ""
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{intro}</p><p class="meta">By 555185 Editorial · Updated {UPDATED}</p></div>
<div class="wrap layout"><article class="prose">{toc_html}{ad("top")}{content}{faq_block}{ad("footer")}</article>{sidebar(r)}</div>'''
    return page(path, title, desc, body, crumbs=crumbs, ld=ld, og_type="article")
