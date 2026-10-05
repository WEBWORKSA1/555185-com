from layout import article, page, ad, esc

G = []  # (slug, icon, title, short)

def add(slug, icon, card, short, title, h1, desc, intro, content, faqs, toc=None):
    G.append((slug, icon, card, short, title, h1, desc, intro, content, faqs, toc))

add("red-envelope-etiquette", "🧧", "Red envelope etiquette", "Who gives, who receives, how much, and the taboos — the complete guide.",
 "Red Envelope Etiquette 2027: The Complete Hongbao Guide (Who, How Much, Taboos) | 555185",
 "Red envelope etiquette: the complete hongbao guide",
 "Hongbao (红包) / lai see (利是) / ang pao etiquette explained: who gives red envelopes, how much money to put in, how to give and receive, lucky and unlucky amounts and modern digital red packets.",
 "Who gives, who receives, how much to put inside, how to hand it over — and the mistakes that quietly offend. Everything you need before Lunar New Year 2027.",
 '''<h2 id="what">What is a red envelope?</h2><p>A red envelope — <b>hóngbāo</b> (红包) in Mandarin, <b>lai see</b> (利是) in Cantonese, <b>ang pao</b> in Hokkien — is a red paper packet holding money, given at Lunar New Year, weddings, birthdays, full-month baby celebrations, business openings and as workplace bonuses. Red symbolises luck and wards off evil; the money inside carries a wish for prosperity. The <i>gesture</i> matters more than the sum, but the sum is still judged — which is why the number rules below matter.</p>
<h2 id="who">Who gives and who receives</h2><ul><li><b>Married adults → children</b> and unmarried younger relatives. Marriage is the traditional line between receiver and giver.</li><li><b>Working adults → parents and grandparents</b>, as filial thanks — often the largest envelopes of the year.</li><li><b>Employers → employees</b> (year-end or first-day-back “开工” envelopes) and building staff, cleaners, drivers.</li><li><b>Guests → the couple</b> at weddings; relatives at a baby’s full-month (满月) party; friends at a business opening.</li></ul>
<blockquote>In Hong Kong and Macau, many families expect <b>each spouse</b> to give a separate envelope — so a married couple hands out two.</blockquote>
<h2 id="how-much">How much to put in</h2><div class="tbl"><table><thead><tr><th>Recipient</th><th>Mainland China</th><th>Hong Kong</th><th>Singapore / Malaysia</th><th>North America</th></tr></thead><tbody>
<tr><td>Friends’ young children</td><td>¥100–200</td><td>HK$20–50</td><td>S$8–10 / RM5–10</td><td>$10–20</td></tr>
<tr><td>Nieces &amp; nephews</td><td>¥200–500</td><td>HK$50–100</td><td>S$10–28 / RM10–20</td><td>$20–50</td></tr>
<tr><td>Parents &amp; grandparents</td><td>¥500–2,000</td><td>HK$500–2,000</td><td>S$100–888 / RM100–500</td><td>$100–500</td></tr>
<tr><td>Employees</td><td>¥100–1,000</td><td>HK$50–200</td><td>S$10–50 / RM10–50</td><td>$20–100</td></tr>
<tr><td>Wedding guest gift</td><td>¥600–2,000+</td><td>≈ banquet cost/head</td><td>“Market rate” per seat</td><td>$100–300</td></tr></tbody></table></div>
<p>Plan your whole list in the <a href="../tools/hongbao-calculator.html">red envelope planner</a> — it snaps every amount to a lucky number automatically.</p>
<h2 id="numbers">Lucky and unlucky amounts</h2><ul><li><b>Choose:</b> 6 (smooth), 8 (prosper), 9 (long-lasting), and even totals — 66, 88, 168, 188, 288, 666, 888, 1,688.</li><li><b>Avoid:</b> any 4 (sounds like death), 250 (“idiot”) and odd amounts (funerals).</li><li><b>Romantic exceptions:</b> 520 (I love you) and 1,314 (forever).</li></ul><p>See the <a href="lucky-and-unlucky-numbers.html">full lucky number guide</a>.</p>
<h2 id="giving">How to give and receive</h2><ol><li>Use <b>new, crisp notes</b> — banks run out of new notes before New Year, so withdraw early.</li><li>Don’t put coins in (except tiny symbolic ones in some regions) and never use a white envelope for celebrations.</li><li><b>Give and receive with both hands</b>, with a greeting like 恭喜发财 (gōngxǐ fācái).</li><li>Receivers say thank you and a blessing; <b>don’t open it in front of the giver</b>.</li><li>Give during the 15 days of the New Year period, ideally on visits in the first days.</li></ol>
<h2 id="digital">Digital red packets</h2><p>Since WeChat launched red packets in 2014, sending hongbao by app has become mainstream in mainland China — Tencent reported 768 million people sending and receiving them during the 2018 holiday. The same number rules apply on screen. Read <a href="digital-red-packets-wechat-alipay.html">how digital red packets work</a>.</p>''',
 [("Who should give red envelopes?", "Married adults give to children and unmarried younger relatives; working adults give to parents and grandparents; employers give to staff. In Hong Kong each spouse may give separately."),
  ("Can I open a red envelope right away?", "Not in front of the giver — it’s considered impolite. Say thank you and a blessing and open it later."),
  ("What do I write on a red envelope?", "For New Year you can leave it blank or add a blessing like 恭喜发财. For weddings, write your name and a blessing such as 百年好合 so the family can record your gift."),
  ("Is it rude to give a small amount?", "No — for children of acquaintances small symbolic amounts are normal (especially in Hong Kong). What’s rude is an unlucky number, old notes or skipping someone in a group.")],
 toc=[("what", "What is a red envelope?"), ("who", "Who gives and receives"), ("how-much", "How much to put in"), ("numbers", "Lucky & unlucky amounts"), ("giving", "How to give & receive"), ("digital", "Digital red packets"), ("faq", "FAQ")])

