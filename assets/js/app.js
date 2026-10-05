/* 555185.com — site behaviour: nav, theme, forms, ads, video, modal, countdown */
(function () {
  const S = window.SITE || {};
  const ROOT = document.body.dataset.root || './';
  const $ = (q, el = document) => el.querySelector(q), $$ = (q, el = document) => [...el.querySelectorAll(q)];
  const store = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, v); } catch (e) { } } };
  const sstore = { get(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { sessionStorage.setItem(k, v); } catch (e) { } } };
  const inbox = () => (S._k || []).slice().reverse().map(c => String.fromCharCode(c - S._o)).join('');

  /* theme */
  const saved = store.get('theme'); if (saved) document.documentElement.dataset.theme = saved;
  $$('[data-theme-toggle]').forEach(b => b.addEventListener('click', () => {
    const cur = document.documentElement.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    const nx = cur === 'dark' ? 'light' : 'dark'; document.documentElement.dataset.theme = nx; store.set('theme', nx);
  }));

  /* mobile nav */
  const mb = $('.menu-btn'), nav = $('.nav');
  if (mb && nav) mb.addEventListener('click', () => { const o = nav.classList.toggle('open'); mb.setAttribute('aria-expanded', o); });

  /* email links: built only on click, never rendered */
  $$('[data-mail]').forEach(a => a.addEventListener('click', e => {
    e.preventDefault(); const subj = encodeURIComponent(a.dataset.mail || '555185.com enquiry');
    location.href = 'mailto:' + inbox() + '?subject=' + subj;
  }));

  /* tabs */
  $$('[data-tabs]').forEach(wrap => {
    const tabs = $$('.tab', wrap), panels = $$('.panel', wrap.parentElement);
    const show = id => { tabs.forEach(t => t.setAttribute('aria-selected', t.dataset.tab === id)); panels.forEach(p => p.classList.toggle('on', p.id === id)); };
    tabs.forEach(t => t.addEventListener('click', () => { show(t.dataset.tab); history.replaceState(null, '', '#' + t.dataset.tab); }));
    const h = location.hash.slice(1); if (h && tabs.some(t => t.dataset.tab === h)) show(h);
  });

  /* chip groups → hidden input */
  $$('[data-chips]').forEach(g => {
    const input = $('input[type=hidden]', g), multi = g.dataset.chips === 'multi';
    $$('.chip', g).forEach(c => c.addEventListener('click', () => {
      if (!multi) $$('.chip', g).forEach(x => x.setAttribute('aria-pressed', 'false'));
      c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      if (input) input.value = $$('.chip[aria-pressed="true"]', g).map(x => x.dataset.v || x.textContent.trim()).join(', ');
    }));
  });

  /* multi-step forms */
  $$('form[data-steps]').forEach(f => {
    const steps = $$('.step', f), bar = $('.steps-bar', f); let i = 0;
    const render = () => { steps.forEach((s, k) => s.classList.toggle('on', k === i)); if (bar) $$('span', bar).forEach((s, k) => s.classList.toggle('on', k <= i)); };
    const valid = () => $$('input,select,textarea', steps[i]).every(el => el.reportValidity ? el.reportValidity() : true);
    $$('[data-next]', f).forEach(b => b.addEventListener('click', () => { if (valid() && i < steps.length - 1) { i++; render(); f.scrollIntoView({ behavior: 'smooth', block: 'start' }); } }));
    $$('[data-prev]', f).forEach(b => b.addEventListener('click', () => { if (i > 0) { i--; render(); } }));
    render();
  });

  /* form delivery (FormSubmit AJAX). The inbox is assembled at runtime only. */
  $$('form[data-form]').forEach(f => f.addEventListener('submit', async e => {
    e.preventDefault();
    const msg = $('.form-msg', f) || f.appendChild(Object.assign(document.createElement('p'), { className: 'form-msg' }));
    if ($('.hp input', f) && $('.hp input', f).value) return;
    const btn = $('button[type=submit]', f); const old = btn ? btn.textContent : '';
    const data = {}; new FormData(f).forEach((v, k) => { if (k !== '_hp' && !(v instanceof File)) data[k] = data[k] ? data[k] + ', ' + v : v; });
    data._subject = '[555185.com] ' + (f.dataset.form || 'Form') + (data.name ? ' — ' + data.name : '');
    data._template = 'table'; data._captcha = 'false'; data.page = location.href;
    if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
    try {
      const r = await fetch('https://formsubmit.co/ajax/' + inbox(), { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(data) });
      if (!r.ok) throw new Error('HTTP ' + r.status);
      if (window.gtag) gtag('event', 'generate_lead', { form: f.dataset.form });
      f.reset(); msg.className = 'form-msg ok'; msg.textContent = 'Received — thank you! Redirecting…';
      setTimeout(() => location.href = ROOT + 'thank-you.html?f=' + encodeURIComponent(f.dataset.form || ''), 700);
    } catch (err) {
      msg.className = 'form-msg err'; msg.innerHTML = 'Could not send right now. Please try again in a minute, or use the <a href="#" data-mail-fallback>email link</a>.';
      const fb = $('[data-mail-fallback]', msg); if (fb) fb.addEventListener('click', ev => { ev.preventDefault(); location.href = 'mailto:' + inbox() + '?subject=' + encodeURIComponent(data._subject) + '&body=' + encodeURIComponent(Object.entries(data).filter(([k]) => k[0] !== '_').map(([k, v]) => k + ': ' + v).join('\n')); });
    } finally { if (btn) { btn.disabled = false; btn.textContent = old; } }
  }));

  /* ads: AdSense when configured, otherwise rotating house ads */
  const HOUSE = [
    ['Ordering 100+ red envelopes for staff or clients?', 'Get free quotes for custom-printed hongbao & CNY gift boxes.', 'quote.html#corporate', 'Get a quote'],
    ['Planning a Chinese wedding or tea ceremony?', 'Get matched with vetted vendors — banquet, lion dance, décor.', 'quote.html#wedding', 'Find vendors'],
    ['Sponsor the 2027 Year of the Goat tools', 'Put your brand in front of an audience planning CNY spend.', 'advertise.html', 'See packages'],
    ['Keep 555185.com free', 'Send us a “lucky hongbao” — from $8.88.', 'donate.html', 'Support us'],
    ['Win a share of the 2027 contest prize pool', 'Design a red envelope or film your best New Year greeting.', 'contests.html', 'Enter now']
  ];
  let adsLoaded = false;
  $$('.ad[data-slot]').forEach((el, idx) => {
    const lbl = '<span class="ad-lbl">Advertisement</span>';
    if (S.ADSENSE_CLIENT) {
      if (!adsLoaded) { const sc = document.createElement('script'); sc.async = true; sc.crossOrigin = 'anonymous'; sc.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + S.ADSENSE_CLIENT; document.head.appendChild(sc); adsLoaded = true; }
      const slot = (S.ADSENSE_SLOTS || {})[el.dataset.slot] || '';
      el.innerHTML = lbl + '<ins class="adsbygoogle" style="display:block" data-ad-client="' + S.ADSENSE_CLIENT + '"' + (slot ? ' data-ad-slot="' + slot + '"' : '') + ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) { }
    } else {
      const h = HOUSE[(idx + new Date().getDate()) % HOUSE.length];
      el.innerHTML = '<span class="ad-lbl">Sponsored</span><div class="house"><div><b>' + h[0] + '</b><br><span class="muted">' + h[1] + '</span></div><a class="btn sm" href="' + ROOT + h[2] + '">' + h[3] + '</a></div>';
    }
  });

  /* GA4 */
  if (S.GA4_ID) { const g = document.createElement('script'); g.async = true; g.src = 'https://www.googletagmanager.com/gtag/js?id=' + S.GA4_ID; document.head.appendChild(g); window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag('js', new Date()); gtag('config', S.GA4_ID); }

  /* YouTube facade */
  $$('.vid[data-id]').forEach(v => {
    const id = v.dataset.id;
    v.innerHTML = '<img loading="lazy" alt="' + (v.dataset.title || 'Video') + '" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><div class="play"><span>▶</span></div>';
    v.setAttribute('role', 'button'); v.tabIndex = 0;
    const go = () => { v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.dataset.title || 'Video') + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; };
    v.addEventListener('click', go, { once: true }); v.addEventListener('keydown', e => { if (e.key === 'Enter') go(); });
  });
  $$('[data-yt-channel]').forEach(a => { if (S.YOUTUBE_CHANNEL) a.href = S.YOUTUBE_CHANNEL; else a.style.display = 'none'; });

  /* donation links */
  $$('[data-donate]').forEach(a => { const u = (S.DONATE || {})[a.dataset.donate]; if (u) a.href = u; else a.style.display = 'none'; });
  const anyDonate = Object.values(S.DONATE || {}).some(Boolean);
  $$('[data-donate-none]').forEach(el => el.style.display = anyDonate ? 'none' : '');

  /* modal + exit intent */
  const modal = $('#lead-modal');
  const open = () => { if (modal) { modal.classList.add('on'); sstore.set('lm', '1'); } };
  const close = () => modal && modal.classList.remove('on');
  $$('[data-open-modal]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); open(); }));
  if (modal) {
    $$('.x,[data-close]', modal).forEach(b => b.addEventListener('click', close));
    modal.addEventListener('click', e => { if (e.target === modal) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
    if (!document.body.hasAttribute('data-no-exit')) {
      document.addEventListener('mouseout', e => { if (!e.relatedTarget && e.clientY < 8 && !sstore.get('lm') && innerWidth > 900) open(); });
    }
  }

  /* sticky CTA */
  const st = $('.sticky-cta');
  if (st && !sstore.get('stx')) {
    addEventListener('scroll', () => { const p = scrollY / (document.body.scrollHeight - innerHeight); st.classList.toggle('on', p > .35 && !sstore.get('stx')); }, { passive: true });
    const x = $('button', st); if (x) x.addEventListener('click', () => { sstore.set('stx', '1'); st.classList.remove('on'); });
  }

  /* countdown */
  $$('[data-countdown]').forEach(el => {
    const t = new Date(el.dataset.countdown + 'T00:00:00').getTime();
    const tick = () => { let d = Math.max(0, t - Date.now()); const u = [86400000, 3600000, 60000, 1000].map(x => { const v = Math.floor(d / x); d -= v * x; return v; });
      el.innerHTML = ['Days', 'Hours', 'Mins', 'Secs'].map((l, k) => '<div><b>' + u[k] + '</b><span>' + l + '</span></div>').join(''); };
    tick(); setInterval(tick, 1000);
  });

  /* copy buttons */
  $$('[data-copy]').forEach(b => b.addEventListener('click', () => {
    const el = $(b.dataset.copy); const txt = el ? (el.value || el.textContent) : '';
    navigator.clipboard && navigator.clipboard.writeText(txt).then(() => { const o = b.textContent; b.textContent = 'Copied!'; setTimeout(() => b.textContent = o, 1200); });
  }));

  /* meanings filter */
  const q = $('#num-search');
  if (q) q.addEventListener('input', () => { const v = q.value.trim().toLowerCase(); $$('.num-card').forEach(c => c.style.display = !v || c.textContent.toLowerCase().includes(v) ? '' : 'none'); });

  /* thank-you personalisation */
  const ty = $('#ty-form'); if (ty) { const f = new URLSearchParams(location.search).get('f'); if (f) ty.textContent = f; }

  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
