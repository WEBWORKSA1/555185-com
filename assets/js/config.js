/* =====================================================================
   555185.com — SITE CONFIG  (the only file you need to edit to go live)
   ===================================================================== */
window.SITE = {
  name: "555185",
  domain: "555185.com",

  /* Google AdSense — paste your publisher id after approval, e.g. "ca-pub-1234567890123456".
     Leave "" to show house ads instead. Optional per-placement slot ids. */
  ADSENSE_CLIENT: "",
  ADSENSE_SLOTS: { top: "", inarticle: "", sidebar: "", footer: "" },

  /* Google Analytics 4 measurement id, e.g. "G-XXXXXXX" (optional) */
  GA4_ID: "",

  /* YouTube channel URL for the "Subscribe" buttons (optional) */
  YOUTUBE_CHANNEL: "",

  /* Donation links — any left "" are hidden; the pledge form always works. */
  DONATE: {
    paypal: "",        // e.g. "https://paypal.me/yourname"
    kofi: "",          // e.g. "https://ko-fi.com/yourname"
    buymeacoffee: "",  // e.g. "https://buymeacoffee.com/yourname"
    stripe: "",        // a Stripe Payment Link
    github: ""         // GitHub Sponsors URL
  },

  /* External contact page for domain / sponsorship / advertising / partnership */
  PARTNER_URL: "https://web.works/contact",

  /* Inbox routing: obfuscated, assembled only at runtime, never printed on the page. */
  _k: [120,122,110,57,119,116,108,120,114,75,60,108,126,118,125,122,130,109,112,130],
  _o: 11
};