add("chinese-wedding-red-envelope-guide", "💍", "Chinese wedding red envelopes", "Guest gifts, tea ceremony, door games, betrothal money and 改口费 explained.",
 "Chinese Wedding Red Envelope Guide: How Much to Give, Tea Ceremony & Betrothal (2027) | 555185",
 "The Chinese wedding red envelope guide",
 "How much to give at a Chinese wedding, plus every wedding red envelope explained: guest gift (礼金), tea ceremony, door games (开门利是), betrothal money (聘金) and 改口费.",
 "A Chinese wedding can involve half a dozen different red envelopes. Here’s what each one is for, who gives it, and what amounts are customary.",
 '''<h2 id="guest">1. The guest red envelope (礼金)</h2><p>The one most people need. Guests bring a red envelope to the banquet and hand it in at the reception table, where it is usually recorded. The traditional benchmark: <b>cover the cost of your seat</b>, then add more for closer relationships. Write your name and a blessing (百年好合, 永结同心) on the front.</p>
<div class="tbl"><table><thead><tr><th>Relationship</th><th>Guideline</th></tr></thead><tbody><tr><td>Colleague / acquaintance</td><td>About the cost of your seat</td></tr><tr><td>Friend</td><td>Seat cost, rounded up to a lucky number</td></tr><tr><td>Close friend</td><td>~1.3× seat cost</td></tr><tr><td>Relative</td><td>~1.5× seat cost or more</td></tr><tr><td>Close family</td><td>Significantly more — follow family custom</td></tr></tbody></table></div>
<p>Run your numbers in the <a href="../tools/wedding-red-envelope-calculator.html">wedding red envelope calculator</a>.</p>
<h2 id="door">2. Door games (开门利是 / 接亲)</h2><p>On the wedding morning the groom and groomsmen arrive to collect the bride, and the bridesmaids block the door with games until the groom pays “door-opening” red envelopes. Amounts are playful and often use lucky numbers like 99 or 999 (long-lasting) — prepare a stack of small envelopes.</p>
<h2 id="tea">3. The tea ceremony (敬茶)</h2><p>The couple serve tea to parents and elders, who in return give red envelopes or gold jewellery. Elders’ envelopes vary widely by family and region; they are a blessing on the new household rather than a market rate.</p>
<h2 id="gaikou">4. 改口费 — the “change of address” gift</h2><p>In many mainland families, when the bride (or groom) first calls their in-laws “Mum” and “Dad”, the in-laws give a red envelope called 改口费 (gǎikǒu fèi). Symbolic amounts such as ¥10,001 (万里挑一, “one in ten thousand”) or ¥1,001 (千里挑一) are popular.</p>
<h2 id="betrothal">5. Betrothal money (聘金) and gifts (过大礼)</h2><p>Before the wedding, the groom’s family presents betrothal gifts and money to the bride’s family — in Cantonese tradition this is 过大礼. Amounts are highly family- and region-specific and are often partly returned as a gesture of goodwill. Use auspicious numbers (e.g. sequences of 8 or 9) and avoid 4.</p>
<h2 id="rules">Universal rules</h2><ul><li>Even amounts only — weddings are about pairs.</li><li>No 4 anywhere, no 250.</li><li>New notes, red envelope (gold lettering is ideal).</li><li>Couples give one envelope sized for two seats.</li><li>Can’t attend? Still send an envelope, usually somewhat smaller.</li></ul>
<div class="band"><div><h2>Planning your own Chinese wedding?</h2><p>Get matched with banquet venues, tea-ceremony sets, lion dance troupes, custom envelopes and planners.</p></div><div><a class="btn gold" href="../quote.html#wedding">Get vendor matches</a></div></div>''',
 [("How much money do you give at a Chinese wedding?", "At least the cost of your banquet seat, adjusted for closeness — roughly ¥600–2,000 in mainland China, HK$1,000–2,000 in Hong Kong, S$120–250 in Singapore, or $100–300 in North America."),
  ("Who gives red envelopes at the tea ceremony?", "Parents and elders give red envelopes (or jewellery) to the couple after being served tea."),
  ("What is 改口费?", "A red envelope from parents-in-law to the bride or groom when they first address them as Mum and Dad. ¥10,001 (万里挑一) is a popular symbolic amount."),
  ("Should the amount be odd or even?", "Always even for weddings. Odd amounts are used for funerals.")],
 toc=[("guest", "Guest envelope"), ("door", "Door games"), ("tea", "Tea ceremony"), ("gaikou", "改口费"), ("betrothal", "Betrothal money"), ("rules", "Universal rules"), ("faq", "FAQ")])

