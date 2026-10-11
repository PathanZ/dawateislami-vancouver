"""Assemble the site pages from shared pieces. Run: python3 build.py

Pages
  index.html          Dawat-e-Islami Canada home (national)
  centres.html        All Faizan e Madina centres in Canada
  vancouver.html      Faizan e Madina Vancouver (Surrey): prayers, Ijtima, services, map
  prayer-times.html   Monthly timetable for the Vancouver centre

To add a city, add an entry to CENTRES below and rebuild.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).parent
BN = "81933 5662 RR0001"
# Cache-busting: browsers re-download CSS/JS whenever their contents change
V = hashlib.md5(b"".join((ROOT / f).read_bytes() for f in ["assets/style.css", "assets/main.js", "assets/prayer-data.js"])).hexdigest()[:8]


def tbc(label="TBC"):
    return f'<span class="draft">{label}</span>'


# ---- Centres in Canada -------------------------------------------------------
# page: the centre's own page, or None while it has no page yet
CENTRES = [
    # British Columbia
    {"province": "British Columbia", "city": "Vancouver", "name": "Faizan-e-Madina Masjid",
     "address": "7062 134 St, Surrey, BC V3W 4T2", "phone": "+1 (778) 895-0886", "page": "vancouver.html",
     "note": "Daily prayers · Weekly Ijtima · Weekend Islamic School"},
    # Alberta
    {"province": "Alberta", "city": "Calgary", "name": "Faizan-e-Madina",
     "address": "32 Westwinds Crescent NE, Calgary, AB T3J 5H2", "phone": "+1 (403) 618-5408", "page": None, "note": ""},
    {"province": "Alberta", "city": "Calgary", "name": "Faizan-e-Makkah",
     "address": "4250 109 Ave NE, Calgary, AB T3N 1Z3", "phone": "+1 (403) 618-5408", "page": None, "note": ""},
    {"province": "Alberta", "city": "Edmonton", "name": "Faizan-e-Madina Edmonton",
     "address": "11809 96 St, Edmonton, AB T5G 1V4", "phone": "+1 (780) 729-6492", "page": None, "note": ""},
    # Saskatchewan
    {"province": "Saskatchewan", "city": "Regina", "name": "Faizan-e-Madina Islamic Center",
     "address": "1169 Athol St, Regina, SK S4T 3C3", "phone": "+1 (438) 401-0782", "page": None, "note": ""},
    # Manitoba
    {"province": "Manitoba", "city": "Winnipeg", "name": "Faizan-e-Madina Islamic Centre",
     "address": "585 St Anne's Rd, Winnipeg, MB R2M 5R5", "phone": "+1 (204) 998-1979", "page": None, "note": ""},
    {"province": "Manitoba", "city": "Winnipeg", "name": "Faizan-e-Makkah",
     "address": "509 Trans-Canada Hwy, Winnipeg, MB R2M 3L2", "phone": "+1 (204) 998-1979", "page": None,
     "note": "Under construction"},
    # Ontario
    {"province": "Ontario", "city": "East York (Thorncliffe)", "name": "Faizan-e-Attar",
     "address": "49 Thorncliffe Park Dr, Unit 120, East York, ON M4H 1J6", "phone": "+1 (647) 366-3786", "page": None, "note": ""},
    {"province": "Ontario", "city": "Etobicoke", "name": "Faizan-e-Madina Etobicoke",
     "address": "595 Albion Rd, Etobicoke, ON M9V 1A1", "phone": "+1 (647) 366-3786", "page": None, "note": ""},
    {"province": "Ontario", "city": "Hamilton", "name": "Faizan-e-Madina Hamilton",
     "address": "1202 Dunsmure Rd, Hamilton, ON L8H 1L4", "phone": "+1 (647) 366-3786", "page": None, "note": ""},
    {"province": "Ontario", "city": "Ottawa", "name": "Faizan-e-Madina Islamic Center",
     "address": "415 McArthur Ave, Ottawa, ON K1K 1G5", "phone": "+1 (514) 983-7861", "page": None, "note": ""},
    # Quebec
    {"province": "Quebec", "city": "Montreal", "name": "Faizan-e-Madina Montreal",
     "address": "810 Rue Saint-Roch, Montréal, QC H3N 1L4", "phone": "+1 (514) 983-7861", "page": None, "note": ""},
    {"province": "Quebec", "city": "Montreal", "name": "Faizan-e-Hub-e-Rasool",
     "address": "1008 Rue Jean-Talon O, Montréal, QC H3N 1T1", "phone": "+1 (514) 983-7861", "page": None, "note": ""},
]

V_ADDRESS = CENTRES[0]["address"]
V_PHONE = CENTRES[0]["phone"]
V_MAP_Q = "Faizan+e+Madina,+7062+134+Street,+Surrey,+BC"


def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#075b48">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%95%8C%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Marcellus&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v={V}">
</head>
<body>
'''


def header(current, local_prayer=False):
    def link(href, text, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}>{text}</a>'
    nxt = ('<a class="next" id="nextPrayer" href="vancouver.html" aria-live="polite"></a>'
           if local_prayer else "")
    return f'''<div class="topbar">
  <div class="wrap">
    <span class="arabic bismillah" lang="ar">بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ</span>
    {nxt}
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html"><img src="assets/img/logo.png" width="900" height="242" alt="Dawat-e-Islami Canada"></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      {link("index.html#about", "About Us", "about")}
      {link("index.html#services", "Services", "services")}
      {link("centres.html", "Centres", "centres")}
      {link("index.html#contact", "Contact", "contact")}
      <a class="btn btn-gold" href="index.html#donate">Donate now</a>
    </nav>
  </div>
</header>
'''


FOOTER = f'''<footer class="site-footer" id="contact">
  <div class="wrap">
    <div class="cols">
      <div>
        <img class="footer-logo" src="assets/img/logo-white.png" width="900" height="242" alt="Dawat-e-Islami Canada">
        <p>A global, non-political movement spreading the teachings of the Qur'an and Sunnah.</p>
        <p class="bn">Registered Canadian charity · BN {BN}</p>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>Address: {tbc()}</li>
          <li>Phone: {tbc()}</li>
          <li>Email: {tbc()}</li>
          <li>WhatsApp: {tbc()}</li>
        </ul>
      </div>
      <div>
        <h4>Quick links</h4>
        <ul>
          <li><a href="index.html#about">About us</a></li>
          <li><a href="index.html#services">Services</a></li>
          <li><a href="centres.html">Centres</a></li>
          <li><a href="index.html#donate">Donate</a></li>
        </ul>
      </div>
      <div>
        <h4>Dawat-e-Islami worldwide</h4>
        <ul>
          <li><a href="https://www.dawateislami.net/" target="_blank" rel="noopener">Global website</a></li>
          <li><a href="https://www.dawateislamiusa.org/" target="_blank" rel="noopener">Dawat-e-Islami USA</a></li>
          <li><a href="https://dawateislami.co.uk/" target="_blank" rel="noopener">Dawat-e-Islami UK</a></li>
          <li><a href="https://www.fatwaqa.com/en" target="_blank" rel="noopener">Ask a question (Darul Ifta)</a></li>
        </ul>
        <p class="social">Social media: {tbc("Links TBC")}</p>
      </div>
    </div>
    <div class="legal">
      <span>© <span id="year">2026</span> Dawat-e-Islami Canada</span>
      <span>Draft preview for management review</span>
    </div>
  </div>
</footer>
<script src="assets/prayer-data.js?v={V}"></script>
<script src="assets/main.js?v={V}"></script>
</body>
</html>
'''

ICON = {
    "salah": '<path d="M3 20h18M5 20V11l7-6 7 6v9M10 20v-5h4v5"/>',
    "jummah": '<circle cx="8" cy="9" r="3"/><circle cx="16" cy="9" r="3"/><path d="M2 20c.8-3 3-5 6-5s5.2 2 6 5M14 15.2c.6-.1 1.3-.2 2-.2 3 0 5.2 2 6 5"/>',
    "ijtima": '<path d="M12 3v3M5 21v-6a7 7 0 0114 0v6M3 21h18M9 21v-3h6v3"/>',
    "school": '<rect x="3" y="5" width="18" height="15" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "courses": '<path d="M4 4h12l4 4v12H4zM8 12h8M8 16h5"/>',
    "quran": '<path d="M4 5h7a2 2 0 012 2v12a2 2 0 00-2-2H4zM20 5h-7a2 2 0 00-2 2v12a2 2 0 012-2h7z"/>',
    "sisters": '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1-4 4-6 7-6s6 2 7 6"/>',
    "online": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4M10 9l5 2-5 2z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
}


def svg(name):
    return f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>'


def card(icon, title, text):
    return f'''        <article class="program">
          <div class="ic" aria-hidden="true">{svg(icon)}</div>
          <h3>{title}</h3>
          <p>{text}</p>
        </article>'''


def centre_card(c):
    q = c["address"].replace(" ", "+")
    note = f'<p class="note">{c["note"]}</p>' if c["note"] else ""
    tel = "".join(ch for ch in c["phone"] if ch.isdigit() or ch == "+")
    inner = f'''<div class="ic" aria-hidden="true">{svg("pin")}</div>
          <p class="city-prov">{c["city"]}</p>
          <h3>{c["name"]}</h3>
          <p>{c["address"]}</p>
          {note}'''
    if c["page"]:
        return f'''        <a class="program centre" href="{c["page"]}">
          {inner}
          <p class="phone">{c["phone"]}</p>
          <span class="when">View centre →</span>
        </a>'''
    return f'''        <article class="program centre">
          {inner}
          <p class="phone"><a href="tel:{tel}">{c["phone"]}</a></p>
          <a class="when" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener">Directions →</a>
        </article>'''


def placeholder_card():
    return f'''        <article class="program centre empty">
          <div class="ic" aria-hidden="true">{svg("pin")}</div>
          <h3>More cities</h3>
          <p>Other Faizan e Madina centres across Canada will be listed here. {tbc("Send list of cities")}</p>
        </article>'''


GLOBAL_SERVICES = "\n".join([
    card("salah", "Masajid", "Faizan e Madina centres for the five daily prayers and Jummah."),
    card("ijtima", "Weekly Ijtima", "Weekly spiritual gatherings with tilawat, naat, bayan, zikr and dua."),
    card("school", "Faizan Weekend Islamic School", "Faith, character and Qur'an for children who attend school during the week."),
    card("quran", "Qur'an classes & Hifz", "Learn to read the Qur'an with tajweed, and memorise it in the Hifz program."),
    card("courses", "Free short courses", "Monthly courses on everyday Islamic knowledge, open to everyone."),
    card("sisters", "Programs for sisters", "Halaqahs, classes and gatherings run by and for Islamic sisters."),
    card("online", "Faizan Online Academy", "Live online Qur'an and Islamic studies classes you can join from home."),
    card("jummah", "Community support", "Guidance, spiritual cure and help for families in our community."),
])

PILLARS = "\n".join(
    f'<div class="pillar"><span class="arabic" lang="ar">{ar}</span><h3>{en}</h3><p>{txt}</p></div>'
    for ar, en, txt in [
        ("شَهَادَة", "Shahadah", "Belief in the oneness of Allah and that Muhammad ﷺ is His final messenger."),
        ("صَلَاة", "Salah", "Worshipping Allah through the five daily prayers."),
        ("زَكَاة", "Zakat", "Giving 2.5% of eligible wealth each year to those in need."),
        ("صَوْم", "Sawm", "Fasting from dawn to sunset through the month of Ramadan."),
        ("حَجّ", "Hajj", "Pilgrimage to Makkah once in a lifetime, for those who are able."),
    ])

DONATE = f'''  <section class="block alt" id="donate">
    <div class="wrap donate">
      <div>
        <div class="head left">
          <p class="kicker">Support us</p>
          <h2>Your donation keeps our work going</h2>
          <div class="ornament" aria-hidden="true">✦</div>
        </div>
        <p>Donations support our masajid, Qur'an classes and community programs across Canada. Sadaqah, Zakat and Fitrana are all accepted.</p>
        <p class="hadith">"Charity does not decrease wealth." <span>Sahih Muslim, 2588</span></p>
        <p class="muted">Dawat-e-Islami Canada is a registered Canadian charity (BN {BN}). Official tax receipts are issued for eligible donations.</p>
      </div>
      <div class="give">
        <h3>Ways to give</h3>
        <a class="btn btn-green wide" href="#donate" aria-disabled="true">Donate online {tbc("link TBC")}</a>
        <div class="etransfer">
          <b>Interac e-Transfer</b>
          <span>{tbc("Email TBC")}</span>
          <small>For a tax receipt, include your full name and mailing address in the message.</small>
        </div>
        <div class="etransfer">
          <b>In person</b>
          <span>At any of our centres after prayers</span>
        </div>
      </div>
    </div>
  </section>
'''

CITY_CHIPS = "\n".join(
    f'        <li><a href="{c["page"] or "centres.html"}">{c["city"]}</a></li>'
    for c in {c["city"]: c for c in reversed(CENTRES)}.values().__reversed__())

HOME = f'''<main id="top">
  <section class="hero hero-global">
    <!-- Hero video goes here later: <video class="hero-video" autoplay muted loop playsinline poster="assets/img/hero.jpg"><source src="assets/video/hero.mp4" type="video/mp4"></video> -->
    <div class="wrap">
      <p class="arabic" lang="ar">اَلسَّلَامُ عَلَيْكُمْ</p>
      <h1>Welcome to Dawat-e-Islami Canada</h1>
      <p class="tagline">Connect · Learn · Grow · Together</p>
      <p class="lead">Spreading the teachings of the Qur'an and Sunnah through our masajid, Qur'an classes and community programs across Canada.</p>
      <div class="actions">
        <a class="btn btn-gold" href="#donate">Donate now</a>
        <a class="btn btn-line" href="centres.html">Find a centre</a>
      </div>
    </div>
  </section>

  <section class="slogan" aria-label="Madani Maqsad">
    <div class="wrap">
      <p class="kicker">Our Madani Maqsad</p>
      <p class="en">"I must strive to reform myself and the people of the entire world, In sha Allah."</p>
    </div>
  </section>

  <section class="block alt" id="about">
    <div class="wrap about">
      <div>
        <div class="head left">
          <p class="kicker">About us</p>
          <h2>Part of the global family of Dawat-e-Islami</h2>
          <div class="ornament" aria-hidden="true">✦</div>
        </div>
        <p>Dawat-e-Islami was founded in 1981 in Karachi by Ameer-e-Ahl-e-Sunnat, Maulana Muhammad Ilyas Attar Qadri. Today it serves communities around the world through Qur'an education, Islamic scholarship and welfare work.</p>
        <p>Dawat-e-Islami Canada brings that work to communities across the country through its Faizan e Madina centres, classes and weekly gatherings.</p>
        <p>{tbc("Add: a few lines about Dawat-e-Islami Canada's history")}</p>
      </div>
      <div class="photo-slot">
        <div><strong>Photo</strong><span>Masjid or Ameer-e-Ahl-e-Sunnat, to be added</span></div>
      </div>
    </div>
  </section>

{DONATE}
  <section class="block" id="services">
    <div class="wrap">
      <div class="head">
        <p class="kicker">What we offer</p>
        <h2>Our services</h2>
        <div class="ornament" aria-hidden="true">✦</div>
        <p>Available at our centres across Canada. See each centre's page for its own programs and timings.</p>
      </div>
      <div class="programs four">
{GLOBAL_SERVICES}
      </div>
    </div>
  </section>

  <section class="block hadees" aria-labelledby="hadeesTitle">
    <div class="wrap">
      <p class="kicker" id="hadeesTitle">Hadees of the week</p>
      <p class="arabic" lang="ar">خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ</p>
      <blockquote>The best among you is the one who learns the Qur'an and teaches it.</blockquote>
      <cite>Sahih al-Bukhari, Hadith 5027</cite>
    </div>
  </section>

  <section class="block tint" id="pillars">
    <div class="wrap">
      <div class="head">
        <p class="kicker">Discover Islam</p>
        <h2>The five pillars of Islam</h2>
        <div class="ornament" aria-hidden="true">✦</div>
      </div>
      <div class="pillars">
{PILLARS}
      </div>
    </div>
  </section>

  <section class="block" id="centres">
    <div class="wrap">
      <div class="head">
        <p class="kicker">Our centres</p>
        <h2>Find a Faizan e Madina near you</h2>
        <div class="ornament" aria-hidden="true">✦</div>
        <p>{len(CENTRES)} centres in {len(set(c["province"] for c in CENTRES))} provinces, for daily prayers, weekly gatherings and classes.</p>
      </div>
      <ul class="city-chips">
{CITY_CHIPS}
      </ul>
      <p class="center-cta"><a class="btn btn-green" href="centres.html">View all centres</a></p>
    </div>
  </section>
</main>
'''


def page_head(title, sub, crumbs):
    trail = " <span>›</span> ".join(
        f'<a href="{h}">{t}</a>' if h else f"<span aria-current=\"page\">{t}</span>" for t, h in crumbs)
    return f'''  <section class="page-head">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">{trail}</nav>
      <h1>{title}</h1>
      <p>{sub}</p>
    </div>
  </section>
'''


provinces = []
for prov in dict.fromkeys(c["province"] for c in CENTRES):
    cards = "\n".join(centre_card(c) for c in CENTRES if c["province"] == prov)
    provinces.append(f'''    <h2 class="prov">{prov}</h2>
    <div class="programs centres-grid">
{cards}
    </div>''')

CENTRES_PAGE = f'''<main>
{page_head("Our centres in Canada", "Faizan e Madina centres of Dawat-e-Islami across Canada", [("Home", "index.html"), ("Centres", None)])}
  <div class="wrap pt-main">
{chr(10).join(provinces)}
    <p class="muted centres-note">Centre list from Dawat-e-Islami Canada. Is a centre missing or out of date? Please let us know.</p>
  </div>
</main>
'''

V_SERVICES = "\n".join([
    card("salah", "5 daily prayers", "Jama'at for all five daily prayers."),
    card("jummah", "Two Jummah prayers", "Two Friday congregations, at 1:30 PM and 3:30 PM."),
    card("ijtima", "Weekly Ijtima", "Every Thursday at 7:00 PM."),
    card("school", "Weekend Islamic School", "Faith, character and Qur'an for children on weekends."),
    card("courses", "Free monthly courses", "Short courses on everyday Islamic knowledge."),
    card("quran", "Qur'an classes & Hifz", "Qur'an reading with tajweed and the Hifz program."),
    card("sisters", "Sisters-only Halaqah", "Classes and gatherings for Islamic sisters."),
    card("online", "Faizan Online Academy", "Live online classes you can join from home."),
])

IJTIMA_PARTS = "".join(f"<li>{p}</li>" for p in ["Tilawat", "Naat", "Bayan", "Zikr", "Dua", "Salam"])

VANCOUVER = f'''<main>
{page_head("Faizan e Madina Vancouver", V_ADDRESS, [("Home", "index.html"), ("Centres", "centres.html"), ("Vancouver", None)])}
  <section class="block">
    <div class="wrap centre-top">
      <aside class="today" aria-labelledby="todayTitle">
        <div class="today-head">
          <h2 id="todayTitle">Today's prayers</h2>
          <span class="today-date" id="todayDate"></span>
        </div>
        <div class="today-cols"><span>Prayer</span><span>Begins</span><span>Jama'at</span></div>
        <ul class="today-list" id="todayList"></ul>
        <div class="today-foot">
          <span>Jummah: 1:30 PM &amp; 3:30 PM</span>
          <a href="prayer-times.html">Full timetable</a>
        </div>
      </aside>
      <div id="ijtima">
        <div class="head left">
          <p class="kicker">Every Thursday</p>
          <h2>Weekly Ijtima, open to everyone</h2>
          <div class="ornament" aria-hidden="true">✦</div>
        </div>
        <p>A weekly spiritual gathering with recitation, a bayan on the topic of the week, remembrance of Allah and a heartfelt dua.</p>
        <ul class="parts">{IJTIMA_PARTS}</ul>
        <ul class="facts">
          <li><b>When</b><span>Thursdays at 7:00 PM</span></li>
          <li><b>Where</b><span>{V_ADDRESS}</span></li>
          <li><b>Also</b><span>Dinner served · separate arrangement for sisters</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="block alt">
    <div class="wrap">
      <div class="head">
        <p class="kicker">At this centre</p>
        <h2>Our services to the community</h2>
        <div class="ornament" aria-hidden="true">✦</div>
      </div>
      <div class="programs four">
{V_SERVICES}
      </div>
    </div>
  </section>

  <section class="block">
    <div class="wrap visit">
      <div>
        <div class="head left">
          <p class="kicker">Visit us</p>
          <h2>Find Faizan e Madina Vancouver</h2>
          <div class="ornament" aria-hidden="true">✦</div>
        </div>
        <ul>
          <li><b>Address</b><span>{V_ADDRESS}</span></li>
          <li><b>Open</b><span>Daily for all five prayers</span></li>
          <li><b>Phone</b><span><a href="tel:+17788950886">{V_PHONE}</a></span></li>
          <li><b>Parking</b><span>{tbc()}</span></li>
        </ul>
        <a class="btn btn-green" href="https://www.google.com/maps/search/?api=1&amp;query={V_MAP_Q}" target="_blank" rel="noopener">Get directions</a>
      </div>
      <div class="map-slot">
        <iframe title="Map of Faizan e Madina Vancouver" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={V_MAP_Q}&amp;output=embed"></iframe>
      </div>
    </div>
  </section>
</main>
'''

PT_MAIN = (ROOT / "partials/prayer-main.html").read_text()

pages = {
    "index.html": (head("Dawat-e-Islami Canada", "Dawat-e-Islami Canada: masajid, Qur'an classes, weekly gatherings and donations across Canada.")
                   + header("") + HOME),
    "centres.html": (head("Centres | Dawat-e-Islami Canada", "Faizan e Madina centres of Dawat-e-Islami across Canada.")
                     + header("centres") + CENTRES_PAGE),
    "vancouver.html": (head("Faizan e Madina Vancouver | Dawat-e-Islami Canada", "Prayer times, weekly Ijtima and services at Faizan e Madina Vancouver, 7062 134 Street, Surrey, BC.")
                       + header("centres", local_prayer=True) + VANCOUVER),
    "prayer-times.html": (head("Prayer times | Faizan e Madina Vancouver", "Monthly prayer and jama'at times for Faizan e Madina Vancouver (Hanafi).")
                          + header("centres", local_prayer=True) + PT_MAIN),
}
for name, html in pages.items():
    (ROOT / name).write_text(html + FOOTER)
print("built", ", ".join(pages))
