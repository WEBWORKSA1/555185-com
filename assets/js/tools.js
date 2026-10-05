/* 555185.com — interactive tools */
(function () {
  const $ = (q, el = document) => el.querySelector(q), $$ = (q, el = document) => [...el.querySelectorAll(q)];
  const NUM = window.NUM; if (!NUM) return;
  const ROOT = document.body.dataset.root || './';
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fmt = (n, cur) => (cur || '') + Number(n).toLocaleString('en-US');

  /* ===== shared region data (indicative norms from published etiquette guides) ===== */
  const REGIONS = {
    CN: { name: 'Mainland China', cur: '¥', code: 'CNY', parity: 'even' },
    HK: { name: 'Hong Kong / Macau', cur: 'HK$', code: 'HKD', parity: 'even' },
    TW: { name: 'Taiwan', cur: 'NT$', code: 'TWD', parity: 'even' },
    SG: { name: 'Singapore', cur: 'S$', code: 'SGD', parity: 'even' },
    MY: { name: 'Malaysia', cur: 'RM', code: 'MYR', parity: 'even' },
    US: { name: 'USA / Canada', cur: '$', code: 'USD', parity: 'even' },
    UK: { name: 'UK / Europe', cur: '£', code: 'GBP', parity: 'even' },
    AU: { name: 'Australia / NZ', cur: 'A$', code: 'AUD', parity: 'even' }
  };
  // [low, high] per relationship, Lunar New Year
  const CNY = {
    kid:      { CN: [100, 200], HK: [20, 50],  TW: [600, 1200],  SG: [8, 10],  MY: [5, 10],  US: [10, 20], UK: [10, 20], AU: [10, 20] },
    niece:    { CN: [200, 500], HK: [50, 100], TW: [1200, 2000], SG: [10, 28], MY: [10, 20], US: [20, 50], UK: [20, 40], AU: [20, 50] },
    own:      { CN: [200, 1000], HK: [100, 500], TW: [2000, 6000], SG: [20, 88], MY: [20, 100], US: [20, 100], UK: [20, 80], AU: [20, 100] },
    parent:   { CN: [500, 2000], HK: [500, 2000], TW: [3600, 10000], SG: [100, 888], MY: [100, 500], US: [100, 500], UK: [80, 400], AU: [100, 500] },
    adult:    { CN: [200, 600], HK: [50, 100], TW: [1200, 2000], SG: [10, 20], MY: [10, 20], US: [20, 50], UK: [20, 40], AU: [20, 50] },
    employee: { CN: [100, 1000], HK: [50, 200], TW: [600, 3000], SG: [10, 50], MY: [10, 50], US: [20, 100], UK: [20, 80], AU: [20, 100] },
    service:  { CN: [50, 100], HK: [20, 50], TW: [200, 600], SG: [8, 10], MY: [5, 10], US: [20, 50], UK: [10, 30], AU: [20, 50] }
  };
  const REL = { kid: "Friends' / colleagues' young children", niece: 'Nieces & nephews', own: 'Your own children', parent: 'Parents & grandparents', adult: 'Unmarried adult relatives', employee: 'Employees / team', service: 'Service staff (doorman, cleaner, driver)' };

  function snapLucky(v, parity, region) {
    const r = NUM.luckyAmounts(v, { parity, lo: .8, hi: 1.25 });
    return r;
  }

  /* ===== 1) Hongbao planner ===== */
  const hb = $('#hb-tool');
  if (hb) {
    const reg = $('#hb-region'), lvl = $('#hb-level'), list = $('#hb-list'), out = $('#hb-out');
    Object.entries(REGIONS).forEach(([k, r]) => reg.add(new Option(r.name + ' (' + r.cur + ')', k)));
    const addRow = (rel = 'kid', n = 1) => {
      const row = document.createElement('div'); row.className = 'plan-row';
      row.innerHTML = '<select aria-label="Recipient type">' + Object.entries(REL).map(([k, v]) => '<option value="' + k + '"' + (k === rel ? ' selected' : '') + '>' + v + '</option>').join('') + '</select><input type="number" min="1" max="200" value="' + n + '" aria-label="How many"><button type="button" class="icon-btn" aria-label="Remove">✕</button>';
      $('button', row).onclick = () => { row.remove(); };
      list.appendChild(row);
    };
    addRow('kid', 3); addRow('parent', 2); addRow('niece', 2);
    $('#hb-add').onclick = () => addRow('adult', 1);
    $('#hb-go').onclick = () => {
      const R = REGIONS[reg.value], L = +lvl.value, married = $('#hb-married').checked;
      let total = 0; const rows = [];
      $$('.plan-row', list).forEach(r => {
        const rel = $('select', r).value, n = Math.max(1, +$('input', r).value || 1);
        const [lo, hi] = CNY[rel][reg.value]; const target = lo + (hi - lo) * L;
        const s = snapLucky(target, R.parity); const amt = s.recommended;
        total += amt * n; rows.push([REL[rel], n, amt, s.options]);
      });
      const recRegion = ['HK', 'SG', 'MY'].includes(reg.value);
      out.innerHTML = '<div class="muted">Your total red-envelope budget</div><div class="big">' + fmt(total, R.cur) + '</div>' +
        '<div class="tbl"><table><thead><tr><th>Recipient</th><th>Qty</th><th>Per envelope</th><th>Other lucky options</th></tr></thead><tbody>' +
        rows.map(r => '<tr><td>' + esc(r[0]) + '</td><td>' + r[1] + '</td><td><b>' + fmt(r[2], R.cur) + '</b></td><td>' + r[3].map(x => fmt(x, R.cur)).join(' · ') + '</td></tr>').join('') +
        '</tbody></table></div>' +
        '<p class="mb0"><b>Write it formally:</b> ' + esc(NUM.daxie(total, { cur: R.code === 'CNY' ? 'CNY' : R.code === 'HKD' ? 'HKD' : R.code === 'TWD' ? 'TWD' : 'none', trad: ['HKD', 'TWD'].includes(R.code) })) + (['CNY', 'HKD', 'TWD'].includes(R.code) ? '' : ' (' + R.code + ')') + '</p>' +
        (married && recRegion ? '<p class="note" style="margin-top:12px">In ' + R.name + ' married couples traditionally give, and in Hong Kong/Macau each spouse often gives a separate envelope — budget about double for close family.</p>' : '') +
        '<p class="muted" style="margin-top:10px;font-size:.85rem">Amounts avoid any 4 and 250, prefer 6/8/9 and even numbers. Indicative norms only — family custom wins.</p>' +
        '<div class="pills"><a class="btn sm" href="' + ROOT + 'quote.html#plan">Email me this plan + printable checklist</a> <a class="btn sm ghost" href="' + ROOT + 'quote.html#corporate">Need 100+ envelopes? Get a quote</a></div>';
      out.classList.add('on'); out.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    };
  }

  /* ===== 2) Wedding red envelope calculator ===== */
  const wd = $('#wd-tool');
  if (wd) {
    const PER_HEAD = { CN: [300, 500, 800], HK: [800, 1200, 1800], TW: [1600, 2200, 3200], SG: [120, 180, 250], MY: [100, 150, 250], US: [100, 150, 250], UK: [80, 120, 200], AU: [100, 150, 250] };
    const reg = $('#wd-region'), tier = $('#wd-tier'), per = $('#wd-perhead');
    Object.entries(REGIONS).forEach(([k, r]) => reg.add(new Option(r.name + ' (' + r.cur + ')', k)));
    const sync = () => { per.value = PER_HEAD[reg.value][+tier.value]; $('#wd-cur').textContent = REGIONS[reg.value].cur; };
    reg.onchange = sync; tier.onchange = sync; sync();
    $('#wd-go').onclick = () => {
      const R = REGIONS[reg.value], ph = Math.max(1, +per.value || 1), ppl = Math.max(1, +$('#wd-people').value || 1), mult = +$('#wd-close').value, att = $('#wd-attend').value;
      let base = ph * ppl * mult; if (att === 'no') base *= .6;
      const s = NUM.luckyAmounts(base, { parity: 'even', lo: .85, hi: 1.3 });
      const out = $('#wd-out');
      out.innerHTML = '<div class="muted">Recommended wedding red envelope</div><div class="big">' + fmt(s.recommended, R.cur) + '</div>' +
        '<div class="pills">' + s.options.map(x => '<span class="pill' + (x === s.recommended ? ' best' : '') + '">' + fmt(x, R.cur) + '</span>').join('') + '</div>' +
        '<dl class="kv"><dt>Logic</dt><dd>' + fmt(ph, R.cur) + ' per seat × ' + ppl + ' guest(s) × closeness ' + mult + (att === 'no' ? ' × 0.6 (not attending)' : '') + ' ≈ ' + fmt(Math.round(base), R.cur) + ', snapped to a lucky even amount</dd>' +
        '<dt>Formal (大写)</dt><dd>' + esc(NUM.daxie(s.recommended, { cur: ['CN'].includes(reg.value) ? 'CNY' : reg.value === 'HK' ? 'HKD' : reg.value === 'TW' ? 'TWD' : 'none', trad: ['HK', 'TW'].includes(reg.value) })) + '</dd></dl>' +
        '<p class="note" style="margin-top:12px">Rule of thumb across Chinese communities: your gift should at least cover your seat at the banquet. Even amounts only; never include a 4. For funerals use an odd amount in a white envelope (帛金).</p>' +
        '<div class="pills"><a class="btn sm" href="' + ROOT + 'quote.html#wedding">Planning your own wedding? Get vendor matches</a></div>';
      out.classList.add('on'); out.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    };
  }

  /* ===== 3) Number code decoder ===== */
  function renderDecode(target, val, compact) {
    const r = NUM.decode(val);
    if (!r.s) { target.innerHTML = '<p>Type some digits.</p>'; target.classList.add('on'); return; }
    const cls = r.score >= 65 ? 'Lucky' : r.score >= 45 ? 'Neutral' : 'Unlucky';
    const digitsHtml = '<div class="digits">' + r.digits.map(d => '<div class="digit' + (d.luck === 'lucky' ? ' g' : '') + '"><b>' + d.d + '</b><i>' + esc((d.py || '').split(' ')[0]) + '</i></div>').join('') + '</div>';
    const m = r.matches.length ? '<h4 style="margin:12px 0 6px">Codes found</h4><ul>' + r.matches.map(c => '<li><a href="' + ROOT + 'meanings/' + c.num + '.html"><b>' + c.num + '</b></a> = <span class="zh">' + esc(c.zh) + '</span> (' + esc(c.py) + ') — ' + esc(c.en) + '</li>').join('') + '</ul>' : '<p class="muted">No famous slang code inside — read it digit by digit below.</p>';
    const per = compact ? '' : '<h4 style="margin:12px 0 6px">Digit by digit</h4><ul>' + [...new Set(r.s)].map(d => { const x = r.digits.find(z => z.d === d); return '<li><b>' + d + '</b> <span class="zh">' + esc(x.zh || '') + '</span> ' + esc(x.py || '') + ' — sounds like ' + esc(x.sounds || '') + '</li>'; }).join('') + '</ul>';
    target.innerHTML = digitsHtml + '<div style="display:flex;justify-content:space-between;align-items:baseline;gap:10px"><b>Luck score: ' + r.score + '/100 · ' + cls + '</b></div><div class="score"><i style="width:' + r.score + '%"></i></div>' +
      (r.notes.length ? '<ul style="margin:8px 0">' + r.notes.map(n => '<li>' + esc(n) + '</li>').join('') + '</ul>' : '') + m + per;
    target.classList.add('on');
  }
  const dec = $('#dec-tool');
  if (dec) {
    const inp = $('#dec-in'), out = $('#dec-out');
    const run = () => renderDecode(out, inp.value, false);
    $('#dec-go').onclick = run; inp.addEventListener('keydown', e => { if (e.key === 'Enter') run(); });
    $$('[data-try]').forEach(b => b.onclick = () => { inp.value = b.dataset.try; run(); });
    const p = new URLSearchParams(location.search).get('n'); inp.value = p || '555185'; run();
  }
  const hd = $('#home-dec');
  if (hd) { const inp = $('#home-dec-in'), out = $('#home-dec-out'); const run = () => renderDecode(out, inp.value, true); $('#home-dec-go').onclick = run; inp.addEventListener('keydown', e => { if (e.key === 'Enter') run(); }); }

  /* ===== 4) 大写 converter ===== */
  const dx = $('#dx-tool');
  if (dx) {
    const inp = $('#dx-in'), cur = $('#dx-cur'), trad = $('#dx-trad'), pre = $('#dx-prefix');
    const run = () => {
      const v = inp.value.trim();
      const res = NUM.daxie(v, { cur: cur.value, trad: trad.checked, prefix: pre.checked });
      $('#dx-out').textContent = res || 'Enter a number up to 16 digits, with up to 2 decimals.';
      $('#dx-lower').textContent = v && /^\d/.test(v) ? NUM.lowerZh(v) : '—';
    };
    [inp, cur, trad, pre].forEach(el => el.addEventListener('input', run));
    cur.addEventListener('change', () => { if (['HKD', 'TWD'].includes(cur.value)) trad.checked = true; run(); });
    run();
  }

  /* ===== 5) Lucky amount & price finder ===== */
  const la = $('#la-tool');
  if (la) {
    const run = () => {
      const v = +$('#la-in').value, mode = $('#la-mode').value, c = $('#la-cur').value;
      if (!v) return;
      let r;
      if (mode === 'price') {
        r = NUM.luckyAmounts(v, { parity: 'any', lo: .85, hi: 1.15 });
      } else r = NUM.luckyAmounts(v, { parity: mode === 'funeral' ? 'odd' : 'even', lo: .75, hi: 1.3 });
      $('#la-out').innerHTML = '<div class="muted">' + (mode === 'price' ? 'Best price point near your target' : 'Best lucky amount near your budget') + '</div><div class="big">' + fmt(r.recommended, c) + '</div>' +
        '<div class="pills">' + r.options.map(x => '<span class="pill' + (x === r.recommended ? ' best' : '') + '">' + fmt(x, c) + '</span>').join('') + '</div>' +
        '<p class="muted" style="font-size:.88rem">' + (mode === 'funeral' ? 'Condolence money (帛金 / 白金) uses odd amounts in a white envelope, e.g. 101, 301, 501.' : mode === 'price' ? 'For Chinese-speaking shoppers, prices ending in 8 (发) or 6 (顺) outperform “.99” framing for gifts and premium goods; any 4 is avoided.' : 'Even amounts, no 4, no 250 — bonus points for 6, 8 and 9.') + '</p>' +
        (mode === 'price' ? '<a class="btn sm" href="' + ROOT + 'quote.html#market">Get a Chinese-market pricing review</a>' : '');
      $('#la-out').classList.add('on');
    };
    $('#la-go').onclick = run; $('#la-in').addEventListener('keydown', e => { if (e.key === 'Enter') run(); });
  }

  /* ===== 6) Greetings generator ===== */
  const gr = $('#gr-tool');
  if (gr) {
    const G = window.GREETINGS || [];
    const cat = $('#gr-cat'); [...new Set(G.map(g => g.c))].forEach(c => cat.add(new Option(c, c)));
    let cur = null;
    const show = () => {
      const pool = G.filter(g => !cat.value || g.c === cat.value); cur = pool[Math.floor(Math.random() * pool.length)];
      $('#gr-zh').textContent = cur.zh; $('#gr-py').textContent = cur.py; $('#gr-en').textContent = cur.en;
      $('#gr-list').innerHTML = pool.map(g => '<tr><td class="zh">' + esc(g.zh) + '</td><td>' + esc(g.py) + '</td><td>' + esc(g.en) + '</td></tr>').join('');
    };
    cat.onchange = show; $('#gr-go').onclick = show;
    $('#gr-copy').onclick = () => navigator.clipboard && navigator.clipboard.writeText(cur.zh + ' (' + cur.py + ') — ' + cur.en);
    $('#gr-card').onclick = () => {
      const cv = document.createElement('canvas'); cv.width = 1080; cv.height = 1350; const x = cv.getContext('2d');
      const g = x.createLinearGradient(0, 0, 0, 1350); g.addColorStop(0, '#C8102E'); g.addColorStop(1, '#8E0A1F'); x.fillStyle = g; x.fillRect(0, 0, 1080, 1350);
      x.strokeStyle = '#E5C25A'; x.lineWidth = 10; x.strokeRect(40, 40, 1000, 1270);
      x.fillStyle = '#FFD86B'; x.textAlign = 'center';
      x.font = 'bold 120px "PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif';
      wrap(x, cur.zh, 540, 560, 900, 140);
      x.font = '44px Georgia,serif'; x.fillStyle = '#FFE8A3'; wrap(x, cur.py, 540, 860, 900, 56);
      x.font = 'italic 40px Georgia,serif'; x.fillStyle = '#fff'; wrap(x, cur.en, 540, 1000, 900, 52);
      x.font = 'bold 34px sans-serif'; x.fillStyle = '#FFD86B'; x.fillText('555185.com', 540, 1250);
      const a = document.createElement('a'); a.download = 'greeting-555185.png'; a.href = cv.toDataURL('image/png'); a.click();
    };
    function wrap(ctx, text, cx, y, maxW, lh) {
      const cjk = /[一-鿿]/.test(text); const parts = cjk ? [...text] : text.split(' '); let line = '';
      for (const p of parts) { const t = line + (cjk || !line ? '' : ' ') + p; if (ctx.measureText(t).width > maxW && line) { ctx.fillText(line, cx, y); line = p; y += lh; } else line = t; }
      ctx.fillText(line, cx, y);
    }
    show();
  }

  /* ===== 7) Zodiac & CNY ===== */
  const zd = $('#zd-tool');
  if (zd) {
    fetch(ROOT + 'assets/data/cny.json').then(r => r.json()).then(cny => {
      const run = () => {
        const v = $('#zd-in').value; if (!v) return;
        const z = NUM.zodiacForDate(v, cny);
        $('#zd-out').innerHTML = '<div class="muted">Your Chinese zodiac sign</div><div class="big">' + z.element + ' ' + z.animal + ' <span class="zh">' + z.elementZh + z.animalZh + '</span></div><dl class="kv"><dt>Lunar year</dt><dd>' + z.lunarYear + ' (began ' + (cny[z.lunarYear] || '?') + ')</dd><dt>Polarity</dt><dd>' + z.yinyang + '</dd></dl><p class="muted" style="font-size:.88rem;margin-top:8px">Born in January or early February? Your sign follows the Lunar New Year date, not 1 January — this tool checks it for you.</p>';
        $('#zd-out').classList.add('on');
      };
      $('#zd-go').onclick = run;
      const tb = $('#zd-table');
      if (tb) { const y0 = new Date().getFullYear() - 1; let h = ''; for (let y = y0; y < y0 + 10; y++) { const z = NUM.zodiacYear(y); h += '<tr><td>' + y + '</td><td>' + (cny[y] || '') + '</td><td>' + z.element + ' ' + z.animal + ' <span class="zh">' + z.elementZh + z.animalZh + '</span></td></tr>'; } tb.innerHTML = h; }
    });
  }
})();