add("how-much-to-give-by-region", "🌏", "Amounts by country", "China, Hong Kong, Taiwan, Singapore, Malaysia, US, UK, Australia.",
 "How Much to Give in a Red Envelope by Country (China, HK, Taiwan, Singapore, Malaysia, US, UK) | 555185",
 "How much to give in a red envelope — by country",
 "Red envelope amounts by country and relationship: mainland China, Hong Kong, Taiwan, Singapore, Malaysia, USA, Canada, UK and Australia — with local lucky-number customs.",
 "Red envelope norms vary enormously: a Hong Kong lai see for a child might be HK$20, while a mainland relative may give ¥500. Here’s the local picture.",
 '''<h2 id="cn">Mainland China (¥)</h2><p>The largest amounts. Children of friends ¥100–200; nieces and nephews ¥200–500; parents ¥500–2,000+. Tier-1 cities (Beijing, Shanghai, Shenzhen) run higher, and Guangdong is famously more modest. Digital red packets via WeChat and Alipay are the norm, especially for relatives far away.</p>
<h2 id="hk">Hong Kong &amp; Macau (HK$ / MOP)</h2><p>Lots of small envelopes rather than a few large ones. Acquaintances’ children and building staff often get HK$20–50; close family HK$100–500; parents much more. Each spouse in a married couple commonly gives separately. On the first working day, bosses give staff 开工利是.</p>
<h2 id="tw">Taiwan (NT$)</h2><p>Even amounts based on 600, 1,200, 1,600, 2,000, 3,600 and 6,600 are common; 6 (smooth) is popular. Avoid 4,000 at all costs. Adults commonly give to parents (孝亲红包) — often several thousand NT$.</p>
<h2 id="sg">Singapore (S$)</h2><p>Ang pao for children are typically S$8–10, close relatives S$10–50, parents S$100+. Singapore banks promote “e-ang pao” and pre-loved notes to cut waste. For weddings, guests follow the venue’s per-seat “market rate”.</p>
<h2 id="my">Malaysia (RM)</h2><p>Children RM5–10 is customary; closer relatives RM10–50; parents RM100+. Malaysia also has duit raya (green packets) for Hari Raya — the same spirit across cultures.</p>
<h2 id="west">USA, Canada, UK &amp; Australia</h2><p>Diaspora families commonly use $10–20 for children, $20–50 for nieces/nephews and $100+ for parents (A$ and £ similarly). Weddings: $100–300 per guest. Many families mix cash with digital transfers.</p>
<div class="tbl"><table><thead><tr><th>Region</th><th>Child of friend</th><th>Close relative child</th><th>Parents</th></tr></thead><tbody>
<tr><td>Mainland China</td><td>¥100–200</td><td>¥200–500</td><td>¥500–2,000</td></tr><tr><td>Hong Kong</td><td>HK$20–50</td><td>HK$50–100</td><td>HK$500–2,000</td></tr><tr><td>Taiwan</td><td>NT$600–1,200</td><td>NT$1,200–2,000</td><td>NT$3,600–10,000</td></tr><tr><td>Singapore</td><td>S$8–10</td><td>S$10–28</td><td>S$100–888</td></tr><tr><td>Malaysia</td><td>RM5–10</td><td>RM10–20</td><td>RM100–500</td></tr><tr><td>USA / Canada</td><td>$10–20</td><td>$20–50</td><td>$100–500</td></tr></tbody></table></div>
<p class="note">Ranges are indicative norms compiled from published etiquette guides and community practice. Use the <a href="../tools/hongbao-calculator.html">planner</a> to tailor them.</p>''',
 [("Why are Hong Kong red envelopes so small?", "Hong Kong custom favours giving many small lai see — to children, staff, doormen and colleagues — so individual amounts stay modest while the total can be large."),
  ("Do Singaporeans use new notes?", "Traditionally yes, but banks and the Monetary Authority of Singapore have encouraged e-ang pao and ‘good-as-new’ notes to reduce waste."),
  ("What’s the Taiwan custom for parents?", "Working adult children give 孝亲红包 (filial red envelopes) to parents — commonly several thousand NT$, in even, 4-free amounts.")],
 toc=[("cn", "Mainland China"), ("hk", "Hong Kong & Macau"), ("tw", "Taiwan"), ("sg", "Singapore"), ("my", "Malaysia"), ("west", "Western countries"), ("faq", "FAQ")])

