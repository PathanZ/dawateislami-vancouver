"""Build the Dawat-e-Islami Canada website. Run: python3 build.py

Words and lists live in content.py. Events live in assets/events.js.
To add a centre, service or department, edit content.py and rebuild.
"""
import hashlib
from pathlib import Path
from content import *  # noqa: F401,F403

ROOT = Path(__file__).parent
ASSETS = ["assets/style.css", "assets/main.js", "assets/events.js"]
V = hashlib.md5(b"".join((ROOT / f).read_bytes() for f in ASSETS)).hexdigest()[:8]
HERO_VIDEO = (ROOT / "assets/video/hero.mp4").exists()


def tbc(label="TBC"):
    return f'<span class="draft">{label}</span>'


def tel(phone):
    return "".join(ch for ch in phone if ch.isdigit() or ch == "+")


ICON = {
    "salah": '<path d="M3 20h18M5 20V11l7-6 7 6v9M10 20v-5h4v5"/>',
    "jummah": '<circle cx="8" cy="9" r="3"/><circle cx="16" cy="9" r="3"/><path d="M2 20c.8-3 3-5 6-5s5.2 2 6 5M14 15.2c.6-.1 1.3-.2 2-.2 3 0 5.2 2 6 5"/>',
    "ijtima": '<path d="M12 3v3M5 21v-6a7 7 0 0114 0v6M3 21h18M9 21v-3h6v3"/>',
    "school": '<rect x="3" y="5" width="18" height="15" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "courses": '<path d="M4 4h12l4 4v12H4zM8 12h8M8 16h5"/>',
    "quran": '<path d="M4 5h7a2 2 0 012 2v12a2 2 0 00-2-2H4zM20 5h-7a2 2 0 00-2 2v12a2 2 0 012-2h7z"/>',
    "sisters": '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1-4 4-6 7-6s6 2 7 6"/>',
    "online": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4M10 9l5 2-5 2z"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z"/>',
    "jamia": '<path d="M2 9l10-5 10 5-10 5zM6 11v5c3 2 9 2 12 0v-5M22 9v6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "dept": '<path d="M4 20V8l8-4 8 4v12M9 20v-6h6v6M4 20h16"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
}


def svg(name):
    return f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'


def section_head(kicker, title, text="", left=False):
    cls = "head left" if left else "head"
    p = f"\n        <p>{text}</p>" if text else ""
    return f'''      <div class="{cls}">
        <p class="kicker">{kicker}</p>
        <h2>{title}</h2>
        <div class="ornament" aria-hidden="true">✦</div>{p}
      </div>'''


# ---------------------------------------------------------------- page shell
NAV = [("about.html", "About Us"), ("services.html", "Services"), ("departments.html", "Departments"),
       ("centres.html", "Centres"), ("events.html", "Events"), ("contact.html", "Contact")]


def head(page, title, desc):
    url = f"{SITE}/" if page == "index.html" else f"{SITE}/{page.replace('.html', '')}"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#075b48">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dawat-e-Islami Canada">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Marcellus&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v={V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def header(current):
    links = "\n      ".join(
        f'<a href="{h}"{" aria-current=page" if h == current else ""}>{t}</a>' for h, t in NAV)
    donate_cur = " aria-current=page" if current == "donate.html" else ""
    return f'''<div class="topbar">
  <div class="wrap">
    <span class="arabic bismillah" lang="ar">بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ</span>
    <a class="topbar-link" href="https://dawateislami.net/pk/islam/streaming/watch-live-youtube-madani-channel-english.htm" target="_blank" rel="noopener">Madani Channel live</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html"><img src="assets/img/logo.png" width="900" height="242" alt="Dawat-e-Islami Canada home"></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      {links}
      <a class="btn btn-gold" href="donate.html"{donate_cur}>Donate now</a>
    </nav>
  </div>
</header>
'''


