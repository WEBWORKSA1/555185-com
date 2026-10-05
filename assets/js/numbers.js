/* 555185.com — number intelligence engine (pure functions, no DOM). Requires numdata.js */
(function (G) {
  const N = G.NUMDATA || { digits: {}, codes: [] };
  const SPECIAL = { 8: 4, 88: 6, 888: 9, 8888: 12, 6: 2, 66: 4, 666: 7, 6666: 9, 9: 2, 99: 4, 999: 6, 168: 6, 1688: 8, 188: 6, 288: 5, 388: 5, 588: 6, 688: 6, 988: 6, 1888: 8, 2888: 7, 3888: 7, 5888: 7, 6888: 8, 8888: 12, 520: 6, 1314: 6, 518: 6, 1188: 6, 1288: 6, 1388: 6, 1588: 6, 1600: 4, 2200: 4, 3600: 4, 6600: 6, 9999: 8, 108: 4, 128: 4 };

  /* ---------- luck scoring for any digit string ---------- */
  function luck(str) {
    const s = String(str).replace(/\D/g, '');
    if (!s) return { score: 0, notes: [] };
    let pts = 0; const notes = [];
    for (const d of s) {
      if (d === '8') pts += 3; else if (d === '6') pts += 2; else if (d === '9') pts += 2;
      else if (d === '2') pts += 1; else if (d === '4') pts -= 4; else if (d === '3') pts += 0;
    }
    const love = N.codes.find(c => c.num === s && c.luck === 'love');
    if (/4/.test(s) && !love) notes.push('Contains 4 (sì ≈ 死, death) — the most avoided digit.');
    if (/250/.test(s)) { pts -= 6; notes.push('Contains 250 (二百五, “idiot”).'); }
    if (/14|74/.test(s) && !love) { pts -= 3; notes.push('Contains 14 / 74 (要死 / 气死 readings).'); }
    if (/888|666|999|168|518/.test(s)) { pts += 4; notes.push('Contains a famous lucky sequence.'); }
    if (/(\d)\1\1/.test(s)) { pts += 2; notes.push('Has a repeating triple — easy to remember, prized in phone numbers.'); }
    if (/8$/.test(s)) { pts += 2; notes.push('Ends in 8 (发, prosper) — the strongest ending.'); }
    if (/555/.test(s)) notes.push('555 = 呜呜呜 (crying) in texting slang — fun, not unlucky.');
    if (love) { pts += 6; notes.push('Recognised love code: ' + love.zh + ' (' + love.en + ').'); }
    const max = s.length * 3 + 10;
    let score = Math.round(50 + (pts / max) * 50);
    score = Math.max(1, Math.min(99, score));
    return { score, notes };
  }

  /* ---------- decoder: digit-by-digit + slang matches ---------- */
  function decode(str) {
    const s = String(str).replace(/\D/g, '').slice(0, 24);
    const digits = [...s].map(d => ({ d, ...(N.digits[d] || {}) }));
    const codes = [...N.codes].sort((a, b) => b.num.length - a.num.length);
    const matches = []; const used = new Array(s.length).fill(false);
    const exact = N.codes.find(c => c.num === s);
    if (exact) { matches.push({ at: 0, ...exact }); used.fill(true); }
    for (const c of codes) {
      if (c.num.length < 2) continue;
      let i = s.indexOf(c.num);
      while (i !== -1) {
        let free = true; for (let k = i; k < i + c.num.length; k++) if (used[k]) free = false;
        if (free) { for (let k = i; k < i + c.num.length; k++) used[k] = true; matches.push({ at: i, ...c }); }
        i = s.indexOf(c.num, i + 1);
      }
    }
    matches.sort((a, b) => a.at - b.at);
    return { s, digits, matches, exact, ...luck(s) };
  }

  /* ---------- lucky amount search ---------- */
  function amountScore(n, parity) {
    const s = String(n);
    if (/4/.test(s) && !(n === 1314)) return -999;
    if (/250/.test(s)) return -999;
    if (parity === 'even' && n % 2) return -999;
    if (parity === 'odd' && n % 2 === 0) return -999;
    let p = SPECIAL[n] || 0;
    for (const d of s) { if (d === '8') p += 1.6; else if (d === '6' || d === '9') p += 1.1; }
    const tail = s.replace(/0+$/, '');
    const messy = [...tail.slice(1)].filter(d => !'0689'.includes(d) && !(d === tail[0])).length;
    p -= messy * 1.6;
    if (/^(\d)\1+$/.test(s)) p += 2;
    return p;
  }
  function luckyAmounts(target, opts = {}) {
    target = Math.max(1, Math.round(+target || 0));
    const parity = opts.parity || 'any';
    const lo = Math.max(1, Math.floor(target * (opts.lo || 0.72))), hi = Math.ceil(target * (opts.hi || 1.38));
    const mag = Math.pow(10, Math.max(0, String(target).length - 2));
    const step = Math.max(1, mag / (target >= 100 ? 10 : 1));
    const seen = new Set(); const out = [];
    const add = n => { if (n < lo || n > hi || seen.has(n)) return; seen.add(n); const sc = amountScore(n, parity); if (sc > -100) out.push({ n, sc: sc - Math.abs(n - target) / target * 6 }); };
    for (let n = Math.floor(lo / step) * step; n <= hi; n += step) add(n);
    Object.keys(SPECIAL).forEach(k => add(+k));
    for (let d = 1; d <= 9; d++) for (let m = 1; m <= 100000; m *= 10) add(d * m);
    out.sort((a, b) => b.sc - a.sc);
    const best = out.slice(0, 6).map(o => o.n).sort((a, b) => a - b);
    const rec = out.length ? out[0].n : target;
    return { recommended: rec, options: best };
  }

  /* ---------- 大写 financial numerals ---------- */
  function daxie(input, o = {}) {
    const trad = !!o.trad, cur = o.cur || 'CNY';
    const D = trad ? '零壹貳參肆伍陸柒捌玖' : '零壹贰叁肆伍陆柒捌玖';
    const U = ['', '拾', '佰', '仟'], B = trad ? ['', '萬', '億', '兆'] : ['', '万', '亿', '兆'];
    let raw = String(input).replace(/[,\s]/g, '');
    if (!/^\d+(\.\d{0,2})?$/.test(raw)) return '';
    let [ip, dp = ''] = raw.split('.'); dp = (dp + '00').slice(0, 2);
    ip = ip.replace(/^0+(?=\d)/, '');
    if (ip.length > 16) return '';
    const intWords = groupWords(ip, D, U, B, D[0]);
    const unitYuan = cur === 'HKD' ? '圓' : (trad ? '圓' : '元');
    const [j, f] = [+dp[0], +dp[1]];
    const jiao = cur === 'HKD' ? '毫' : '角', fen = cur === 'HKD' ? '仙' : '分';
    if (cur === 'none') return intWords || D[0];
    let out = '';
    if (+ip > 0) out += intWords + unitYuan;
    if (j > 0) out += (+ip > 0 && /0$/.test(ip) ? D[0] : '') + D[j] + jiao;
    if (f > 0) out += ((j === 0 && +ip > 0) ? D[0] : '') + D[f] + fen;
    if (!out) out = D[0] + unitYuan;
    if (f === 0) out += '整';
    const prefix = cur === 'CNY' ? (trad ? '人民幣' : '人民币') : cur === 'HKD' ? '港幣' : cur === 'TWD' ? '新臺幣' : '';
    return (o.prefix ? prefix : '') + out;
  }
  function groupWords(ip, D, U, B, Z) {
    if (!+ip) return '';
    const groups = []; for (let i = ip.length; i > 0; i -= 4) groups.unshift(ip.slice(Math.max(0, i - 4), i));
    let res = '', zero = false;
    groups.forEach((g, idx) => {
      const gi = groups.length - 1 - idx; const v = +g;
      if (!v) { if (res) zero = true; return; }
      if (res && v < 1000) zero = true;
      const p = g.padStart(4, '0'); let s = '', z = false, started = false;
      for (let i = 0; i < 4; i++) { const d = +p[i]; if (!d) { if (started) z = true; } else { if (z) { s += Z; z = false; } s += D[d] + U[3 - i]; started = true; } }
      res += (zero ? Z : '') + s + B[gi]; zero = false;
    });
    return res;
  }
  function lowerZh(n) {
    const s = String(Math.floor(Math.abs(+n) || 0));
    let w = groupWords(s, '零一二三四五六七八九', ['', '十', '百', '千'], ['', '万', '亿', '兆'], '零') || '零';
    return w.replace(/^一十/, '十');
  }

  /* ---------- CNY + zodiac ---------- */
  const ANIMALS = [['Rat', '鼠'], ['Ox', '牛'], ['Tiger', '虎'], ['Rabbit', '兔'], ['Dragon', '龙'], ['Snake', '蛇'], ['Horse', '马'], ['Goat', '羊'], ['Monkey', '猴'], ['Rooster', '鸡'], ['Dog', '狗'], ['Pig', '猪']];
  const ELEMENTS = [['Metal', '金'], ['Water', '水'], ['Wood', '木'], ['Fire', '火'], ['Earth', '土']];
  function zodiacYear(y) { const a = ANIMALS[((y - 4) % 12 + 12) % 12]; const e = ELEMENTS[Math.floor((((y % 10) + 10) % 10) / 2)]; return { animal: a[0], animalZh: a[1], element: e[0], elementZh: e[1], yinyang: y % 2 ? 'Yin' : 'Yang' }; }
  function zodiacForDate(dateStr, cny) {
    const d = new Date(dateStr + 'T12:00:00'); let y = d.getFullYear();
    const ny = cny && cny[y] ? new Date(cny[y] + 'T00:00:00') : null;
    if (ny && d < ny) y -= 1;
    return { lunarYear: y, ...zodiacYear(y) };
  }

  G.NUM = { luck, decode, luckyAmounts, amountScore, daxie, lowerZh, zodiacYear, zodiacForDate };
})(window);