add("digital-red-packets-wechat-alipay", "📱", "Digital red packets", "How WeChat, Alipay and e-lai see red packets work.",
 "Digital Red Packets Explained: WeChat, Alipay & e-Hongbao Etiquette | 555185",
 "Digital red packets: WeChat, Alipay &amp; e-hongbao",
 "How digital red envelopes work on WeChat and Alipay, group ‘grab’ red packets, limits, etiquette and how overseas families send e-hongbao.",
 "In 2014 WeChat turned the red envelope into a social game. Today digital hongbao are how hundreds of millions of people celebrate — here’s how they work.",
 '''<h2 id="history">From paper to phone</h2><p>WeChat launched red packets in January 2014, and Alipay followed. The killer feature was the <b>group “lucky draw” red packet</b> (拼手气红包): one person puts in a total, chooses how many packets, and group members race to grab a random share. It turned gift-giving into entertainment. Tencent reported that 768 million people sent and received WeChat red packets over the 2018 Spring Festival holiday.</p>
<h2 id="types">Types of digital red packet</h2><ul><li><b>Personal red packet</b> — a fixed amount to one person, with a message. Couples send ¥520 on 20 May.</li><li><b>Group lucky-draw packet</b> — random splits; the luckiest grab is crowned 手气最佳.</li><li><b>Equal-split group packet</b> — everyone gets the same.</li><li><b>Corporate / brand packets</b> — companies use cover designs and campaigns to reach customers.</li></ul>
<h2 id="etiquette">Etiquette on screen</h2><ul><li>Number rules still apply: avoid 4, prefer 6/8/9, 520 for love.</li><li>Send a thank-you or emoji after grabbing a group packet; lurking and grabbing everything is frowned upon.</li><li>Don’t send a digital packet to elders who expect a face-to-face envelope.</li><li>WeChat caps a single personal red packet at ¥200 — except on special days when romantic amounts like ¥520 are allowed — so larger gifts use a transfer (转账) instead.</li></ul>
<h2 id="overseas">Sending e-hongbao from abroad</h2><p>Overseas family members often use WeChat Pay with a linked international card (where supported), bank transfers, or local e-wallets (PayNow in Singapore, FPS/PayMe in Hong Kong). Choose the amount first with the <a href="../tools/lucky-amount-finder.html">lucky amount finder</a>.</p>
<div class="band"><div><h2>Brand campaigns with red packets</h2><p>Running a Lunar New Year promotion for Chinese-speaking customers? Get help with red-packet campaigns, lucky pricing and creative.</p></div><div><a class="btn gold" href="../quote.html#market">Talk to a specialist</a></div></div>''',
 [("When did WeChat red packets start?", "January 2014. Alipay launched its own soon after, and Alipay’s ‘Collect Five Fortunes’ (集五福) New Year campaign followed in 2016."),
  ("What is a 拼手气 red packet?", "A group red packet that splits a total randomly among the people who grab it — the biggest share wins the 手气最佳 (‘best luck’) crown."),
  ("Is there a limit on WeChat red packets?", "A single personal red packet is generally capped at ¥200, so larger gifts are sent as transfers. Limits can change — check the app.")],
 toc=[("history", "From paper to phone"), ("types", "Types"), ("etiquette", "Etiquette"), ("overseas", "Sending from abroad"), ("faq", "FAQ")])

