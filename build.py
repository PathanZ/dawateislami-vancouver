"""Build the Dawat-e-Islami Canada website. Run: python3 build.py

Words and lists live in content.py. One-off announcements live in assets/events.js.
Every page is generated from here, so edit content.py (not the .html files) and rebuild.
"""
import hashlib
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import quote, quote_plus
from content import *  # noqa: F401,F403

ROOT = Path(__file__).parent
ASSETS = ["assets/style.css", "assets/main.js", "assets/events.js"]
V = hashlib.md5(b"".join((ROOT / f).read_bytes() for f in ASSETS)).hexdigest()[:8]
EXT = ROOT / "assets/img/ext"
OPT = ROOT / "assets/img/opt"
REMOTE = set()          # every remote picture used, so they can be downloaded later (see README)
WRITTEN = []            # every page written, for the sitemap
CENTRE = {c["slug"]: c for c in CENTRES}


# ---------------------------------------------------------------- helpers
def e(s):
    return escape(str(s), quote=True)


def tel(phone):
    return "".join(ch for ch in phone if ch.isdigit() or ch == "+")


def phone_link(p):
    return '<span class="tbd">TBD</span>' if p == "TBD" else f'<a href="tel:{tel(p)}">{e(p)}</a>'


def local_name(url):
    name = url.split("?")[0].rstrip("/").split("/")[-1]
    return re.sub(r"[^A-Za-z0-9._-]", "_", name)


def img(url, pre):
    """Use a downloaded copy in assets/img/ext/ when there is one, otherwise the original address."""
    if not url:
        return ""
    if url.startswith("http"):
        REMOTE.add(url)
        if (OPT / (local_name(url) + ".webp")).exists():
            return f"{pre}assets/img/opt/{local_name(url)}.webp"
        if (EXT / local_name(url)).exists():
            return f"{pre}assets/img/ext/{local_name(url)}"
        return url
    return pre + url


def srcset(url, pre):
    """Let phones download the smaller copy of a card picture."""
    small = OPT / (local_name(url) + ".480.webp")
    if url.startswith("http") and small.exists():
        return (f' srcset="{pre}assets/img/opt/{small.name} 480w, {img(url, pre)} 960w"'
                f' sizes="(max-width: 700px) 92vw, 400px"')
    return ""


def maps_search(q):
    return "https://www.google.com/maps/search/?api=1&amp;query=" + quote_plus(q)


def map_box(q, title, fid=""):
    """A map that only loads when tapped, to save mobile data and keep pages fast."""
    idattr = f' id="{fid}"' if fid else ""
    return (f'<div class="map" data-map="{maps_embed(q)}" data-title="{title}"{idattr}>'
            f'<button type="button" class="map-load">{svg("pin", 28)}<b>Show map</b><span>{e(q)}</span></button>'
            f'<noscript><a class="link" href="{maps_search(q)}">Open in Google Maps</a></noscript></div>')


def maps_embed(q):
    return "https://www.google.com/maps?q=" + quote_plus(q) + "&amp;output=embed"


ICON = {
    "ijtima": '<path d="M12 3v3M5 21v-6a7 7 0 0114 0v6M3 21h18M9 21v-3h6v3"/>',
    "jummah": '<path d="M3 20h18M5 20V11l7-6 7 6v9M10 20v-5h4v5"/>',
    "school": '<rect x="3" y="5" width="18" height="15" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "courses": '<path d="M4 4h12l4 4v12H4zM8 12h8M8 16h5"/>',
    "quran": '<path d="M4 5h7a2 2 0 012 2v12a2 2 0 00-2-2H4zM20 5h-7a2 2 0 00-2 2v12a2 2 0 012-2h7z"/>',
    "book": '<path d="M5 4h11a3 3 0 013 3v13H8a3 3 0 01-3-3zM5 17a3 3 0 013-3h11"/>',
    "online": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4M10 9l5 2-5 2z"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z"/>',
    "jamia": '<path d="M2 9l10-5 10 5-10 5zM6 11v5c3 2 9 2 12 0v-5M22 9v6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "dept": '<path d="M4 20V8l8-4 8 4v12M9 20v-6h6v6M4 20h16"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
}


def svg(name, size=24):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')


def sec_head(kicker, title, lead="", link=None):
    l = f'<p class="lead">{lead}</p>' if lead else ""
    a = f'<a class="btn btn-line" href="{link[0]}">{link[1]}</a>' if link else ""
    return f'''      <div class="sec-head">
        <div><p class="kicker">{kicker}</p><h2>{title}</h2>{l}</div>
        {a}
      </div>'''


# ---------------------------------------------------------------- page shell
NAV = [("about.html", "About"), ("departments.html", "Departments"), ("centres.html", "Centres"),
       ("events.html", "Events &amp; Classes"), ("jamia.html", "Jamia"), ("contact.html", "Contact")]


FONTS = "https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&amp;family=Plus+Jakarta+Sans:wght@400;600;700;800&amp;display=swap"


def head(path, title, desc, pre):
    url = f"{SITE}/" if path == "index.html" else f"{SITE}/{path.replace('.html', '')}"
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<script>document.documentElement.className="js"</script>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#12285f">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dawat-e-Islami Canada">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{pre}assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{pre}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="manifest" href="{pre}manifest.webmanifest">
<link rel="stylesheet" href="{pre}assets/style.css?v={V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def header(current, pre):
    links = "\n      ".join(
        '<a href="' + pre + h + '"' + (' aria-current="page"' if h == current else "") + '>' + t + '</a>' for h, t in NAV)
    dc = ' aria-current="page"' if current == "donate.html" else ""
    return f'''<div class="topbar">
  <div class="wrap">
    <span class="arabic bismillah" lang="ar">بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ</span>
    <a class="live" href="{LIVE_URL}" target="_blank" rel="noopener">Madani Channel live</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{pre}index.html"><img src="{pre}assets/img/logo-sm.webp" width="400" height="108" alt="Dawat-e-Islami Canada home"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      {links}
      <a class="nav-donate" href="{pre}donate.html"{dc}>Donate</a>
    </nav>
  </div>
</header>
'''