def social_links():
    filled = [(n, u) for n, u in SOCIAL.items() if u]
    if not filled:
        return f'<p class="social">Follow us: {tbc("Links TBC")}</p>'
    return '<p class="social">' + " · ".join(
        f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in filled) + "</p>"


def footer():
    ww = "\n".join(f'          <li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in WORLDWIDE[:4])
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <img class="footer-logo" src="assets/img/logo-white.png" width="900" height="242" alt="Dawat-e-Islami Canada" loading="lazy">
        <p>A global, non-political movement spreading the teachings of the Qur'an and Sunnah, with {len(CENTRES)} centres across Canada.</p>
        <p class="bn">Registered Canadian charity · BN {BN}</p>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{OFFICE}</li>
          <li><a href="contact.html">Phone numbers by province</a></li>
        </ul>
        {social_links()}
      </div>
      <div>
        <h4>Quick links</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="centres.html">Centres</a></li>
          <li><a href="events.html">Events</a></li>
          <li><a href="donate.html">Donate</a></li>
        </ul>
      </div>
      <div>
        <h4>Dawat-e-Islami worldwide</h4>
        <ul>
{ww}
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© <span id="year">2026</span> Dawat-e-Islami Canada</span>
      <span><a href="privacy.html">Privacy policy</a> · <a href="terms.html">Terms of use</a></span>
    </div>
  </div>
</footer>
<script src="assets/events.js?v={V}"></script>
<script src="assets/main.js?v={V}"></script>
</body>
</html>
'''


def page_head(title, sub, crumb):
    return f'''  <section class="page-head">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span>›</span> <span aria-current="page">{crumb}</span></nav>
      <h1>{title}</h1>
      <p>{sub}</p>
    </div>
  </section>
'''


# ---------------------------------------------------------------- shared blocks
def card(icon, title, text, href=None, more="Read more"):
    body = f'''<div class="ic">{svg(icon)}</div>
          <h3>{title}</h3>
          <p>{text}</p>'''
    if href:
        return f'''        <a class="program" href="{href}">
          {body}
          <span class="when">{more} →</span>
        </a>'''
    return f'''        <article class="program">
          {body}
        </article>'''


def slug(s):
    return s.lower().replace(" ", "-")


def centre_card(c):
    q = c["address"].replace(" ", "+")
    note = f'<p class="note">{c["note"]}</p>' if c["note"] else ""
    site = (f'<a class="when" href="{c["site"]}" target="_blank" rel="noopener">Centre website →</a>'
            if c["site"] else "")
    return f'''        <article class="program centre">
          <div class="ic">{svg("pin")}</div>
          <p class="city-prov">{c["city"]}</p>
          <h3>{c["name"]}</h3>
          <p>{c["address"]}</p>
          {note}
          <p class="phone"><a href="tel:{tel(c["phone"])}">{c["phone"]}</a></p>
          <div class="centre-links">
            <a class="when" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener">Directions →</a>
            {site}
          </div>
        </article>'''


def pillars():
    items = "\n".join(
        f'        <div class="pillar"><span class="arabic" lang="ar">{ar}</span><h3>{en}</h3><p>{t}</p></div>'
        for ar, en, t in PILLARS)
    return f'''  <section class="block tint" id="pillars">
    <div class="wrap">
{section_head("Discover Islam", "The five pillars of Islam")}
      <div class="pillars">
{items}
      </div>
    </div>
  </section>
'''


HADEES = '''  <section class="block hadees" aria-labelledby="hadeesTitle">
    <div class="wrap">
      <p class="kicker" id="hadeesTitle">Hadees of the week</p>
      <p class="arabic" lang="ar">خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ</p>
      <blockquote>The best among you is the one who learns the Qur'an and teaches it.</blockquote>
      <cite>Sahih al-Bukhari, Hadith 5027</cite>
    </div>
  </section>
'''

SLOGAN = '''  <section class="slogan" aria-label="Madani Maqsad">
    <div class="wrap">
      <p class="kicker">Our Madani Maqsad</p>
      <p class="en">"I must strive to reform myself and the people of the entire world, In sha Allah."</p>
    </div>
  </section>
'''


def etransfer_list():
    rows = "\n".join(
        f'            <li><span class="et-type">{t}</span><span class="et-email">{e}</span>'
        f'<button type="button" class="copy" data-copy="{e}" aria-label="Copy {t} e-Transfer email">Copy</button></li>'
        for t, e in ETRANSFERS)
    return f'''          <ul class="et-list">
{rows}
          </ul>'''


def donate_button(cls="btn btn-green wide"):
    if DONATE_URL:
        return f'<a class="{cls}" href="{DONATE_URL}" target="_blank" rel="noopener">Donate online</a>'
    return f'<a class="{cls}" href="donate.html" aria-disabled="true">Donate online {tbc("link TBC")}</a>'


def give_box(full):
    extra = "" if full else '\n        <a class="more" href="donate.html">All ways to give →</a>'
    return f'''      <div class="give">
        <h3>Ways to give</h3>
        {donate_button()}
        <div class="etransfer">
          <b>Interac e-Transfer</b>
          <small>Faizan-e-Madina Vancouver (Surrey). Send to the email for the type of donation.</small>
{etransfer_list()}
          <small>For a tax receipt, include your full name and mailing address in the message.</small>
        </div>
        <div class="etransfer">
          <b>In person</b>
          <span>At any of our centres after prayers</span>
        </div>{extra}
      </div>'''


# ---------------------------------------------------------------- pages
def home():
    video = ('<video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="assets/img/hero.jpg" aria-hidden="true"><source src="assets/video/hero.mp4" type="video/mp4"></video>'
             if HERO_VIDEO else "")
    featured = "\n".join(card(i, t, s, f"services.html#{sid}") for sid, i, t, s, _ in
                         [x for x in SERVICES if x[0] in ("madrasa", "jamia", "weekly-school", "online-academy")])
    services = "\n".join(card(i, t, s, f"services.html#{sid}") for sid, i, t, s, _ in SERVICES[:8])
    cities = "\n".join(f'        <li><a href="centres.html#{slug(c["province"])}">{c["city"]}</a></li>'
                       for c in {c["city"]: c for c in CENTRES}.values())
    provinces = len({c["province"] for c in CENTRES})
    return f'''<main id="main">
  <section class="hero hero-global">
    {video}
    <div class="wrap">
      <p class="arabic" lang="ar">اَلسَّلَامُ عَلَيْكُمْ</p>
      <h1>Welcome to Dawat-e-Islami Canada</h1>
      <p class="tagline">Connect · Learn · Grow · Together</p>
      <p class="lead">Spreading the teachings of the Qur'an and Sunnah through our masajid, Qur'an classes and community programs across Canada.</p>
      <div class="actions">
        <a class="btn btn-gold" href="donate.html">Donate now</a>
        <a class="btn btn-line" href="centres.html">Find a centre</a>
      </div>
    </div>
  </section>

{SLOGAN}
  <section class="block alt" id="about">
    <div class="wrap about">
      <div>
{section_head("About us", "Dawat-e-Islami Canada", left=True)}
        <p>Dawat-e-Islami is an international, non-political Islamic organization working to spread the message of the Qur'an and Sunnah. It was established in 1981 in Karachi, Pakistan, by Ameer-e-Ahl-e-Sunnat, Allama Maulana Abu Bilal Muhammad Ilyas Attar Qadri.</p>
        <p>In Canada, Dawat-e-Islami has {len(CENTRES)} centres across {provinces} provinces, offering weekly gatherings, Qur'an classes for adults and children, Friday prayers and youth programs.</p>
        <a class="btn btn-green" href="about.html">Read more</a>
      </div>
      <div class="photo-slot">
        <div><strong>Photo</strong><span>One of our centres, to be added</span></div>
      </div>
    </div>
  </section>

  <section class="block" id="donate">
    <div class="wrap donate">
      <div>
{section_head("Support us", "Your donation keeps our work going", left=True)}
        <p>Donations support our masajid, Qur'an classes and community programs across Canada. Zakat, Sadaqah, Fitrah and masjid donations are all welcome.</p>
        <p class="hadith">"Charity does not decrease wealth." <span>Sahih Muslim, 2588</span></p>
        <p class="muted">Dawat-e-Islami Canada is a registered Canadian charity (BN {BN}). Official tax receipts are issued for eligible donations.</p>
      </div>
{give_box(full=False)}
    </div>
  </section>

  <section class="block alt" id="programs">
    <div class="wrap">
{section_head("Islamic education", "Your path to Islamic knowledge", "From a child's first Qur'an lesson to full scholarly training.")}
      <div class="programs four">
{featured}
      </div>
    </div>
  </section>

  <section class="block" id="services">
    <div class="wrap">
{section_head("What we offer", "Our services", "Available at our centres across Canada.")}
      <div class="programs four">
{services}
      </div>
      <p class="center-cta"><a class="btn btn-green" href="services.html">View all services</a></p>
    </div>
  </section>

{HADEES}
  <section class="block" id="events">
    <div class="wrap narrow">
{section_head("Events and activities", "What's coming up")}
      <div class="events" data-events data-limit="3"><p class="muted">Loading events…</p></div>
      <p class="center-cta"><a class="btn btn-green" href="events.html">View all events</a></p>
    </div>
  </section>

{pillars()}
  <section class="block" id="centres">
    <div class="wrap">
{section_head("Our centres", "Find a Faizan-e-Madina near you", f"{len(CENTRES)} centres in {provinces} provinces, for daily prayers, weekly gatherings and classes.")}
      <ul class="city-chips">
{cities}
      </ul>
      <p class="center-cta"><a class="btn btn-green" href="centres.html">View all centres</a></p>
    </div>
  </section>
</main>
'''


def about():
    worldwide = "\n".join(f'          <li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in WORLDWIDE)
    return f'''<main id="main">
{page_head("About us", "An international, non-political movement of the Qur'an and Sunnah", "About us")}
  <section class="block">
    <div class="wrap about">
      <div>
{section_head("Who we are", "About Dawat-e-Islami", left=True)}
        <p>Dawat-e-Islami is an international, non-political Islamic organization working to spread the message of the Qur'an and Sunnah across the world. It was established in 1981 in Karachi, Pakistan, by one of the great scholars of the present era, Ameer-e-Ahl-e-Sunnat, Allama Maulana Abu Bilal Muhammad Ilyas Attar Qadri.</p>
        <p>Today Dawat-e-Islami serves communities in many countries through Qur'an education, Islamic scholarship, publishing, the Madani Channel and welfare work.</p>
      </div>
      <div class="photo-slot">
        <div><strong>Photo</strong><span>To be added</span></div>
      </div>
    </div>
  </section>

{SLOGAN}
  <section class="block alt" id="ameer">
    <div class="wrap narrow">
{section_head("Our founder", "Ameer-e-Ahl-e-Sunnat")}
      <p>Shaykh-e-Tariqat, Ameer-e-Ahl-e-Sunnat, Allama Maulana Abu Bilal Muhammad Ilyas Attar Qadri Razavi is the founder of Dawat-e-Islami. Through his books, bayans and the Madani Muzakra, he has inspired people around the world to live by the Qur'an and Sunnah.</p>
      <p class="center-cta"><a class="btn btn-green" href="https://www.ilyasqadri.com/" target="_blank" rel="noopener">Visit his website</a></p>
    </div>
  </section>

  <section class="block" id="canada">
    <div class="wrap narrow">
{section_head("In Canada", "Dawat-e-Islami Canada")}
      <p>Dawat-e-Islami has {len(CENTRES)} centres across Canada, in British Columbia, Alberta, Saskatchewan, Manitoba, Ontario and Quebec. Through Jamia-tul-Madina in Montreal, Quebec, it is also producing the next generation of scholars.</p>
      <ul class="tick-list">
        <li>Weekly Islamic gatherings for brothers and sisters</li>
        <li>Zikr sessions</li>
        <li>Qur'an classes for adults and children</li>
        <li>Friday prayers</li>
        <li>Youth gatherings in provinces, cities and local areas</li>
      </ul>
      <p>{tbc("Add: when Dawat-e-Islami started in Canada, and a few lines of its history")}</p>
      <p class="muted">Dawat-e-Islami Canada is a registered Canadian charity, BN {BN}.</p>
      <p class="center-cta"><a class="btn btn-green" href="centres.html">See our centres</a></p>
    </div>
  </section>

  <section class="block tint">
    <div class="wrap narrow">
{section_head("Learn more", "Dawat-e-Islami worldwide")}
      <ul class="link-list">
{worldwide}
      </ul>
    </div>
  </section>
</main>
'''


def services_page():
    blocks = "\n".join(f'''        <article class="service" id="{sid}">
          <div class="ic">{svg(i)}</div>
          <div>
            <h2>{t}</h2>
            <p>{long}</p>
          </div>
        </article>''' for sid, i, t, _, long in SERVICES)
    return f'''<main id="main">
{page_head("Our services", "Your one-stop destination for Islamic learning and growth", "Services")}
  <section class="block">
    <div class="wrap narrow">
      <p class="intro">Dawat-e-Islami Canada offers a wide range of services to support the community. Religious activities are free of charge. Programs and timings vary by centre, so please contact your nearest centre for details.</p>
      <div class="service-list">
{blocks}
      </div>
      <p class="center-cta"><a class="btn btn-green" href="centres.html">Find your nearest centre</a></p>
    </div>
  </section>
</main>
'''


def departments_page():
    cards = "\n".join(card("dept", n, d) for n, d in DEPARTMENTS)
    return f'''<main id="main">
{page_head("Departments", "The departments that carry out the work of Dawat-e-Islami Canada", "Departments")}
  <section class="block">
    <div class="wrap">
      <p class="intro center">Each department focuses on one area of service, from Qur'an education to welfare and media.</p>
      <div class="programs four">
{cards}
      </div>
    </div>
  </section>
</main>
'''


def centres_page():
    provs = list(dict.fromkeys(c["province"] for c in CENTRES))
    groups = []
    for prov in provs:
        cards = "\n".join(centre_card(c) for c in CENTRES if c["province"] == prov)
        groups.append(f'''    <h2 class="prov" id="{slug(prov)}">{prov}</h2>
    <div class="programs centres-grid">
{cards}
    </div>''')
    jump = "".join(f'<a href="#{slug(p)}">{p}</a>' for p in provs)
    return f'''<main id="main">
{page_head("Our centres in Canada", f"{len(CENTRES)} Faizan-e-Madina centres of Dawat-e-Islami across Canada", "Centres")}
  <div class="wrap pt-main">
    <nav class="jump" aria-label="Provinces">{jump}</nav>
{chr(10).join(groups)}
    <p class="muted centres-note">Is a centre missing or out of date? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</main>
'''


def events_page():
    return f'''<main id="main">
{page_head("Events and activities", "Gatherings, programs and announcements across Canada", "Events")}
  <section class="block">
    <div class="wrap narrow">
      <div class="events" data-events><p class="muted">Loading events…</p></div>
      <p class="muted centres-note">Weekly gatherings take place at every centre. Contact your <a href="centres.html">nearest centre</a> for its schedule.</p>
    </div>
  </section>
</main>
'''


def donate_page():
    types = "\n".join(f'          <li><b>{t}</b><span>{d}</span></li>' for t, d in DONATION_TYPES)
    return f'''<main id="main">
{page_head("Donate", "Support our masajid, Qur'an classes and community programs", "Donate")}
  <section class="block">
    <div class="wrap donate">
      <div>
{section_head("Support us", "Your extra is someone's need", left=True)}
        <p>Every donation helps keep our centres open, pays for Qur'an classes and supports the community. Please choose the type of donation so it is used correctly.</p>
        <p class="hadith">"Charity does not decrease wealth." <span>Sahih Muslim, 2588</span></p>
        <ul class="types">
{types}
        </ul>
      </div>
{give_box(full=True)}
    </div>
  </section>

  <section class="block alt">
    <div class="wrap narrow">
{section_head("Tax receipts", "Official donation receipts")}
      <p>Dawat-e-Islami Canada is a registered Canadian charity (BN {BN}). Official tax receipts are issued for eligible donations.</p>
      <p>When donating by Interac e-Transfer, include your <b>full name and mailing address</b> in the message so a receipt can be issued. For receipt questions, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </section>
</main>
'''


def contact_page():
    groups = []
    for prov in dict.fromkeys(c["province"] for c in CENTRES):
        seen, rows = set(), []
        for c in CENTRES:
            if c["province"] == prov and (c["city"], c["phone"]) not in seen:
                seen.add((c["city"], c["phone"]))
                rows.append(f'<li><span>{c["city"]}</span><a href="tel:{tel(c["phone"])}">{c["phone"]}</a></li>')
        groups.append(f'''        <div class="contact-prov">
          <h3>{prov}</h3>
          <ul>{"".join(rows)}</ul>
        </div>''')
    return f'''<main id="main">
{page_head("Contact us", "We would love to hear from you", "Contact")}
  <section class="block">
    <div class="wrap contact-top">
      <a class="contact-card" href="mailto:{EMAIL}">
        <div class="ic">{svg("mail")}</div>
        <h2>Email</h2>
        <p>{EMAIL}</p>
      </a>
      <div class="contact-card">
        <div class="ic">{svg("pin")}</div>
        <h2>Registered office</h2>
        <p>{OFFICE}</p>
      </div>
    </div>
  </section>
  <section class="block alt">
    <div class="wrap">
{section_head("By province", "Phone numbers", "Call the number for your area. For centre addresses, see the centres page.")}
      <div class="contact-grid">
{chr(10).join(groups)}
      </div>
      <p class="center-cta"><a class="btn btn-green" href="centres.html">View all centres</a></p>
    </div>
  </section>
</main>
'''


def privacy_page():
    return f'''<main id="main">
{page_head("Privacy policy", "How this website handles your information", "Privacy policy")}
  <section class="block">
    <div class="wrap narrow prose">
      <p class="muted">Last updated: October 2026. {tbc("Draft, to be reviewed by management")}</p>
      <h2>What we collect</h2>
      <p>This website does not ask you to create an account and does not use advertising or tracking cookies. We may use privacy-friendly visitor statistics (such as Cloudflare Web Analytics) that count page visits without identifying you.</p>
      <h2>When you contact us</h2>
      <p>If you email or phone us, we use your details only to reply to you, and we do not sell or share them.</p>
      <h2>Donations</h2>
      <p>Online donations are processed by a third-party payment provider, and Interac e-Transfers by your bank. Their privacy policies apply. We keep the name and address you give us only to issue tax receipts and to meet the Canada Revenue Agency's record-keeping requirements.</p>
      <h2>Links to other websites</h2>
      <p>This site links to other Dawat-e-Islami websites, YouTube and map services, which have their own privacy policies.</p>
      <h2>Questions</h2>
      <p>For any privacy question, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </section>
</main>
'''


def terms_page():
    return f'''<main id="main">
{page_head("Terms of use", "Using this website", "Terms of use")}
  <section class="block">
    <div class="wrap narrow prose">
      <p class="muted">Last updated: October 2026. {tbc("Draft, to be reviewed by management")}</p>
      <h2>About this website</h2>
      <p>This website is run by Dawat-e-Islami Canada, a registered Canadian charity (BN {BN}), to share information about our centres, programs and events.</p>
      <h2>Accuracy</h2>
      <p>We try to keep all information, including timings and addresses, accurate and up to date. Timings can change, so please confirm with the centre before travelling.</p>
      <h2>Content</h2>
      <p>The text, images and logos on this site belong to Dawat-e-Islami Canada or are used with permission. Please do not reuse them without permission.</p>
      <h2>External links</h2>
      <p>We are not responsible for the content of other websites we link to.</p>
      <h2>Contact</h2>
      <p>Questions about these terms can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </section>
</main>
'''


def not_found():
    return f'''<main id="main">
{page_head("Page not found", "The page you are looking for has moved or does not exist", "Not found")}
  <section class="block">
    <div class="wrap narrow center">
      <p><a class="btn btn-green" href="index.html">Go to the home page</a></p>
    </div>
  </section>
</main>
'''


PAGES = {
    "index.html": ("Dawat-e-Islami Canada", "Dawat-e-Islami Canada: masajid, Qur'an classes, weekly gatherings and community programs across Canada.", home),
    "about.html": ("About us | Dawat-e-Islami Canada", "About Dawat-e-Islami, its founder Ameer-e-Ahl-e-Sunnat, and its work in Canada.", about),
    "services.html": ("Services | Dawat-e-Islami Canada", "Weekly Ijtima, Madrasa-tul-Madina, Qur'an classes, Islamic school, courses and more.", services_page),
    "departments.html": ("Departments | Dawat-e-Islami Canada", "The departments of Dawat-e-Islami Canada.", departments_page),
    "centres.html": ("Centres | Dawat-e-Islami Canada", "Faizan-e-Madina centres of Dawat-e-Islami across Canada, with addresses and phone numbers.", centres_page),
    "events.html": ("Events | Dawat-e-Islami Canada", "Upcoming gatherings, programs and announcements from Dawat-e-Islami Canada.", events_page),
    "donate.html": ("Donate | Dawat-e-Islami Canada", "Donate Zakat, Sadaqah, Fitrah and more to Dawat-e-Islami Canada, a registered Canadian charity.", donate_page),
    "contact.html": ("Contact | Dawat-e-Islami Canada", "Contact Dawat-e-Islami Canada by email or phone.", contact_page),
    "privacy.html": ("Privacy policy | Dawat-e-Islami Canada", "Privacy policy of the Dawat-e-Islami Canada website.", privacy_page),
    "terms.html": ("Terms of use | Dawat-e-Islami Canada", "Terms of use of the Dawat-e-Islami Canada website.", terms_page),
    "404.html": ("Page not found | Dawat-e-Islami Canada", "This page could not be found.", not_found),
}

NO_NAV = {"index.html", "privacy.html", "terms.html", "404.html"}

for name, (title, desc, fn) in PAGES.items():
    current = "" if name in NO_NAV else name
    (ROOT / name).write_text(head(name, title, desc) + header(current) + fn() + footer())

# Old Vancouver pages now live on the Vancouver centre's own site
for old in ["vancouver.html", "prayer-times.html"]:
    (ROOT / old).write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Moved | Dawat-e-Islami Canada</title>
<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={VANCOUVER_SITE}">
<link rel="canonical" href="{VANCOUVER_SITE}"></head>
<body><p>This page has moved to <a href="{VANCOUVER_SITE}">{VANCOUVER_SITE}</a>.</p></body></html>
''')

# Hosting files (Cloudflare Pages reads _redirects and _headers)
(ROOT / "_redirects").write_text(f"""/vancouver.html {VANCOUVER_SITE} 301
/vancouver {VANCOUVER_SITE} 301
/prayer-times.html {VANCOUVER_SITE} 301
/prayer-times {VANCOUVER_SITE} 301
""")
(ROOT / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()
""")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = "\n".join(
    f"  <url><loc>{SITE}/{'' if n == 'index.html' else n.replace('.html', '')}</loc></url>"
    for n in PAGES if n != "404.html")
(ROOT / "sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')

print("built", len(PAGES), "pages, version", V)