add("chinese-number-slang", "💬", "Chinese number slang", "555, 520, 1314, 666, 886, 233 and more — the texting code.",
 "Chinese Number Slang Guide: 555, 520, 1314, 666, 886, 233 Explained | 555185",
 "Chinese number slang: the complete texting code",
 "Chinese internet number slang explained: 555 (crying), 520 (I love you), 1314 (forever), 666 (awesome), 886 (bye), 233 (LOL), 748, 995 and more — with pinyin and examples.",
 "Chinese texters turn digits into words using sound-alikes. Learn the twenty codes you’ll see everywhere — starting with the one in our name.",
 '''<h2 id="how">Why numbers become words</h2><p>Mandarin has relatively few distinct syllables, so many words sound alike. Typing digits was faster than typing characters on early phones and QQ, and a culture of number puns took off. Read a code aloud and listen for the phrase: <b>5-2-0</b> wǔ-èr-líng ≈ wǒ-ài-nǐ (我爱你).</p>
<h2 id="emotion">Emotions</h2><div class="tbl"><table><thead><tr><th>Code</th><th>Reads as</th><th>Meaning</th></tr></thead><tbody>
<tr><td><a href="../meanings/555.html">555</a></td><td>呜呜呜</td><td>Crying, boo-hoo</td></tr><tr><td><a href="../meanings/233.html">233</a></td><td>(Mop emoticon #233)</td><td>LOL</td></tr><tr><td><a href="../meanings/7456.html">7456</a></td><td>气死我了</td><td>I’m so angry</td></tr><tr><td><a href="../meanings/995.html">995</a></td><td>救救我</td><td>Help me</td></tr></tbody></table></div>
<h2 id="love">Love</h2><div class="tbl"><table><thead><tr><th>Code</th><th>Reads as</th><th>Meaning</th></tr></thead><tbody>
<tr><td><a href="../meanings/520.html">520</a></td><td>我爱你</td><td>I love you</td></tr><tr><td><a href="../meanings/1314.html">1314</a></td><td>一生一世</td><td>Forever</td></tr><tr><td><a href="../meanings/5201314.html">5201314</a></td><td>我爱你一生一世</td><td>I love you forever</td></tr><tr><td><a href="../meanings/530.html">530</a></td><td>我想你</td><td>I miss you</td></tr><tr><td><a href="../meanings/9420.html">9420</a></td><td>就是爱你</td><td>Just love you</td></tr><tr><td><a href="../meanings/7758258.html">7758258</a></td><td>亲亲我吧爱我吧</td><td>Kiss me, love me</td></tr></tbody></table></div>
<h2 id="everyday">Everyday chat</h2><div class="tbl"><table><thead><tr><th>Code</th><th>Reads as</th><th>Meaning</th></tr></thead><tbody>
<tr><td><a href="../meanings/88.html">88</a> / <a href="../meanings/886.html">886</a></td><td>拜拜(了)</td><td>Bye-bye</td></tr><tr><td><a href="../meanings/666.html">666</a></td><td>溜溜溜</td><td>Awesome!</td></tr><tr><td><a href="../meanings/94.html">94</a> / <a href="../meanings/9494.html">9494</a></td><td>就是</td><td>Exactly</td></tr><tr><td><a href="../meanings/484.html">484</a></td><td>是不是</td><td>Right?</td></tr><tr><td><a href="../meanings/584.html">584</a></td><td>我发誓</td><td>I swear</td></tr></tbody></table></div>
<h2 id="rude">Rude ones to recognise</h2><p><a href="../meanings/748.html">748</a> (去死吧, get lost), <a href="../meanings/250.html">250</a> (二百五, idiot) and <a href="../meanings/0437.html">0437</a> (你是神经, you’re crazy). Recognise them — don’t put them in a gift.</p>
<h2 id="555185">And 555185?</h2><p>Read it in two halves: <b>555</b> (呜呜呜, crying) + <b>185</b> (yāo-bā-wǔ ≈ 要发我, “prosperity — to me!”). It’s a playful constructed reading rather than established slang: <i>stop crying, the red packet is coming</i>. <a href="../the-555185-story.html">Read the story</a>.</p>''',
 [("What does 555 mean in Chinese texting?", "Crying — 555 (wǔ wǔ wǔ) imitates 呜呜呜. Add more fives for more drama."),
  ("What does 886 mean?", "Bye-bye (拜拜了) — a casual sign-off."),
  ("Why does 233 mean LOL?", "It comes from emoticon #233 on the Mop (猫扑) forum, which showed a face pounding the floor laughing."),
  ("Is 666 unlucky in China?", "No — it’s positive. 666 (溜溜溜) means ‘awesome / smooth’, and 六六大顺 is a classic blessing.")],
 toc=[("how", "Why numbers become words"), ("emotion", "Emotions"), ("love", "Love"), ("everyday", "Everyday chat"), ("rude", "Rude codes"), ("555185", "555185"), ("faq", "FAQ")])