def footer(pre):
    ww = "\n".join(f'          <li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in WORLDWIDE)
    social = [(n, u) for n, u in SOCIAL.items() if u]
    soc = ("\n        <p>" + " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in social) + "</p>") if social else ""
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <img class="footer-logo" src="{pre}assets/img/logo-white-sm.webp" width="400" height="108" alt="Dawat-e-Islami Canada" loading="lazy">
        <p>A global, non-political movement spreading the teachings of the Qur'an and Sunnah, with {len(CENTRES)} centres across Canada.</p>
        <p class="bn">Registered Canadian charity · BN {BN}</p>{soc}
      </div>
      <div>
        <h2 class="fh">Visit</h2>
        <ul>
          <li><a href="{pre}centres.html">Centres</a></li>
          <li><a href="{pre}events.html">Events</a></li>
          <li><a href="{pre}events.html#courses">Classes &amp; courses</a></li>
          <li><a href="{pre}jamia.html">Jamia-tul-Madina</a></li>
          <li><a href="{LIVE_URL}" target="_blank" rel="noopener">Madani Channel live</a></li>
        </ul>
      </div>
      <div>
        <h2 class="fh">Give &amp; contact</h2>
        <ul>
          <li><a href="{pre}donate.html">Donate</a></li>
          <li><a href="{pre}receipt.html">Donation receipt</a></li>
          <li><a href="{pre}contact.html">Contact us</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h2 class="fh">Dawat-e-Islami worldwide</h2>
        <ul>
{ww}
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© <span id="year">2026</span> Dawat-e-Islami Canada</span>
      <span><a href="{pre}privacy.html">Privacy policy</a> · <a href="{pre}terms.html">Terms of use</a></span>
    </div>
  </div>
</footer>
<script src="{pre}assets/events.js?v={V}"></script>
<script src="{pre}assets/main.js?v={V}"></script>
</body>
</html>
'''


def page_head(title, sub, crumbs, pre, actions="", image="", poster=False):
    trail = f'<a href="{pre}index.html">Home</a>'
    for label, href in crumbs[:-1]:
        trail += f' <span>›</span> <a href="{pre}{href}">{label}</a>'
    trail += f' <span>›</span> <span aria-current="page">{crumbs[-1][0]}</span>'
    act = f'\n        <div class="actions">{actions}</div>' if actions else ""
    text = f'''<div>
        <nav class="crumbs" aria-label="Breadcrumb">{trail}</nav>
        <h1>{title}</h1>
        <p class="sub">{sub}</p>{act}
      </div>'''
    if image:
        return f'''  <section class="page-head has-img"><div class="wrap"><div class="tile-head">
      {text}
      <div class="head-img{' poster' if poster else ''}"><img src="{image}" alt="" loading="eager"></div>
    </div></div></section>
'''
    return f'''  <section class="page-head"><div class="wrap"><div class="tile-head">
      {text}
    </div></div></section>
'''


def write(path, title, desc, body_fn, current=""):
    depth = path.count("/")
    pre = "../" * depth
    html = head(path, title, desc, pre) + header(current, pre) + body_fn(pre) + footer(pre)
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    WRITTEN.append(path)


# ---------------------------------------------------------------- shared blocks
def centre_card(c, pre, show_map=False):
    note = f'<span class="note">{c["note"]}</span>' if c["note"] else ""
    site = f'<a href="{c["site"]}" target="_blank" rel="noopener">Website</a>' if c["site"] else ""
    mapb = (f'<a href="#map" class="map-btn" data-q="{e(c["address"])}" data-name="{e(c["name"])}">Show on map</a>'
            if show_map else "")
    return f'''        <article class="card pcard">
          <a class="ph" href="{pre}centres/{c["slug"]}.html" tabindex="-1" aria-hidden="true"><img src="{img(c["img"], pre)}"{srcset(c["img"], pre)} alt="" loading="lazy"></a>
          <div class="bd">
            <p class="city">{c["city"]}, {c["province"]}</p>
            <h3>{c["name"]}</h3>
            {note}
            <p>{c["address"]}</p>
            <p class="meta">{phone_link(c["phone"])}</p>
            <div class="card-links">
              <a href="{pre}centres/{c["slug"]}.html">View centre</a>
              {mapb}
              <a href="{maps_search(c["address"])}" target="_blank" rel="noopener">Directions</a>
              {site}
              <a class="don" href="{pre}donate.html?centre={c["slug"]}">Donate</a>
            </div>
          </div>
        </article>'''


def day_badge(day, time):
    return f'<div class="day"><small>Every</small><b>{day[:3]}</b></div>'


def event_card(ev, pre):
    c = CENTRE[ev["centre"]]
    sis = '<span class="sis">Sisters welcome</span>' if ev["sisters"] else ""
    return f'''        <a class="card ev" href="{pre}events/{ev["slug"]}.html">
          <div class="when">{day_badge(ev["day"], ev["time"])}<div><p class="city">{ev["kind"]}</p><h3>{ev["title"]}</h3></div></div>
          <p class="meta">Every {ev["day"]} · {ev["time"]}</p>
          <p>{c["name"]}</p>
          {sis}
          <span class="more">Details →</span>
        </a>'''


def course_card(co, pre):
    ph = (f'<div class="ph poster"><img src="{img(co["img"], pre)}"{srcset(co["img"], pre)} alt="" loading="lazy"></div>' if co["img"]
          else f'<div class="ph icon">{svg("quran")}</div>')
    ages = (f'Ages {co["ages"]}' if co["ages"][:1].isdigit() else co["ages"])
    bits = " · ".join(x for x in [co["when"], ages] if x)
    return f'''        <a class="card pcard" href="{pre}courses/{co["slug"]}.html">
          {ph}
          <div class="bd">
            <p class="city">{co["city"]}</p>
            <h3>{co["title"]}</h3>
            <p class="meta">{bits}</p>
            <p>{phone_text(co["phones"][0])}</p>
            <span class="more">Details →</span>
          </div>
        </a>'''


def phone_text(p):
    return "Phone TBD" if p == "TBD" else p


def dept_href(slug, pre):
    if slug == "jamia":
        return f"{pre}jamia.html"
    if slug == "courses":
        return f"{pre}events.html#courses"
    if slug in ("education", "it"):
        return f"{pre}contact.html"
    return f"{pre}departments/{slug}.html"


def dept_card(d, pre):
    slug, icon, name, short, _, _ = d
    return f'''        <a class="card" href="{dept_href(slug, pre)}">
          <div class="ic">{svg(icon)}</div>
          <h3>{name}</h3>
          <p>{short}</p>
          <span class="more">Learn more →</span>
        </a>'''


def pillars_grid(pre):
    items = "\n".join(
        f'''        <a class="pillar" href="{pre}islam/{s}.html"><span class="arabic" lang="ar">{ar}</span><small>{num} pillar</small><h3>{en}</h3><p>{short}</p></a>'''
        for s, ar, en, num, _, short, _ in PILLARS)
    return f'      <div class="pillars">\n{items}\n      </div>'


def etransfer_list():
    rows = "\n".join(
        f'            <li><span class="et-type">{t}</span><span class="et-email">{em}</span>'
        f'<button type="button" class="copy" data-copy="{em}" aria-label="Copy {t} e-Transfer email">Copy</button></li>'
        for t, em in ETRANSFERS)
    return f'          <ul class="et-list">\n{rows}\n          </ul>'


def appeal(pre):
    chips = "".join(f'<a href="{pre}donate.html?purpose={k}">{n}</a>' for k, n, _ in DONATION_PURPOSES)
    return f'''  <section class="section">
    <div class="wrap appeal">
      <div class="tile navy">
        <p class="kicker">Donation appeal</p>
        <h2>Zakat, Fitrana and Sadaqah</h2>
        <p>Your donation keeps our masajid open, pays for free Qur'an classes and supports the training of scholars across Canada. Choose where your donation goes.</p>
        <div class="purpose-chips">{chips}</div>
        <div class="actions"><a class="btn btn-gold" href="{pre}donate.html">Donate now</a><a class="btn btn-ghost" href="{pre}receipt.html">Request a receipt</a></div>
      </div>
      <div class="tile img"><img src="{img(APPEAL_IMG, pre)}" alt="Dawat-e-Islami donation campaign" loading="lazy"></div>
    </div>
  </section>
'''


# ---------------------------------------------------------------- home
def home(pre):
    slides = "\n".join(
        f'          <div class="slide{" on" if i == 0 else ""}"><img src="{img(u, pre)}" alt="{e(a)}" {'loading="eager" fetchpriority="high"' if i == 0 else 'loading="lazy"'}></div>'
        for i, (u, a) in enumerate(HERO_SLIDES))
    dots = "".join(f'<span{" class=on" if i == 0 else ""}></span>' for i in range(len(HERO_SLIDES)))
    nxt = EVENTS[0]
    provinces = len({c["province"] for c in CENTRES})
    events = "\n".join(event_card(ev, pre) for ev in EVENTS[:4])
    courses = "\n".join(course_card(co, pre) for co in [x for x in COURSES if x["img"]][:4])
    depts = "\n".join(dept_card(d, pre) for d in DEPARTMENTS[:4])
    centres = "\n".join(centre_card(c, pre) for c in CENTRES[:6])
    books = "\n".join(
        f'''        <a class="book" href="{u}" target="_blank" rel="noopener"><div class="cover"><small>Free booklet</small><b>{t}</b></div><span>Read PDF →</span></a>'''
        for t, u in BOOKS)
    vids = "\n".join(
        f'''        <div class="video"><div class="frame" data-yt="{vid}"><img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy"><button class="play" type="button" aria-label="Play video: {e(t)}"><span>▶</span></button></div><p>{t}</p></div>'''
        for vid, t in VIDEOS)
    return f'''<main id="main">
  <section>
    <div class="wrap bento">
      <div class="tile navy b-hero">
        <div>
          <p class="salaam arabic" lang="ar">اَلسَّلَامُ عَلَيْكُمْ</p>
          <h1>Welcome to Dawat-e-Islami Canada</h1>
        </div>
        <p class="lead">A global, non-political movement spreading the teachings of the Qur'an and Sunnah, serving communities at {len(CENTRES)} centres across Canada since its founding in 1981.</p>
        <div class="actions">
          <a class="btn btn-gold" href="{pre}donate.html">Donate</a>
          <a class="btn btn-ghost" href="{pre}centres.html">Find a centre</a>
          <a class="btn btn-ghost" href="{pre}events.html">See what's on</a>
        </div>
      </div>
      <a class="tile gold b-donate" href="{pre}donate.html">
        <h2 class="h3">Donate</h2>
        <p>Zakat, Fitrana, Sadaqah and masjid building →</p>
      </a>
      <a class="tile navy b-live" href="{LIVE_URL}" target="_blank" rel="noopener"><span class="chip">● Live now</span><h2 class="h3">Madani Channel</h2><p>Watch in English, 24/7 →</p></a>
      <a class="tile b-next" href="{pre}events/{nxt["slug"]}.html" style="text-decoration:none;color:inherit">
        <span class="chip">{nxt["day"]}s</span>
        <h2 class="h3">{nxt["title"]}</h2>
        <p class="muted">{nxt["time"]}</p>
      </a>
      <a class="tile sky b-next" href="{pre}events.html#courses" style="text-decoration:none;color:inherit">
        <span class="chip">{len(COURSES)} classes</span>
        <h2 class="h3">Qur'an classes</h2>
        <p class="muted">For children and adults</p>
      </a>
      <div class="tile b-slider" data-slider role="region" aria-roledescription="carousel" aria-label="Highlights">
        <div class="slides">
{slides}
        </div>
        <div class="slide-dots" aria-hidden="true">{dots}</div>
        <div class="slide-ctrl"><button type="button" data-prev aria-label="Previous slide">‹</button><button type="button" data-next aria-label="Next slide">›</button></div>
      </div>
    </div>
  </section>

  <section class="section tight" aria-label="Dawat-e-Islami Canada in numbers">
    <div class="wrap stats">
      <div class="tile"><b>{len(CENTRES)}</b><span>Centres across Canada</span></div>
      <div class="tile"><b>{len(EVENTS)}</b><span>Weekly gatherings &amp; prayers</span></div>
      <div class="tile"><b>{len(COURSES)}</b><span>Courses &amp; classes</span></div>
      <div class="tile"><b>{len(DEPARTMENTS)}</b><span>Departments</span></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="tile">
        <p class="kicker">About us</p>
        <h2 style="margin:6px 0 14px">Dawat-e-Islami Canada</h2>
        <div class="prose">
          <p>Dawat-e-Islami is a global, non-political Islamic organization working to spread the Qur'an and Sunnah. It was founded in 1981 in Karachi by Ameer-e-Ahl-e-Sunnat, Allama Maulana Muhammad Ilyas Attar Qadri.</p>
          <p>Its departments run masajid, Qur'an classes, Islamic schools, Jamias, spiritual cure and welfare work. In Canada, this work reaches communities in {provinces} provinces.</p>
        </div>
        <p style="margin-top:14px"><a class="btn btn-navy" href="{pre}about.html">Read our story</a></p>
      </div>
      <div class="tile cream">
        <div class="founder">
          <img src="{img(FOUNDER_IMG, pre)}" alt="Ameer-e-Ahl-e-Sunnat, founder of Dawat-e-Islami" loading="lazy">
          <div>
            <p class="kicker">Our founder</p>
            <blockquote>"I must strive to reform myself and the people of the entire world."</blockquote>
            <cite>Ameer-e-Ahl-e-Sunnat, Maulana Muhammad Ilyas Attar Qadri</cite>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{sec_head("Events and gatherings", "Join us this week", "Weekly gatherings and Friday prayers at our centres, open to everyone.", (pre + "events.html", "All events"))}
      <div class="cards">
{events}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{sec_head("Courses and classes", "Learn with us", "Qur'an classes, Islamic school and courses for children and adults.", (pre + "events.html#courses", "All classes"))}
      <div class="cards">
{courses}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{sec_head("Our departments", "Your path to Islamic knowledge", "From a child's first Qur'an lesson to full scholarly training.", (pre + "departments.html", "All departments"))}
      <div class="cards">
{depts}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{sec_head("Discover Islam", "The five pillars of Islam")}
{pillars_grid(pre)}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{sec_head("Our centres", "Find a centre near you", f"{len(CENTRES)} centres in {provinces} provinces, for prayers, weekly gatherings and classes.", (pre + "centres.html", "All centres"))}
      <div class="cards three">
{centres}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{sec_head("Books", "Free Islamic booklets", "Read online or download, free of charge.", (BOOKS_LIBRARY, "Full library"))}
      <div class="books">
{books}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
{sec_head("Media", "Watch and learn", "Videos from Dawat-e-Islami, and the Madani Channel live in English.", (LIVE_URL, "Watch live"))}
      <div class="videos">
{vids}
      </div>
    </div>
  </section>

{appeal(pre)}</main>
'''


# ---------------------------------------------------------------- about
def about(pre):
    ww = "\n".join(f'          <li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in WORLDWIDE)
    provinces = len({c["province"] for c in CENTRES})
    return f'''<main id="main">
{page_head("About Dawat-e-Islami", "A global, non-political movement for the Qur'an and Sunnah", [("About", "about.html")], pre)}
  <section class="section">
    <div class="wrap split">
      <div class="tile prose">
        <p class="kicker">Who we are</p>
        <h2>Dawat-e-Islami</h2>
        <p>Dawat-e-Islami is a global, non-political Islamic organization working to spread the teachings of the Qur'an and Sunnah. It was founded in 1981 in Karachi, Pakistan, by Ameer-e-Ahl-e-Sunnat, Hazrat Allama Maulana Muhammad Ilyas Attar Qadri Razavi.</p>
        <p>Today its departments serve communities in many countries: masajid and Islamic centres, Qur'an classes, Islamic schools, Jamias that train scholars, spiritual cure, funeral services, the Madani Channel and welfare work.</p>
        <p>Its work rests on four values: the Qur'an and Sunnah, education, welfare and spiritual reform.</p>
      </div>
      <div class="tile cream">
        <div class="founder">
          <img src="{img(FOUNDER_IMG, pre)}" alt="Ameer-e-Ahl-e-Sunnat, founder of Dawat-e-Islami" loading="lazy">
          <div>
            <p class="kicker">Our founder</p>
            <blockquote>"I must strive to reform myself and the people of the entire world."</blockquote>
            <cite>Ameer-e-Ahl-e-Sunnat, a scholar and spiritual guide of the 21st century</cite>
            <p style="margin-top:12px"><a class="link" href="https://www.ilyasqadri.com/" target="_blank" rel="noopener">Visit his website →</a></p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section tight">
    <div class="wrap split">
      <div class="tile prose">
        <p class="kicker">In Canada</p>
        <h2>Dawat-e-Islami Canada</h2>
        <p>Dawat-e-Islami Canada carries this work into Canadian communities, with {len(CENTRES)} centres in {provinces} provinces and Jamia-tul-Madina campuses in Montreal and Cornwall.</p>
        <ul>
          <li>Weekly gatherings for brothers and sisters</li>
          <li>Friday prayers and daily congregational prayers</li>
          <li>Qur'an classes for children and adults</li>
          <li>Weekend Islamic school and youth classes</li>
          <li>Scholarly training at Jamia-tul-Madina</li>
        </ul>
        <p><span class="tbd">TBD</span> When Dawat-e-Islami started in Canada, and a few lines of its history.</p>
        <p class="muted">Dawat-e-Islami Canada is a registered Canadian charity, BN {BN}.</p>
      </div>
      <div class="tile">
        <p class="kicker">Learn more</p>
        <h2 style="margin:6px 0 10px">Dawat-e-Islami worldwide</h2>
        <ul class="facts">
{ww.replace("<li>", '<li class="one">')}
        </ul>
      </div>
    </div>
  </section>
  <div class="wrap center-cta"><a class="btn btn-navy" href="{pre}centres.html">Find a centre</a> <a class="btn btn-line" href="{pre}departments.html">Our departments</a></div>
</main>
'''


# ---------------------------------------------------------------- departments
def departments_page(pre):
    cards = "\n".join(dept_card(d, pre) for d in DEPARTMENTS)
    more = "\n".join(f'''        <div class="card"><div class="ic">{svg("dept")}</div><h3>{n}</h3><p>{t}</p></div>''' for n, t in MORE_DEPARTMENTS)
    return f'''<main id="main">
{page_head("Our departments", "Each department focuses on one area of service, from Qur'an education to welfare and media.", [("Departments", "departments.html")], pre)}
  <section class="section">
    <div class="wrap">
      <div class="cards">
{cards}
      </div>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap">
{sec_head("Also part of Dawat-e-Islami", "More departments")}
      <div class="cards">
{more}
      </div>
    </div>
  </section>
</main>
'''


def dept_detail(d):
    slug, icon, name, short, long, image = d

    def body(pre):
        return f'''<main id="main">
{page_head(name, short, [("Departments", "departments.html"), (name, "")], pre, image=img(image, pre) if image else "")}
  <section class="section">
    <div class="wrap detail">
      <div class="tile prose">
        <p class="kicker">About this department</p>
        <h2>{name}</h2>
        <p>{long}</p>
        <p>Programs and timings vary by centre. Contact your nearest centre to join or to learn more.</p>
      </div>
      <div class="side">
        <div class="tile sky">
          <h2 class="h3">Get involved</h2>
          <p>Find a centre near you, or send us a message.</p>
          <div class="actions" style="margin-top:12px"><a class="btn btn-navy" href="{pre}centres.html">Find a centre</a><a class="btn btn-line" href="{pre}contact.html">Contact us</a></div>
        </div>
        <div class="tile cream">
          <h2 class="h3">Support this work</h2>
          <p>Donations to {name} help keep it free for everyone.</p>
          <p style="margin-top:12px"><a class="btn btn-gold" href="{pre}donate.html{donate_param(slug)}">Donate</a></p>
        </div>
      </div>
    </div>
  </section>
</main>
'''
    return body


def donate_param(dept_slug):
    m = {"madrasa-tul-madina": "madrasa", "spiritual-cure": "spiritual-cure", "madani-channel": "madani-channel"}
    return f"?purpose={m[dept_slug]}" if dept_slug in m else ""


# ---------------------------------------------------------------- centres
def centres_page(pre):
    provs = list(dict.fromkeys(c["province"] for c in CENTRES))
    groups = []
    for prov in provs:
        cards = "\n".join(centre_card(c, pre, True) for c in CENTRES if c["province"] == prov)
        groups.append(f'''    <h2 class="prov" id="{prov.lower().replace(" ", "-")}">{prov}</h2>
    <div class="cards three">
{cards}
    </div>''')
    jump = "".join(f'<a href="#{p.lower().replace(" ", "-")}">{p}</a>' for p in provs) + f'<a href="{pre}jamia.html">Jamia-tul-Madina</a>'
    first = CENTRES[0]
    return f'''<main id="main">
{page_head("Our centres", f"{len(CENTRES)} Dawat-e-Islami centres across Canada, for prayers, weekly gatherings and classes.", [("Centres", "centres.html")], pre)}
  <section class="section tight">
    <div class="wrap">
      <div class="centre-map" id="map">
        <div class="tile">
          <p class="kicker">On the map</p>
          <h2 class="h3" id="mapName">{first["name"]}</h2>
          <p class="muted" id="mapAddr">{first["address"]}</p>
          <p class="muted" style="font-size:14.5px">Tap <b>Show on map</b> on any centre to see it here.</p>
        </div>
        {map_box(first["address"], "Map of the selected centre", "mapFrame")}
      </div>
      <nav class="jump" aria-label="Provinces">{jump}</nav>
{chr(10).join(groups)}
      <p class="muted" style="margin-top:24px">Is a centre missing or out of date? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </section>
</main>
'''


def centre_detail(c):
    def body(pre):
        evs = [x for x in EVENTS if x["centre"] == c["slug"]]
        cos = [x for x in COURSES if x["centre"] == c["slug"]]
        progs = "\n".join([event_card(x, pre) for x in evs] + [course_card(x, pre) for x in cos])
        prog_block = (f'''  <section class="section tight">
    <div class="wrap">
{sec_head("Programs", "At this centre")}
      <div class="cards">
{progs}
      </div>
    </div>
  </section>''' if progs else f'''  <section class="section tight">
    <div class="wrap">
      <div class="tile sky"><h2 class="h3">Programs at this centre</h2><p class="muted" style="margin-top:6px">A weekly gathering is held at every centre. Call {e(c["phone"])} for this centre's timings. <span class="tbd">TBD</span></p></div>
    </div>
  </section>''')
        site = (f'<li><b>Website</b><span><a href="{c["site"]}" target="_blank" rel="noopener">{c["site"].replace("https://", "")}</a></span></li>'
                if c["site"] else "")
        note = f' <span class="note">{c["note"]}</span>' if c["note"] else ""
        actions = (f'<a class="btn btn-gold" href="{pre}donate.html?centre={c["slug"]}">Donate</a>'
                   f'<a class="btn btn-ghost" href="{maps_search(c["address"])}" target="_blank" rel="noopener">Get directions</a>')
        if c["site"]:
            actions += f'<a class="btn btn-ghost" href="{c["site"]}" target="_blank" rel="noopener">Centre website</a>'
        return f'''<main id="main">
{page_head(c["name"] + note, c["address"], [("Centres", "centres.html"), (c["name"], "")], pre, actions, img(c["img"], pre))}
  <section class="section">
    <div class="wrap detail">
      <div class="tile prose">
        <p class="kicker">About this centre</p>
        <h2>{c["name"]}</h2>
        <p>{c["name"]} is a Dawat-e-Islami centre serving the Muslim community of {c["area"]}. It is a place for prayer, Islamic learning and spiritual gatherings, open to everyone.</p>
        <p>Like every Dawat-e-Islami centre, it holds a weekly spiritual gathering and offers Qur'an education for children and adults. Contact the centre for its current timings.</p>
      </div>
      <div class="side">
        <div class="tile">
          <h2 class="h3">Centre information</h2>
          <ul class="facts">
            <li><b>Address</b><span>{c["address"]}</span></li>
            <li><b>Phone</b><span>{phone_link(c["phone"])}</span></li>
            <li><b>Province</b><span>{c["province"]}</span></li>
            {site}
          </ul>
        </div>
      </div>
    </div>
  </section>
{prog_block}
  <section class="section tight">
    <div class="wrap detail">
      {map_box(c["address"], "Map of " + e(c["name"]))}
      <div class="tile navy" style="display:flex;flex-direction:column;gap:12px;justify-content:center">
        <p class="kicker">Support {c["city"]}</p>
        <h2 style="font-size:26px">Help keep this centre running</h2>
        <p style="color:var(--on-navy)">{c["need"]}. Every donation, large or small, helps.</p>
        <p><a class="btn btn-gold" href="{pre}donate.html?centre={c["slug"]}">Donate to this centre</a></p>
      </div>
    </div>
  </section>
</main>
'''
    return body


# ---------------------------------------------------------------- events + courses
def events_page(pre):
    evs = "\n".join(event_card(x, pre) for x in EVENTS)
    cos = "\n".join(course_card(x, pre) for x in COURSES)
    return f'''<main id="main">
{page_head("Events and classes", "Weekly gatherings, Friday prayers and classes at our centres across Canada.", [("Events &amp; Classes", "events.html")], pre,
           f'<a class="btn btn-ghost" href="#gatherings">Gatherings</a><a class="btn btn-ghost" href="#courses">Classes &amp; courses</a>')}
  <section class="section tight" id="announcements" hidden data-announce-wrap>
    <div class="wrap">
{sec_head("Coming up", "Announcements")}
      <div class="events" data-events></div>
    </div>
  </section>
  <section class="section" id="gatherings">
    <div class="wrap">
{sec_head("Every week", "Gatherings and Friday prayers", "Open to everyone. Timings can change, so please confirm with the centre.")}
      <div class="cards">
{evs}
      </div>
    </div>
  </section>
  <section class="section" id="courses">
    <div class="wrap">
{sec_head("Learn", "Classes and courses", "Call the number shown to register or ask about a class.")}
      <div class="cards">
{cos}
      </div>
    </div>
  </section>
</main>
'''


def event_detail(ev):
    def body(pre):
        c = CENTRE[ev["centre"]]
        ph = f'<li><b>Phone</b><span>{phone_link(ev["phone"])}</span></li>' if ev["phone"] else ""
        ln = f'<li><b>Length</b><span>{ev["length"]}</span></li>' if ev["length"] else ""
        sis = '<p><span class="sis">Separate arrangement for sisters</span></p>' if ev["sisters"] else ""
        return f'''<main id="main">
{page_head(ev["title"], f'Every {ev["day"]} · {ev["time"]}', [("Events", "events.html"), (ev["title"], "")], pre,
           f'<a class="btn btn-gold" href="{maps_search(ev["venue"])}" target="_blank" rel="noopener">Get directions</a><a class="btn btn-ghost" href="{pre}centres/{c["slug"]}.html">About the centre</a>',
           img(ev["img"], pre) if ev["img"] else "", poster=True)}
  <section class="section">
    <div class="wrap detail">
      <div class="tile prose">
        <p class="kicker">{ev["kind"]}</p>
        <h2>What to expect</h2>
        <p>{ev["desc"]}</p>
        {sis}
        <p>Everyone is welcome. Timings can change with the seasons, so please confirm with the centre before you travel.</p>
      </div>
      <div class="side">
        <div class="tile">
          <h2 class="h3">Details</h2>
          <ul class="facts">
            <li><b>When</b><span>Every {ev["day"]}, {ev["time"]}</span></li>
            {ln}
            <li><b>Where</b><span>{ev["venue"]}</span></li>
            {ph}
            <li><b>Centre</b><span><a href="{pre}centres/{c["slug"]}.html">{c["name"]}</a></span></li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</main>
'''
    return body


def course_detail(co):
    def body(pre):
        c = CENTRE[co["centre"]]
        rows = [("When", co["when"]), ("Length", co["length"]), ("Ages", co["ages"]), ("Teacher", co["teacher"]),
                ("Fee", co["fee"]), ("Where", co["venue"])]
        facts = "\n".join(f'            <li><b>{k}</b><span>{v}</span></li>' for k, v in rows if v)
        phones = " · ".join(phone_link(p) for p in co["phones"])
        first = co["phones"][0]
        call = f'<a class="btn btn-gold" href="tel:{tel(first)}">Call to register</a>' if first != "TBD" else ""
        return f'''<main id="main">
{page_head(co["title"], f'{co["city"]} · {co["when"]}', [("Classes", "events.html#courses"), (co["title"], "")], pre,
           call + f'<a class="btn btn-ghost" href="{pre}centres/{c["slug"]}.html">About the centre</a>',
           img(co["img"], pre) if co["img"] else "", poster=True)}
  <section class="section">
    <div class="wrap detail">
      <div class="tile prose">
        <p class="kicker">About this class</p>
        <h2>{co["title"]}</h2>
        <p>{co["desc"]}</p>
        <p>To register or ask a question, call {phones}.</p>
      </div>
      <div class="side">
        <div class="tile">
          <h2 class="h3">Details</h2>
          <ul class="facts">
{facts}
            <li><b>Phone</b><span>{phones}</span></li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</main>
'''
    return body


# ---------------------------------------------------------------- jamia
def jamia_page(pre):
    cards = []
    for j in JAMIAS:
        phones = " · ".join(phone_link(p) for p in j["phones"])
        site = f'<a href="{j["site"]}" target="_blank" rel="noopener">Website</a>' if j["site"] else ""
        cards.append(f'''        <article class="card">
          <div class="ic">{svg("jamia")}</div>
          <p class="city">{j["city"]}, {j["province"]}</p>
          <h3>{j["name"]}</h3>
          <p>{j["info"]}</p>
          <ul class="facts">
            <li><b>Address</b><span>{j["address"]}</span></li>
            <li><b>Phone</b><span>{phones}</span></li>
          </ul>
          <div class="card-links"><a href="{maps_search(j["address"])}" target="_blank" rel="noopener">Directions</a>{site}<a class="don" href="{pre}donate.html?purpose=jamia">Donate</a></div>
        </article>''')
    alim = next(x for x in COURSES if x["slug"] == "full-time-alim-course-montreal")
    return f'''<main id="main">
{page_head("Jamia-tul-Madina", "Dawat-e-Islami's Islamic university, training the next generation of scholars in Canada.", [("Jamia-tul-Madina", "jamia.html")], pre,
           f'<a class="btn btn-gold" href="{JAMIA_SITE}" target="_blank" rel="noopener">Visit jamiatulmadina.ca</a><a class="btn btn-ghost" href="{pre}courses/{alim["slug"]}.html">The Aalim course</a>')}
  <section class="section">
    <div class="wrap split">
      <div class="tile prose">
        <p class="kicker">About the Jamia</p>
        <h2>Free scholarly training</h2>
        <p>Jamia-tul-Madina is Dawat-e-Islami's network of Islamic universities, with more than 1,500 branches worldwide. Students study the traditional Dars-e-Nizami (Aalim) course: Qur'an, Hadith, Islamic law, Arabic and the other Islamic sciences.</p>
        <p>In Canada, the Jamia runs a full-time Aalim course in Montreal, free of charge for accepted students, and is opening a new permanent campus in Cornwall, Ontario.</p>
      </div>
      <div class="tile navy" style="display:flex;flex-direction:column;justify-content:center;gap:12px">
        <p class="kicker">Support a student</p>
        <h2 style="font-size:26px">Help train the scholars of tomorrow</h2>
        <p style="color:var(--on-navy)">Education at Jamia-tul-Madina is free. Your donations cover teachers, books and the running of the campuses.</p>
        <p><a class="btn btn-gold" href="{pre}donate.html?purpose=jamia">Donate to the Jamia</a></p>
      </div>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap">
{sec_head("Campuses", "Jamia-tul-Madina in Canada")}
      <div class="cards three">
{chr(10).join(cards)}
      </div>
    </div>
  </section>
</main>
'''


# ---------------------------------------------------------------- pillars
def pillar_page(p):
    slug, ar, en, num, eng, short, sections = p

    def body(pre):
        secs = "\n".join(f'        <h2>{h}</h2>\n        <p>{t}</p>' for h, t in sections)
        others = "\n".join(
            f'''        <a class="pillar" href="{pre}islam/{s}.html"{' aria-current="page"' if s == slug else ""}><span class="arabic" lang="ar">{a}</span><small>{n} pillar</small><h3>{x}</h3></a>'''
            for s, a, x, n, *_ in PILLARS)
        return f'''<main id="main">
{page_head(f"{en} ({eng})", short, [("Discover Islam", "index.html#pillars"), (en, "")], pre)}
  <section class="section">
    <div class="wrap detail">
      <div class="tile prose">
{secs}
      </div>
      <div class="side">
        <div class="tile cream" style="text-align:center">
          <p class="arabic" lang="ar" style="font-size:54px;color:var(--navy);line-height:1.4">{ar}</p>
          <ul class="facts" style="text-align:left">
            <li><b>Pillar</b><span>{num} of five</span></li>
            <li><b>Meaning</b><span>{eng}</span></li>
          </ul>
        </div>
        <div class="tile">
          <h2 class="h3">Have a question?</h2>
          <p>Ask a qualified mufti at Darul Ifta Ahl-e-Sunnat.</p>
          <p style="margin-top:10px"><a class="link" href="https://www.fatwaqa.com/en" target="_blank" rel="noopener">Ask a question →</a></p>
        </div>
      </div>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap">
{sec_head("Discover Islam", "The five pillars")}
      <div class="pillars">
{others}
      </div>
    </div>
  </section>
</main>
'''
    return body


# ---------------------------------------------------------------- donate
def donate_page(pre):
    purposes = "\n".join(
        f'''          <label class="opt"><input type="radio" name="purpose" value="{k}" data-label="{e(n)}"{" checked" if i == 0 else ""}><span>{n}</span></label>'''
        for i, (k, n, _) in enumerate(DONATION_PURPOSES))
    centre_opts = "\n".join(f'            <option value="{c["slug"]}">{c["name"]} ({c["city"]})</option>' for c in CENTRES)
    amounts = "\n".join(
        f'''          <label class="opt"><input type="radio" name="amount" value="{a}"{" checked" if a == 100 else ""}><span>${a}</span></label>'''
        for a in DONATION_AMOUNTS)
    online = (f'data-url="{e(DONATE_URL)}"' if DONATE_URL else "")
    status = ("" if DONATE_URL else
              '<p class="muted" style="font-size:14.5px">Online card payments are being set up <span class="tbd">TBD</span>. Until then, please give by Interac e-Transfer or at any centre.</p>')
    return f'''<main id="main">
{page_head("Donate", "Give your Zakat, Fitrana, Sadaqah and donations to Dawat-e-Islami Canada, a registered Canadian charity.", [("Donate", "donate.html")], pre)}
  <section class="section">
    <div class="wrap donate-grid">
      <form class="tile dform" id="donateForm" {online} novalidate>
        <fieldset>
          <legend>1. What is your donation for?</legend>
          <div class="opts">
{purposes}
          </div>
        </fieldset>
        <div class="field">
          <label for="d_centre"><b>2. Which centre should it support?</b></label>
          <select id="d_centre" name="centre">
            <option value="">Where it is needed most</option>
{centre_opts}
          </select>
        </div>
        <fieldset>
          <legend>3. Amount (CAD)</legend>
          <div class="opts amounts">
{amounts}
            <label class="opt"><input type="radio" name="amount" value="other"><span>Other</span></label>
          </div>
          <div class="field" id="d_other_wrap" hidden style="margin-top:10px">
            <label for="d_other">Other amount</label>
            <input id="d_other" type="number" inputmode="decimal" min="1" step="1" placeholder="$">
          </div>
        </fieldset>
        <fieldset>
          <legend>4. How often?</legend>
          <div class="opts">
            <label class="opt"><input type="radio" name="freq" value="once" checked><span>One time</span></label>
            <label class="opt"><input type="radio" name="freq" value="monthly"><span>Monthly</span></label>
          </div>
        </fieldset>
        <p class="summary" id="d_summary" aria-live="polite">You are giving <b>$100</b> one time for <b>General donation</b>.</p>
        <p class="form-err" id="d_err" role="alert"></p>
        <button class="btn btn-gold wide" type="submit">Donate now</button>
        {status}
        <div class="trust"><span>Secure donation</span><span>Tax receipt available</span><span>Registered charity · BN {BN}</span></div>
      </form>
      <aside class="side">
        <div class="tile" id="etransfer">
          <h2 class="h3">Interac e-Transfer</h2>
          <p>For Faizan-e-Madina Masjid, Surrey. Send to the email for your type of donation, and include your full name and mailing address in the message for a tax receipt.</p>
{etransfer_list()}
        </div>
        <div class="tile sky">
          <h2 class="h3">In person</h2>
          <p>You can donate at any of our centres after prayers.</p>
          <p style="margin-top:8px"><a class="link" href="{pre}centres.html">Find a centre →</a></p>
        </div>
        <div class="tile cream">
          <h2 class="h3">Need a tax receipt?</h2>
          <p>Official receipts are issued for eligible donations.</p>
          <p style="margin-top:12px"><a class="btn btn-navy" href="{pre}receipt.html">Request a receipt</a></p>
        </div>
      </aside>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap">
{sec_head("Where your donation goes", "Ways to give")}
      <div class="cards">
{chr(10).join(f'        <div class="card"><h3>{n}</h3><p>{t}</p></div>' for _, n, t in DONATION_PURPOSES)}
      </div>
    </div>
  </section>
</main>
'''


def gform_attr(cfg):
    return f"data-gform='{e(json.dumps(cfg))}'" if cfg else ""


def receipt_page(pre):
    centre_opts = "\n".join(f'            <option>{c["name"]} ({c["city"]})</option>' for c in CENTRES)
    purposes = "\n".join(
        f'            <label class="opt"><input type="checkbox" name="purpose" value="{p}"><span>{p}</span></label>'
        for p in ["General donation", "Zakat", "Fitrana", "Sadaqah"])
    return f'''<main id="main">
{page_head("Donation receipt", "Request an official tax receipt for your donation to Dawat-e-Islami Canada.", [("Donate", "donate.html"), ("Donation receipt", "")], pre)}
  <section class="section tight">
    <div class="wrap">
      <ol class="steps">
        <li><b>Send your details</b><span>Donation date, amount and your mailing address.</span></li>
        <li><b>We check your donation</b><span>Your request stays pending until our team confirms it.</span></li>
        <li><b>Receive your receipt</b><span>Your official receipt is emailed once it is issued.</span></li>
      </ol>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap donate-grid">
      <form class="tile dform gform" id="receiptForm" {gform_attr(RECEIPT_GFORM)} novalidate>
        <h2 style="font-size:24px">Your details</h2>
        <div class="row2">
          <div class="field"><label for="r_name">Full name</label><input id="r_name" type="text" name="name" autocomplete="name" required><small>As it should appear on the receipt.</small></div>
          <div class="field"><label for="r_email">Email</label><input id="r_email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="r_address">Mailing address</label><textarea id="r_address" name="address" autocomplete="street-address" required style="min-height:90px"></textarea></div>
        <h2 style="font-size:24px">Your donation</h2>
        <div class="field">
          <label for="r_centre">Dawat-e-Islami centre</label>
          <select id="r_centre" name="centre" required>
            <option value="">Select a centre</option>
{centre_opts}
          </select>
        </div>
        <div class="row2">
          <div class="field"><label for="r_date">Date of donation</label><input id="r_date" name="date" type="date" required></div>
          <div class="field"><label for="r_amount">Eligible amount (CAD)</label><input id="r_amount" name="amount" type="number" inputmode="decimal" min="1" step="0.01" required></div>
        </div>
        <fieldset>
          <legend>Donation purpose (select all that apply)</legend>
          <div class="checks opts">
{purposes}
          </div>
        </fieldset>
        <label class="hp" aria-hidden="true">Leave empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label>
        <p class="form-err" role="alert"></p>
        <button class="btn btn-navy wide" type="submit">Send request</button>
        <p class="done" hidden>Thank you. Your request has been sent. We will email your receipt once it has been issued.</p>
      </form>
      <aside class="side">
        <div class="tile sky">
          <h2 class="h3">Good to know</h2>
          <p>Nafl donations are used by Dawat-e-Islami for every good and lawful purpose where appropriate.</p>
          <p style="margin-top:8px">Questions? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>
        <div class="trust"><span>Secure submission</span><span>Receipt by email</span><span>CRA-eligible amounts</span></div>
      </aside>
    </div>
  </section>
</main>
'''


# ---------------------------------------------------------------- contact
def contact_page(pre):
    groups = []
    for prov in dict.fromkeys(c["province"] for c in CENTRES):
        seen, rows = set(), []
        for c in CENTRES:
            if c["province"] == prov and (c["city"], c["phone"]) not in seen:
                seen.add((c["city"], c["phone"]))
                rows.append(f'<li><span>{c["city"]}</span>{phone_link(c["phone"])}</li>')
        groups.append(f'''        <div class="tile"><h2 class="h3">{prov}</h2><ul>{"".join(rows)}</ul></div>''')
    return f'''<main id="main">
{page_head("Contact us", "Questions about events, classes, donations or a centre? We would love to hear from you.", [("Contact", "contact.html")], pre)}
  <section class="section">
    <div class="wrap donate-grid">
      <form class="tile dform gform" id="contactForm" {gform_attr(CONTACT_GFORM)} novalidate>
        <h2 style="font-size:24px">Send us a message</h2>
        <div class="row2">
          <div class="field"><label for="c_name">Full name</label><input id="c_name" type="text" name="name" autocomplete="name" required></div>
          <div class="field"><label for="c_email">Email</label><input id="c_email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="c_phone">Phone (optional)</label><input id="c_phone" name="phone" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="c_msg">Your message</label><textarea id="c_msg" name="message" required></textarea><small>For a question about a centre, please mention your city.</small></div>
        <label class="hp" aria-hidden="true">Leave empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label>
        <p class="form-err" role="alert"></p>
        <button class="btn btn-navy wide" type="submit">Send message</button>
        <p class="done" hidden>Thank you for your message. A member of our team will reply within 1 to 2 business days.</p>
      </form>
      <aside class="side">
        <div class="tile">
          <h2 class="h3">Email</h2>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div class="tile">
          <h2 class="h3">Registered office</h2>
          <p>{OFFICE}</p>
        </div>
        <div class="tile sky">
          <h2 class="h3">Volunteer with us</h2>
          <p>General questions, volunteering and local centre enquiries are all welcome. We usually reply within 1 to 2 business days.</p>
        </div>
      </aside>
    </div>
  </section>
  <section class="section tight">
    <div class="wrap">
{sec_head("By province", "Phone numbers", "Call the number for your area.", (pre + "centres.html", "All centres"))}
      <div class="contact-grid">
{chr(10).join(groups)}
      </div>
    </div>
  </section>
</main>
'''


def privacy_page(pre):
    return f'''<main id="main">
{page_head("Privacy policy", "How this website handles your information", [("Privacy policy", "")], pre)}
  <section class="section">
    <div class="wrap"><div class="tile prose" style="max-width:820px">
      <p class="muted">Last updated: October 2026. <span class="tbd">TBD</span> Draft, to be reviewed by management.</p>
      <h2>What we collect</h2>
      <p>This website does not ask you to create an account and does not use advertising or tracking cookies. We may use privacy-friendly visitor statistics (such as Cloudflare Web Analytics) that count page visits without identifying you.</p>
      <h2>Forms</h2>
      <p>When you send a message or request a donation receipt, we use your details only to reply to you or to issue your receipt. We do not sell or share them.</p>
      <h2>Donations</h2>
      <p>Online donations are processed by a third-party payment provider, and Interac e-Transfers by your bank. Their privacy policies apply. We keep the name and address you give us only to issue tax receipts and to meet the Canada Revenue Agency's record-keeping requirements.</p>
      <h2>Links to other websites</h2>
      <p>This site links to other Dawat-e-Islami websites, YouTube and map services, which have their own privacy policies.</p>
      <h2>Questions</h2>
      <p>For any privacy question, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div></div>
  </section>
</main>
'''


def terms_page(pre):
    return f'''<main id="main">
{page_head("Terms of use", "Using this website", [("Terms of use", "")], pre)}
  <section class="section">
    <div class="wrap"><div class="tile prose" style="max-width:820px">
      <p class="muted">Last updated: October 2026. <span class="tbd">TBD</span> Draft, to be reviewed by management.</p>
      <h2>About this website</h2>
      <p>This website is run by Dawat-e-Islami Canada, a registered Canadian charity (BN {BN}), to share information about our centres, programs and events.</p>
      <h2>Accuracy</h2>
      <p>We try to keep all information, including timings and addresses, accurate and up to date. Timings can change, so please confirm with the centre before travelling.</p>
      <h2>Content</h2>
      <p>The text, images and logos on this site belong to Dawat-e-Islami or are used with permission. Please do not reuse them without permission.</p>
      <h2>External links</h2>
      <p>We are not responsible for the content of other websites we link to.</p>
      <h2>Contact</h2>
      <p>Questions about these terms can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div></div>
  </section>
</main>
'''


def not_found(pre):
    return f'''<main id="main">
{page_head("Page not found", "The page you are looking for has moved or does not exist.", [("Not found", "")], pre,
           f'<a class="btn btn-gold" href="{pre}index.html">Go to the home page</a><a class="btn btn-ghost" href="{pre}centres.html">Find a centre</a>')}
</main>
'''


# ---------------------------------------------------------------- write everything
T = " | Dawat-e-Islami Canada"
write("index.html", "Dawat-e-Islami Canada", "Dawat-e-Islami Canada: masajid, Qur'an classes, weekly gatherings and community programs across Canada.", home)
write("about.html", "About" + T, "About Dawat-e-Islami, its founder Ameer-e-Ahl-e-Sunnat, and its work in Canada.", about, "about.html")
write("departments.html", "Departments" + T, "The departments of Dawat-e-Islami Canada: Madrasa-tul-Madina, Jamia-tul-Madina, Islamic school and more.", departments_page, "departments.html")
for d in DEPARTMENTS:
    if d[4]:
        write(f"departments/{d[0]}.html", d[2] + T, d[3], dept_detail(d), "departments.html")
write("centres.html", "Centres" + T, "Dawat-e-Islami centres across Canada, with addresses, phone numbers and directions.", centres_page, "centres.html")
for c in CENTRES:
    write(f"centres/{c['slug']}.html", c["name"] + T, f'{c["name"]}, {c["address"]}. Prayers, weekly gatherings and classes.', centre_detail(c), "centres.html")
write("events.html", "Events and classes" + T, "Weekly gatherings, Friday prayers and classes at Dawat-e-Islami centres across Canada.", events_page, "events.html")
for ev in EVENTS:
    write(f"events/{ev['slug']}.html", ev["title"] + T, f'{ev["title"]}: every {ev["day"]}, {ev["time"]}.', event_detail(ev), "events.html")
for co in COURSES:
    write(f"courses/{co['slug']}.html", co["title"] + ", " + co["city"] + T, f'{co["title"]} in {co["city"]}: {co["when"]}.', course_detail(co), "events.html")
write("jamia.html", "Jamia-tul-Madina" + T, "Jamia-tul-Madina, Dawat-e-Islami's Islamic university in Canada: Montreal and Cornwall.", jamia_page, "jamia.html")
for p in PILLARS:
    write(f"islam/{p[0]}.html", f"{p[2]} ({p[4]})" + T, p[5], pillar_page(p))
write("donate.html", "Donate" + T, "Donate Zakat, Fitrana, Sadaqah and more to Dawat-e-Islami Canada, a registered Canadian charity.", donate_page, "donate.html")
write("receipt.html", "Donation receipt" + T, "Request an official tax receipt for your donation to Dawat-e-Islami Canada.", receipt_page, "donate.html")
write("contact.html", "Contact" + T, "Contact Dawat-e-Islami Canada by message, email or phone.", contact_page, "contact.html")
write("privacy.html", "Privacy policy" + T, "Privacy policy of the Dawat-e-Islami Canada website.", privacy_page)
write("terms.html", "Terms of use" + T, "Terms of use of the Dawat-e-Islami Canada website.", terms_page)
write("404.html", "Page not found" + T, "This page could not be found.", not_found)
# The 404 page is shown at whatever address was mistyped, so give it a <base> that points at the site root
_p = ROOT / "404.html"
_p.write_text(_p.read_text().replace('<meta charset="utf-8">', """<meta charset="utf-8">
<script>(function(){var b="/";if(/github\\.io$/.test(location.hostname)){var s=location.pathname.split("/")[1];if(s)b="/"+s+"/";}document.write('<base href="'+b+'">');})()</script>""", 1))

# Old addresses that moved
MOVED = {"vancouver.html": VANCOUVER_SITE, "prayer-times.html": VANCOUVER_SITE, "services.html": "departments.html"}
for old, new in MOVED.items():
    (ROOT / old).write_text(f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Moved | Dawat-e-Islami Canada</title>
<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={new}">
<link rel="canonical" href="{new}"></head>
<body><p>This page has moved to <a href="{new}">{new}</a>.</p></body></html>
''')

# Hosting files (Cloudflare Pages reads _redirects and _headers)
(ROOT / "_redirects").write_text(f"""/vancouver {VANCOUVER_SITE} 301
/vancouver.html {VANCOUVER_SITE} 301
/prayer-times {VANCOUVER_SITE} 301
/prayer-times.html {VANCOUVER_SITE} 301
/services /departments 301
/services.html /departments 301
""")
(ROOT / "_headers").write_text("""/assets/*
  Cache-Control: public, max-age=604800
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=()
""")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = "\n".join(
    f"  <url><loc>{SITE}/{'' if n == 'index.html' else n.replace('.html', '')}</loc></url>"
    for n in WRITTEN if n != "404.html")
(ROOT / "sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')

# List of outside pictures, for the "Download pictures" GitHub Action
EXT.mkdir(parents=True, exist_ok=True)
(EXT / "sources.txt").write_text("\n".join(sorted(REMOTE)) + "\n")

print("built", len(WRITTEN), "pages, version", V, "| outside pictures:", len(REMOTE),
      "| downloaded:", sum((EXT / local_name(u)).exists() for u in REMOTE))