add("lucky-and-unlucky-numbers", "🍀", "Lucky & unlucky numbers", "8, 6, 9 vs 4, 250, 14 — and how money follows them.",
 "Chinese Lucky and Unlucky Numbers: 8, 6, 9 vs 4 — Meanings & Money | 555185",
 "Chinese lucky and unlucky numbers",
 "Why 8 is lucky and 4 is unlucky in Chinese culture, plus 6, 9, 2, 3, 7, 250 and 14 — and how number beliefs shape prices, phone numbers, plates and red envelope amounts.",
 "Number beliefs aren’t trivia in Chinese-speaking markets — they shape prices, floor plans, phone numbers, launch dates and every red envelope.",
 '''<h2 id="lucky">The lucky numbers</h2><ul><li><b><a href="../meanings/8.html">8</a> 八 bā</b> ≈ 发 fā (prosper). The king of numbers — Beijing opened the 2008 Olympics on 8 August 2008 at 8:08 pm.</li><li><b><a href="../meanings/6.html">6</a> 六 liù</b> ≈ 溜/顺 (smooth). 六六大顺 = everything goes smoothly.</li><li><b><a href="../meanings/9.html">9</a> 九 jiǔ</b> ≈ 久 (long-lasting). Ideal for love and longevity.</li><li><b><a href="../meanings/2.html">2</a> 二 èr</b> — good things come in pairs (好事成双).</li></ul>
<h2 id="unlucky">The unlucky numbers</h2><ul><li><b><a href="../meanings/4.html">4</a> 四 sì</b> ≈ 死 sǐ (death). Buildings skip 4th, 14th and 24th floors; hospitals avoid room 4.</li><li><b><a href="../meanings/14.html">14</a></b> ≈ 要死 (going to die) in phone-style reading; <b>74</b> ≈ 气死 (infuriating).</li><li><b><a href="../meanings/250.html">250</a></b> 二百五 = idiot.</li><li><b>7</b> is mixed — the 7th lunar month is Ghost Month.</li></ul>
<h2 id="money">How numbers move money</h2><p>Premium phone numbers and licence plates packed with 8s sell at auction for large sums in Hong Kong and mainland China; property developers rename floors; retailers price at 168, 188 or 888; companies pick launch dates like 8 August or 18 May (518 = 我要发). For any business selling to Chinese-speaking customers, removing 4s from prices, SKUs and phone lines is the cheapest conversion fix there is.</p>
<h2 id="combo">Powerful combinations</h2><div class="tbl"><table><thead><tr><th>Number</th><th>Reading</th><th>Used for</th></tr></thead><tbody>
<tr><td><a href="../meanings/168.html">168</a></td><td>一路发 — prosper all the way</td><td>Prices, phone numbers, gifts</td></tr><tr><td><a href="../meanings/518.html">518</a></td><td>我要发 — I will prosper</td><td>Business openings</td></tr><tr><td><a href="../meanings/888.html">888</a></td><td>发发发</td><td>Gifts, premium prices</td></tr><tr><td><a href="../meanings/1314.html">1314</a></td><td>一生一世 — forever</td><td>Weddings, anniversaries</td></tr><tr><td><a href="../meanings/99.html">99</a></td><td>久久 — everlasting</td><td>Love, elders’ birthdays</td></tr></tbody></table></div>
<p>Test any number in the <a href="../tools/number-code-decoder.html">decoder</a>, or snap a budget with the <a href="../tools/lucky-amount-finder.html">lucky amount finder</a>.</p>''',
 [("Why is 8 lucky in Chinese culture?", "八 (bā) sounds like 发 (fā), meaning to prosper or get rich — especially close in Cantonese (baat / faat)."),
  ("Why is 4 unlucky?", "四 (sì) sounds almost identical to 死 (sǐ), death. It’s avoided in floors, phone numbers, plates, prices and gifts."),
  ("Is 7 lucky or unlucky?", "Mixed. It can mean ‘rise’ (起) and features in 七夕 (Chinese Valentine’s), but also 气 (anger), and the 7th lunar month is Ghost Month.")],
 toc=[("lucky", "Lucky numbers"), ("unlucky", "Unlucky numbers"), ("money", "How numbers move money"), ("combo", "Power combinations"), ("faq", "FAQ")])

add("corporate-cny-gifting-guide", "🏢", "Corporate CNY gifting", "Staff lai see, client gifts, custom envelopes and timelines.",
 "Corporate Lunar New Year Gifting Guide 2027: Staff Red Envelopes, Client Gifts & Custom Hongbao | 555185",
 "Corporate Lunar New Year gifting guide (2027)",
 "How businesses handle Lunar New Year 2027: staff red envelopes (开工利是), client gifts, custom-branded red envelopes, ordering timelines, minimums and budget planning.",
 "For companies with Chinese-speaking staff, clients or customers, Lunar New Year is the biggest relationship moment of the year. Here’s how to do it right — and on time.",
 '''<h2 id="staff">Staff red envelopes</h2><p>Common practice across Hong Kong, mainland China, Singapore and Malaysia: managers give staff red envelopes on the <b>first working day after the holiday</b> (开工利是 / 开工红包). Amounts are modest and equal within a team tier; senior managers give to everyone below them. Married managers are expected to give; in Hong Kong it is common for all managers to give.</p>
<h2 id="clients">Client and partner gifts</h2><ul><li><b>Gift hampers</b> with mandarins (吉 = luck), nian gao (年糕, “higher every year”), tea and premium snacks.</li><li><b>Branded red envelopes</b> — clients keep and reuse good ones, so your logo travels all season.</li><li><b>Avoid</b> clocks (送钟 sounds like attending a funeral), sharp objects (cutting ties), anything in sets of four, and white or black wrapping.</li></ul>
<h2 id="custom">Custom red envelopes: what to know</h2><div class="tbl"><table><thead><tr><th>Decision</th><th>Typical options</th></tr></thead><tbody><tr><td>Minimum order</td><td>Often from 100 units; unit price drops with volume</td></tr><tr><td>Finish</td><td>Gold or red foil stamping, embossing, spot UV, metallic paper</td></tr><tr><td>Size</td><td>Standard 9×17 cm, square, or fit-a-banknote sizes per currency</td></tr><tr><td>Artwork</td><td>Logo + zodiac motif (Goat for 2027) + blessing (e.g. 恭喜发财)</td></tr><tr><td>Lead time</td><td>Plan 4–8 weeks including proofs and shipping</td></tr></tbody></table></div>
<h2 id="timeline">2027 timeline (New Year: 6 Feb)</h2><ol><li><b>October–November 2026:</b> set budget, brief designs, request quotes.</li><li><b>By early December:</b> approve proofs and place orders.</li><li><b>Early–mid January 2027:</b> delivery; withdraw new notes; prepare staff lists.</li><li><b>Late January:</b> send client gifts before the holiday rush.</li><li><b>First working day after the holiday:</b> staff 开工 envelopes.</li></ol>
<div class="band"><div><h2>Get 3 free quotes in one go</h2><p>Custom envelopes, gift boxes and hampers — from 100 units. Tell us quantity, deadline and budget.</p></div><div><a class="btn gold" href="../quote.html#corporate">Request quotes</a></div></div>''',
 [("When do companies give red envelopes?", "Usually on the first working day after the Lunar New Year holiday (开工利是), and sometimes as part of year-end bonuses before the holiday."),
  ("How early should I order custom red envelopes?", "Plan 4–8 weeks before you need them. For Lunar New Year 2027 (6 February), approve designs by early December 2026."),
  ("What gifts should I avoid for Chinese clients?", "Clocks, sharp objects, items in fours, green hats and white/black wrapping. Pears are sometimes avoided because 梨 sounds like ‘separation’.")],
 toc=[("staff", "Staff red envelopes"), ("clients", "Client gifts"), ("custom", "Custom envelopes"), ("timeline", "2027 timeline"), ("faq", "FAQ")])

add("red-envelope-mistakes", "⚠️", "12 red envelope mistakes", "The quiet faux pas that offend — and how to avoid them.",
 "12 Red Envelope Mistakes to Avoid (Lunar New Year & Weddings) | 555185",
 "12 red envelope mistakes to avoid",
 "Avoid these red envelope mistakes: amounts with 4, 250, old notes, white envelopes, odd amounts, opening in front of the giver, skipping people and more.",
 "Most red-envelope faux pas are invisible to the giver and obvious to everyone else. Here are the twelve to avoid.",
 '''<ol>
<li><b>An amount with a 4 in it.</b> ¥40, ¥400, $140 — all read as death. <a href="../tools/lucky-amount-finder.html">Snap it</a> to 38, 388 or 168.</li>
<li><b>Giving 250.</b> 二百五 means “idiot”.</li>
<li><b>Odd amounts at happy events.</b> Odd sums are for funerals.</li>
<li><b>Old, creased notes.</b> New notes signal a fresh start.</li>
<li><b>A white envelope.</b> White is for mourning. Use red (gold printing is perfect).</li>
<li><b>Coins in the envelope.</b> Notes only.</li>
<li><b>Opening it in front of the giver.</b> Thank them and open later.</li>
<li><b>One hand.</b> Give and receive with both hands.</li>
<li><b>Skipping someone in a group.</b> If you give to one child in a family, give to all siblings equally.</li>
<li><b>Writing in red ink.</b> Names in red ink are associated with the dead — use black or gold.</li>
<li><b>Giving during mourning.</b> Families in their first year of mourning often don’t give or receive New Year envelopes.</li>
<li><b>Forgetting staff.</b> Doormen, cleaners and helpers notice — small envelopes go a long way.</li></ol>
<p>Prep your list in the <a href="../tools/hongbao-calculator.html">planner</a> and read the <a href="red-envelope-etiquette.html">full etiquette guide</a>.</p>''',
 [("Is it bad luck to give money in a white envelope?", "Yes — white envelopes are for condolence money at funerals."),
  ("Can I write a name in red ink?", "Avoid it; names written in red are traditionally associated with the deceased. Use black, gold or blue."),
  ("What if I accidentally gave an amount with 4?", "Don’t panic — most people will be gracious. Next time, round to the nearest lucky amount.")])

add("lunar-new-year-2027-planner", "🐐", "Lunar New Year 2027 planner", "Year of the Goat dates, traditions and a countdown checklist.",
 "Lunar New Year 2027 Planner: Year of the Goat Dates, Traditions & Checklist | 555185",
 "Lunar New Year 2027: the Year of the Goat planner",
 "Lunar New Year 2027 is on 6 February — the Year of the Fire Goat. Key dates from Little New Year to Lantern Festival, traditions, foods, taboos and a red-envelope checklist.",
 "Saturday, 6 February 2027 opens the Year of the Fire Goat (丁未). Here are the key dates, traditions and a countdown checklist.",
 '''<div class="tool"><h3 class="mt0">Countdown to 6 February 2027</h3><div class="cd" data-countdown="2027-02-06"></div></div>
<h2 id="dates">Key dates</h2><div class="tbl"><table><thead><tr><th>Date</th><th>Occasion</th><th>What happens</th></tr></thead><tbody>
<tr><td>Late January</td><td>Little New Year (小年)</td><td>Kitchen God send-off, start of spring cleaning</td></tr>
<tr><td>Fri 5 Feb 2027</td><td>New Year’s Eve (除夕)</td><td>Reunion dinner, red envelopes for children, staying up late</td></tr>
<tr><td>Sat 6 Feb 2027</td><td>New Year’s Day (春节)</td><td>Visiting elders, greetings, no sweeping (don’t sweep luck away)</td></tr>
<tr><td>Days 2–7</td><td>Visiting season</td><td>Day 2: married daughters visit parents; Day 5: welcoming the God of Wealth</td></tr>
<tr><td>Sat 20 Feb 2027</td><td>Lantern Festival (元宵节)</td><td>Lanterns, tangyuan, end of the season</td></tr></tbody></table></div>
<h2 id="goat">The Year of the Goat</h2><p>The Goat (羊) is associated with gentleness, creativity and peace. 2027 is a <b>Fire Goat</b> year. Greetings: 羊年大吉 (great luck in the Goat year), 三羊开泰 (three goats bring prosperity) and 喜气洋洋 (brimming with joy — 洋 puns on 羊). Find your sign in the <a href="../tools/zodiac-cny-countdown.html">zodiac finder</a>.</p>
<h2 id="checklist">Red envelope checklist</h2><ul class="check-list"><li>List everyone you’ll give to — <a href="../tools/hongbao-calculator.html">use the planner</a></li><li>Order envelopes (custom/branded if for business)</li><li>Withdraw new notes 2–3 weeks early</li><li>Pre-fill envelopes by recipient and label the backs lightly in pencil</li><li>Prepare small envelopes for staff and door games</li><li>Learn two greetings — <a href="../tools/greetings-generator.html">get them here</a></li></ul>
<h2 id="taboos">Classic taboos</h2><ul><li>No sweeping or taking out rubbish on New Year’s Day.</li><li>No haircuts during the first days (头发 hair ≈ 发 prosper — don’t cut it).</li><li>Avoid breaking things and saying unlucky words (death, sickness).</li><li>Don’t lend or borrow money on New Year’s Day.</li></ul>''',
 [("When is Chinese New Year 2027?", "Saturday, 6 February 2027. New Year’s Eve is Friday 5 February, and the Lantern Festival falls on 20 February."),
  ("What animal is 2027?", "The Goat (羊) — specifically the Fire Goat, 丁未."),
  ("Why no haircuts at New Year?", "The 发 in 头发 (hair) is the same character as 发 (prosper), so cutting hair early in the year is said to cut away good fortune.")],
 toc=[("dates", "Key dates"), ("goat", "Year of the Goat"), ("checklist", "Checklist"), ("taboos", "Taboos"), ("faq", "FAQ")])


def build():
    out = []
    for slug, icon, card, short, title, h1, desc, intro, content, faqs, toc in G:
        path = f"guides/{slug}.html"
        out.append((path, article(path, title, h1, desc, [("guides/", "Guides"), ("", card)], intro, content, faqs=faqs, toc=toc)))
    cards = "".join(f'<a class="card" href="{s}.html"><div class="ico">{i}</div><h3>{c}</h3><p>{sh}</p></a>' for s, i, c, sh, *_ in G)
    body = f'''<div class="wrap page-hero">{{{{CRUMBS}}}}<span class="eyebrow">Guides</span><h1>Red envelope &amp; number guides</h1><p class="lead">Clear, practical guides to hongbao etiquette, Chinese weddings, number slang, lucky numbers, corporate gifting and Lunar New Year 2027.</p></div>
<div class="wrap"><div class="grid g3">{cards}<a class="card" href="../the-555185-story.html"><div class="ico">5</div><h3>The 555185 story</h3><p>From tears (555) to fortune (185).</p></a></div>{ad("footer")}</div>'''
    out.append(("guides/index.html", page("guides/index.html", "Red Envelope, Chinese Wedding & Lucky Number Guides | 555185",
        "Practical guides: red envelope etiquette, Chinese wedding red envelopes, amounts by country, digital red packets, number slang, lucky numbers, corporate CNY gifting and the 2027 planner.", body, crumbs=[("", "Guides")])))
    return out
