"""All the words and lists on the site. Edit this file to change content, then run: python3 build.py

Anything written as "TBD" shows on the site as a yellow TBD label until it is filled in.
Images: paste the full https:// address of the picture. build.py automatically uses a local copy
from assets/img/ext/ when one has been downloaded (see README).
"""

SITE = "https://dawateislami.ca"
BN = "81933 5662 RR0001"
EMAIL = "canada@dawateislami.net"
OFFICE = "120 - 32 Westwinds Cres NE, Calgary, AB T3J 5L3"
VANCOUVER_SITE = "https://dawateislamivancouver.ca"
JAMIA_SITE = "https://jamiatulmadina.ca/"
LIVE_URL = "https://www.youtube.com/@MadaniChannelEnglishLive/live"

R2 = "https://pub-6e79549afc524bbd9a283071a4b99ca1.r2.dev/media"
UK = "https://dawateislami.co.uk/admin/assets/uploads"

# ---- Online forms and donations --------------------------------------------------------------
# DONATE_URL: the online donation page (for example a Zeffy or CanadaHelps form). Empty = TBC.
DONATE_URL = ""
# Google Forms that receive the receipt-request and contact forms. Empty = form shows
# "not connected yet". Format: {"action": ".../formResponse", "field": "entry id", ...}
RECEIPT_GFORM = {}
CONTACT_GFORM = {}

SOCIAL = {  # name: url (empty = hidden)
    "YouTube": "",
    "Facebook": "",
    "Instagram": "",
    "TikTok": "",
    "X": "",
}

# ---- Home page -------------------------------------------------------------------------------
HERO_SLIDES = [
    (f"{R2}/hero/reform-myself.png", "I must strive to reform myself and the people of the entire world"),
    (f"{R2}/hero/centres-across-canada.png", "Dawat-e-Islami centres across Canada"),
    (f"{R2}/hero/helping-palestinians.png", "Helping Palestinians"),
]
FOUNDER_IMG = f"{UK}/about-us/1_founder_2044233964.jpeg"
APPEAL_IMG = f"{UK}/campaign/382144462964_campaign.jpeg"

# ---- Centres ---------------------------------------------------------------------------------
# slug: the web address of the centre page (centres/<slug>.html)
# site: the centre's own website, if it has one. note: shown in orange (e.g. "Under construction")
CENTRES = [
    {"slug": "faizan-e-madina-surrey", "province": "British Columbia", "city": "Surrey",
     "area": "Vancouver area", "name": "Faizan-e-Madina Masjid",
     "address": "7062 134 St, Surrey, BC V3W 4T2", "phone": "+1 (778) 895-0886", "site": VANCOUVER_SITE,
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-madina-masjid-surrey.jpg"},
    {"slug": "faizan-e-madina-calgary", "province": "Alberta", "city": "Calgary", "area": "northeast Calgary",
     "name": "Faizan-e-Madina Calgary",
     "address": "32 Westwinds Crescent NE, Calgary, AB T3J 5H2", "phone": "+1 (403) 618-5408", "site": "",
     "note": "", "need": "Daily operations, utilities and programs", "img": f"{R2}/projects/images/faizan-e-madina-calgary.jpg"},
    {"slug": "faizan-e-makkah-calgary", "province": "Alberta", "city": "Calgary", "area": "northeast Calgary",
     "name": "Faizan-e-Makkah Calgary",
     "address": "Unit 5000, 4250 109 Ave NE, Calgary, AB T3N 1Z3", "phone": "+1 (403) 618-5408", "site": "",
     "note": "", "need": "Monthly running costs of about $2,000", "img": f"{R2}/projects/images/faizan-e-makkah-calgary.jpg"},
    {"slug": "faizan-e-madina-edmonton", "province": "Alberta", "city": "Edmonton", "area": "Edmonton",
     "name": "Faizan-e-Madina Edmonton",
     "address": "11809 96 St, Edmonton, AB T5G 1V4", "phone": "+1 (780) 729-6492", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-madina-edmonton.jpg"},
    {"slug": "faizan-e-madina-regina", "province": "Saskatchewan", "city": "Regina", "area": "Regina",
     "name": "Faizan-e-Madina Islamic Center Regina",
     "address": "1169 Athol St, Regina, SK S4T 3C3", "phone": "+1 (438) 401-0782", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-madina-islamic-center-regina.jpg"},
    {"slug": "faizan-e-madina-winnipeg", "province": "Manitoba", "city": "Winnipeg", "area": "Winnipeg",
     "name": "Faizan-e-Madina Islamic Centre Winnipeg",
     "address": "585 St Anne's Rd, Winnipeg, MB R2M 5R5", "phone": "+1 (204) 998-1979", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-madina-islamic-centre-winnipeg.jpg"},
    {"slug": "faizan-e-makkah-winnipeg", "province": "Manitoba", "city": "Winnipeg", "area": "Winnipeg",
     "name": "Faizan-e-Makkah Winnipeg",
     "address": "509 Trans-Canada Hwy, Winnipeg, MB R2M 3L2", "phone": "+1 (204) 998-1979", "site": "",
     "note": "Under construction", "need": "Building fund", "img": f"{R2}/projects/images/faizan-e-makkah-winnipeg.jpg"},
    {"slug": "faizan-e-attar-thorncliffe", "province": "Ontario", "city": "East York", "area": "Thorncliffe Park, Toronto",
     "name": "Faizan-e-Attar Thorncliffe",
     "address": "49 Thorncliffe Park Dr, Unit 120, East York, ON M4H 1J6", "phone": "+1 (647) 366-3786", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-attar-thorncliffe_bPZ5oAo.jpg"},
    {"slug": "faizan-e-madina-etobicoke", "province": "Ontario", "city": "Etobicoke", "area": "Etobicoke, Toronto",
     "name": "Faizan-e-Madina Etobicoke",
     "address": "595 Albion Rd, Etobicoke, ON M9V 1A1", "phone": "+1 (647) 366-3786", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-madina-etobicoke.jpg"},
    {"slug": "faizan-e-madina-hamilton", "province": "Ontario", "city": "Hamilton", "area": "Hamilton",
     "name": "Faizan-e-Madina Hamilton",
     "address": "1202 Dunsmure Rd, Hamilton, ON L8H 1L4", "phone": "+1 (647) 366-3786", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-madina-hamilton.jpg"},
    {"slug": "faizan-e-madina-ottawa", "province": "Ontario", "city": "Ottawa", "area": "Ottawa",
     "name": "Faizan-e-Madina Islamic Center Ottawa",
     "address": "415 McArthur Ave, Ottawa, ON K1K 1G5", "phone": "+1 (514) 983-7861", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/faizan-e-madina-islamic-center-ottawa.jpg"},
    {"slug": "faizan-e-madina-montreal", "province": "Quebec", "city": "Montreal", "area": "Parc-Extension, Montreal",
     "name": "Faizan-e-Madina Montreal",
     "address": "810 Rue Saint-Roch, Montréal, QC H3N 1L4", "phone": "+1 (514) 983-7861", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/WhatsApp_Image_2026-07-24_at_21.39.34_Goi3BxW.jpeg"},
    {"slug": "faizan-e-hub-e-rasool-montreal", "province": "Quebec", "city": "Montreal", "area": "Montreal",
     "name": "Faizan-e-Hub-e-Rasool Montreal",
     "address": "1008 Rue Jean-Talon O, Montréal, QC H3N 1T1", "phone": "+1 (514) 983-7861", "site": "",
     "note": "", "need": "Monthly running expenses", "img": f"{R2}/projects/images/WhatsApp_Image_2026-07-24_at_21.39.34.jpeg"},
]

# ---- Jamia-tul-Madina (Islamic university) ---------------------------------------------------
JAMIAS = [
    {"slug": "montreal", "province": "Quebec", "city": "Montreal", "name": "Jamia-tul-Madina Montreal",
     "address": "810 Rue Saint-Roch, Montréal, QC H3N 1L4",
     "phones": ["+1 (514) 983-7861", "+1 (438) 833-1906", "+1 (514) 880-2025"], "site": "",
     "info": "Full-time Aalim course (Dars-e-Nizami), 5 to 8 years. Brothers only. Free for accepted students."},
    {"slug": "cornwall", "province": "Ontario", "city": "Cornwall", "name": "Jamia-tul-Madina Cornwall",
     "address": "500 York St, Cornwall, ON", "phones": ["TBD"], "site": JAMIA_SITE,
     "info": "Dawat-e-Islami Canada's new permanent Jamia-tul-Madina campus."},
]

# ---- Weekly gatherings and Friday prayers -----------------------------------------------------
# centre: the slug of the centre it belongs to. img: optional picture.
EVENTS = [
    {"slug": "surrey-weekly-ijtima", "kind": "Weekly Ijtima", "title": "Weekly Ijtima, Surrey", "centre": "faizan-e-madina-surrey",
     "day": "Thursday", "time": "7:00 PM", "length": "", "venue": "Faizan-e-Madina Masjid, 7062 134 St, Surrey, BC",
     "phone": "+1 (778) 895-0886", "sisters": True, "img": "",
     "desc": "Tilawat, naat, bayan, zikr, dua and salam, followed by dinner. A separate arrangement is made for sisters."},
    {"slug": "friday-prayer-surrey", "kind": "Friday prayer", "title": "Jumu'ah, Surrey", "centre": "faizan-e-madina-surrey",
     "day": "Friday", "time": "1:30 PM and 3:30 PM", "length": "", "venue": "Faizan-e-Madina Masjid, 7062 134 St, Surrey, BC",
     "phone": "", "sisters": False, "img": "",
     "desc": "Two Jumu'ah congregations: the first Jama'at at 1:30 PM and the second at 3:30 PM."},
    {"slug": "calgary-weekly-ijtima", "kind": "Weekly Ijtima", "title": "Sunnah-Inspired Ijtima, Calgary", "centre": "faizan-e-makkah-calgary",
     "day": "Thursday", "time": "7:30 PM", "length": "About 1 hour", "venue": "Faizan-e-Makkah, Unit 5000, 4250 109 Ave NE, Calgary, AB",
     "phone": "+1 (403) 618-5408", "sisters": False, "img": f"{R2}/events/images/calgary-weekly-ijtima.png",
     "desc": "A weekly gathering with recitation of the Qur'an, naat, a talk on faith and community, collective zikr and a closing dua."},
    {"slug": "regina-weekly-ijtima", "kind": "Weekly Ijtima", "title": "Weekly Ijtima, Regina", "centre": "faizan-e-madina-regina",
     "day": "Thursday", "time": "After Maghrib", "length": "", "venue": "Faizan-e-Madina Regina, 1169 Athol St, Regina, SK",
     "phone": "+1 (306) 201-8556", "sisters": False, "img": "",
     "desc": "A weekly spiritual gathering for the community, with food served afterwards."},
    {"slug": "winnipeg-weekly-ijtima", "kind": "Weekly Ijtima", "title": "Sunnah-Inspired Ijtima, Winnipeg", "centre": "faizan-e-makkah-winnipeg",
     "day": "Thursday", "time": "7:00 PM", "length": "About 1 hour", "venue": "Faizan-e-Makkah, 509 St Mary's Rd, Winnipeg, MB",
     "phone": "+1 (204) 998-1979", "sisters": True, "img": "",
     "desc": "A weekly gathering with recitation, naat, a talk, zikr and dua. A separate arrangement is made for sisters."},
    {"slug": "friday-prayer-winnipeg", "kind": "Friday prayer", "title": "Jumu'ah, Winnipeg", "centre": "faizan-e-makkah-winnipeg",
     "day": "Friday", "time": "2:00 PM and 3:00 PM", "length": "", "venue": "Faizan-e-Makkah, 509 St Mary's Rd, Winnipeg, MB",
     "phone": "", "sisters": True, "img": "",
     "desc": "Two Jumu'ah congregations: the first Jama'at at 2:00 PM and the second at 3:00 PM. A separate arrangement is made for sisters."},
    {"slug": "friday-prayer-ottawa", "kind": "Friday prayer", "title": "Jumu'ah, Ottawa", "centre": "faizan-e-madina-ottawa",
     "day": "Friday", "time": "1:30 PM and 2:30 PM", "length": "", "venue": "415 McArthur Ave, Ottawa, ON K1K 1G5",
     "phone": "", "sisters": False, "img": "",
     "desc": "Two Jumu'ah congregations: 1:30 PM and 2:30 PM (summer schedule). The speech begins 30 minutes before each Jama'at."},
    {"slug": "montreal-weekly-ijtima", "kind": "Weekly Ijtima", "title": "Weekly Ijtima, Montreal", "centre": "faizan-e-madina-montreal",
     "day": "Saturday", "time": "After Isha", "length": "", "venue": "Faizan-e-Madina Montreal, 810 Rue Saint-Roch, Montréal, QC",
     "phone": "+1 (438) 833-1906", "sisters": False, "img": "",
     "desc": "A weekly family gathering with recitation of the Qur'an, naat, a talk and zikr."},
]

# ---- Classes and courses ----------------------------------------------------------------------
COURSES = [
    {"slug": "quran-unlocked-calgary", "title": "Qur'an Unlocked", "city": "Calgary", "centre": "faizan-e-madina-calgary",
     "when": "Saturdays, 7:15 PM", "length": "1 hour", "ages": "12+", "teacher": "Imam Hassan Raza", "fee": "",
     "venue": "Calgary", "phones": ["+1 (825) 561-9192"], "img": f"{R2}/courses/images/WhatsApp_Image_2026-06-09_at_15.24.07.jpeg",
     "desc": "A weekly class on the meanings of the Qur'an, the sciences that help us understand it, and practical lessons for daily life. For beginners and advanced learners."},
    {"slug": "kids-quran-classes-regina", "title": "Kids Qur'an Classes", "city": "Regina", "centre": "faizan-e-madina-regina",
     "when": "Monday to Thursday, 7:00 PM", "length": "2 hours", "ages": "4 to 7", "teacher": "", "fee": "",
     "venue": "Faizan-e-Madina, 1169 Athol St, Regina, SK S4T 3C3", "phones": ["+1 (639) 563-7860"],
     "img": f"{R2}/courses/images/kids-quran-classes-regina.png",
     "desc": "Qur'an reading, basic Islamic teachings, duas and Sunnahs, and good manners for boys and girls. Spaces are limited."},
    {"slug": "hifz-quran-classes-surrey", "title": "Free Hifz Qur'an Classes", "city": "Surrey", "centre": "faizan-e-madina-surrey",
     "when": "Monday to Thursday, 7:00 PM", "length": "1 hour", "ages": "", "teacher": "", "fee": "Free",
     "venue": "Faizan-e-Madina Islamic Center, 7062 134 St, Surrey, BC", "phones": ["+1 (778) 551-6986", "+1 (778) 895-0886"],
     "img": f"{R2}/courses/images/hifz-quran-classes-surrey.png",
     "desc": "Free classes to memorise the Holy Qur'an, for committed students."},
    {"slug": "madrasa-adults-surrey", "title": "Madrasa-tul-Madina for Adults", "city": "Surrey", "centre": "faizan-e-madina-surrey",
     "when": "Every day, 7:00 PM", "length": "1 hour", "ages": "18+", "teacher": "", "fee": "",
     "venue": "Faizan-e-Madina, 7062 134 St, Surrey, BC", "phones": ["+1 (778) 551-6986", "+1 (778) 895-0886"], "img": "",
     "desc": "Learn to read the Qur'an correctly, with tajweed, at your own pace, whatever your starting point."},
    {"slug": "sunday-islamic-school-surrey", "title": "Sunday Islamic School", "city": "Surrey", "centre": "faizan-e-madina-surrey",
     "when": "Sundays, 11:00 AM", "length": "2.5 hours", "ages": "6 to 14", "teacher": "", "fee": "$50 per month",
     "venue": "Faizan-e-Madina, 7062 134 St, Surrey, BC", "phones": ["+1 (778) 251-0786", "+1 (613) 981-5181"], "img": "",
     "desc": "Faith, prayer, Qur'an and Islamic character for children who attend public school during the week."},
    {"slug": "youth-islamic-classes-toronto", "title": "Weekly Youth Islamic Classes", "city": "Toronto", "centre": "faizan-e-attar-thorncliffe",
     "when": "Fridays, 6:30 PM", "length": "1 hour", "ages": "Youth", "teacher": "", "fee": "",
     "venue": "Musallah Faizan-e-Attar, 120-49 Thorncliffe Park Dr, Toronto, ON M4H 1J6", "phones": ["+1 (647) 313-1786"], "img": "",
     "desc": "Weekly Islamic classes for young people in Thorncliffe Park."},
    {"slug": "daily-tafsir-halaqah-ottawa", "title": "Daily Tafsir Halaqah", "city": "Ottawa", "centre": "faizan-e-madina-ottawa",
     "when": "Every day", "length": "30 minutes", "ages": "", "teacher": "", "fee": "",
     "venue": "415 McArthur Ave, Ottawa, ON K1K 1G5", "phones": ["+1 (613) 316-5030"],
     "img": f"{R2}/courses/images/daily-tafsir-halaqah-ottawa.png",
     "desc": "A short daily study circle on the explanation (tafsir) of the Holy Qur'an."},
    {"slug": "full-time-alim-course-montreal", "title": "Full-Time Aalim Course", "city": "Montreal", "centre": "faizan-e-madina-montreal",
     "when": "Every day", "length": "5 to 8 years", "ages": "Brothers only", "teacher": "", "fee": "Free for accepted students",
     "venue": "Jamia-tul-Madina, 810 Rue Saint-Roch, Montréal, QC H3N 1L4",
     "phones": ["+1 (514) 983-7861", "+1 (438) 833-1906", "+1 (514) 880-2025"], "img": "",
     "desc": "Full-time scholarly training (Dars-e-Nizami) at Jamia-tul-Madina, preparing the next generation of Islamic scholars."},
    {"slug": "kids-quran-classes-winnipeg", "title": "Kids Qur'an Classes", "city": "Winnipeg", "centre": "faizan-e-makkah-winnipeg",
     "when": "Every day, 6:30 PM", "length": "1 hour", "ages": "6+", "teacher": "", "fee": "Free",
     "venue": "Faizan-e-Makkah Winnipeg, 509 St Mary's Rd, Winnipeg, MB", "phones": ["+1 (204) 998-1979"],
     "img": f"{R2}/courses/images/winnipeg.png",
     "desc": "Free daily Qur'an classes for children."},
]

# ---- Departments ------------------------------------------------------------------------------
# (slug, icon, name, short, long, image). slug "" = no page of its own; "http..." = external link
DEPARTMENTS = [
    ("madrasa-tul-madina", "quran", "Madrasa-tul-Madina",
     "Free Qur'an and basic Islamic studies for children and adults.",
     "Madrasa-tul-Madina teaches children to read the Holy Qur'an correctly with tajweed (Nazra) and to memorise it (Hifz), alongside basic Islamic studies and good manners. There are classes for boys, for girls (taught by female teachers) and for adults. Classes are free of charge.",
     f"{UK}/services/252015139205_services.jpeg"),
    ("jamia", "jamia", "Jamia-tul-Madina",
     "Free scholarly training in the Islamic sciences.",
     "", ""),
    ("faizan-weekend-islamic-school", "school", "Faizan Weekend Islamic School",
     "Weekend Islamic school for children in public school.",
     "A weekend Islamic school for children who attend public school during the week. Students learn the basics of faith, prayer, the Qur'an and Islamic character in a friendly environment.",
     f"{UK}/services/37803251903_services.jpeg"),
    ("dar-ul-madinah", "school", "Dar-ul-Madinah",
     "Islamic schooling that combines school subjects with Islamic studies.",
     "Dar-ul-Madinah is Dawat-e-Islami's Islamic school system. Children follow the regular school curriculum together with Qur'an and Islamic studies, in an Islamic environment, starting from nursery level.",
     f"{UK}/services/27824943186_services.jpeg"),
    ("courses", "courses", "Courses",
     "Courses on Islamic knowledge for the general public.",
     "", ""),
    ("maktaba-tul-madina", "book", "Maktaba-tul-Madina",
     "Dawat-e-Islami's publisher of Islamic books and literature.",
     "Maktaba-tul-Madina is the publishing department of Dawat-e-Islami. It publishes and distributes Islamic books, booklets and other religious items, many of them written by Ameer-e-Ahl-e-Sunnat.",
     f"{UK}/services/39996572879_services.jpeg"),
    ("spiritual-cure", "heart", "Spiritual Cure",
     "Free Qur'anic and prophetic remedies for those in difficulty.",
     "The Spiritual Cure department (Rohani Ilaj) offers comfort to people who are ill, grieving or facing difficulty, through remedies from the Qur'an and Hadith. Taweez, Kaat and Istikhara are given free of charge.",
     f"{UK}/services/412033436556_services.jpeg"),
    ("education", "courses", "Education Department",
     "Monthly religious education seminars for students.",
     "", ""),
    ("it", "online", "IT Department",
     "Websites, social media and technology for the work of Dawat-e-Islami.",
     "", ""),
    ("madani-channel", "online", "Madani Channel",
     "24/7 Islamic television in English, Urdu and Bangla.",
     "Madani Channel is Dawat-e-Islami's Islamic television channel, broadcasting around the clock in English, Urdu and Bangla. Its programs teach the Qur'an and Sunnah to viewers around the world. You can watch the English channel live on YouTube.",
     f"{UK}/services/42188134555_services.jpeg"),
]

MORE_DEPARTMENTS = [
    ("Dar-ul-Ifta Ahl-e-Sunnat", "Answers to religious questions from qualified muftis."),
    ("Madani Qafila", "Groups that travel to learn and share the teachings of Islam."),
    ("Khuddam-ul-Masajid", "Building, maintaining and serving our masajid and centres."),
    ("FGRF", "Faizan Global Relief Foundation, Dawat-e-Islami's welfare and relief work."),
    ("Faizan Online Academy", "Live online Qur'an and Islamic studies classes."),
    ("Programs for sisters", "Weekly gatherings, Qur'an classes and courses run by sisters."),
]

# ---- Books (free PDF booklets) ---------------------------------------------------------------
BOOKS = [
    ("Speak Kindly", f"{UK}/booklet/speak-kindly.pdf"),
    ("103 Sunnahs and Manners", f"{UK}/booklet/103-sunnahs-and-manners.pdf"),
    ("Journey Beyond the Heavens", f"{UK}/booklet/journey-beyond-the-heavens.pdf"),
    ("107 Sunnahs and Manners", f"{UK}/booklet/107-sunnahs-and-manners.pdf"),
]
BOOKS_LIBRARY = "https://www.dawateislami.net/bookslibrary/"

# ---- Videos (YouTube video id, title) ----------------------------------------------------------
VIDEOS = [
    ("pJqzdHhGd1A", "Dawat-e-Islami Introduction 2026"),
    ("nQyMBwzZiko", "What is Haya?"),
    ("q2b8GDXGnDs", "Most Devout Mother and Son"),
]

# ---- Donations -------------------------------------------------------------------------------
DONATION_PURPOSES = [
    ("general", "General donation", "For the general work of Dawat-e-Islami Canada and its centres."),
    ("zakat", "Zakat", "The obligatory annual charity, used only for those entitled to receive it."),
    ("sadaqah", "Sadaqah", "Voluntary charity of any amount, given at any time."),
    ("fitrana", "Fitrana", "Sadaqat-ul-Fitr, paid before the Eid-ul-Fitr prayer for each member of the household."),
    ("fidya", "Fidya", "Compensation for fasts that cannot be kept because of illness or old age."),
    ("masjid", "Build a masjid", "Helps build, buy and pay the mortgage of our masajid and centres."),
    ("teacher", "Sponsor a teacher", "Supports a Qur'an teacher at one of our centres."),
    ("jamia", "Jamia-tul-Madina", "Supports the training of Islamic scholars in Canada."),
    ("madrasa", "Madrasa-tul-Madina", "Supports free Qur'an classes for children and adults."),
    ("madani-channel", "Madani Channel", "Supports 24/7 Islamic television around the world."),
    ("spiritual-cure", "Spiritual Cure", "Supports free spiritual remedies for those in difficulty."),
]
DONATION_AMOUNTS = [25, 50, 100, 250, 500]

# Interac e-Transfer (Faizan-e-Madina Masjid, Surrey only)
ETRANSFERS = [
    ("Zakat", "Zakat2dawat@gmail.com"),
    ("Sadaqah", "FMsurrey@gmail.com"),
    ("Mortgage payment donation", "Surrey@dawateislamicanada.net"),
    ("Qarz-e-Hasana contribution", "Surrey@dawateislamicanada.net"),
    ("Fitrah", "Fitra2dawat@gmail.com"),
]

# ---- Five pillars (slug, arabic, name, number word, short, page sections) ---------------------
PILLARS = [
    ("shahadah", "شَهَادَة", "Shahadah", "First", "Faith",
     "Bearing witness that there is none worthy of worship except Allah, and that Muhammad ﷺ is His Messenger.",
     [("The declaration of faith",
       "The Shahadah is the declaration that there is none worthy of worship except Allah, and that Muhammad ﷺ is the Messenger of Allah. A person enters Islam by sincerely believing it in the heart and saying it with the tongue."),
      ("What it means",
       "Believing in Allah means believing that He is One, with no partner, and that He alone deserves worship. Believing in the Holy Prophet ﷺ means accepting him as the final Messenger and following his Sunnah."),
      ("Living by it",
       "Every other pillar builds on the Shahadah. Prayer, Zakat, fasting and Hajj are all ways of living out this belief in daily life.")]),
    ("salah", "صَلَاة", "Salah", "Second", "Prayer",
     "Worshipping Allah through the five daily prayers.",
     [("The five daily prayers",
       "Fajr before sunrise, Zuhr after midday, Asr in the afternoon, Maghrib just after sunset and Isha at night. Each prayer has its own time, and wudu (ablution) is needed before praying."),
      ("Why Salah matters",
       "Salah is a Muslim's direct connection with Allah. It is often mentioned in the Qur'an together with Zakat, and it is the first deed a person will be asked about on the Day of Judgement."),
      ("Who must pray",
       "Salah is obligatory on every sane Muslim who has reached puberty. Congregational prayers and Jumu'ah are held at our centres across Canada.")]),
    ("zakat", "زَكَاة", "Zakat", "Third", "Alms",
     "Giving a portion of eligible wealth each year to those entitled to it.",
     [("What Zakat is",
       "Zakat is the obligatory charity paid once a year on eligible wealth, such as savings, gold, silver and trade goods, when it reaches a minimum amount (nisab) and has been held for a full Islamic year. The usual rate is 2.5%."),
      ("Who receives it",
       "The Qur'an names who may receive Zakat, including the poor and the needy. Zakat given to Dawat-e-Islami Canada is kept separate and used only for those entitled to it."),
      ("Why it matters",
       "Zakat purifies wealth, supports those in need and builds a caring community. For questions about calculating Zakat, ask a qualified scholar.")]),
    ("sawm", "صَوْم", "Sawm", "Fourth", "Fasting",
     "Fasting from dawn to sunset through the month of Ramadan.",
     [("The fast of Ramadan",
       "During Ramadan, Muslims fast from dawn (Fajr) until sunset (Maghrib), staying away from food, drink and other things that break the fast."),
      ("Why we fast",
       "The Qur'an says fasting is prescribed so that we may gain taqwa, mindfulness of Allah. It teaches patience, gratitude and care for those in need."),
      ("Who must fast",
       "Fasting is obligatory on every sane, healthy adult Muslim. Those who are ill or travelling may make up the fasts later, and Fidya is given by those who cannot fast at all.")]),
    ("hajj", "حَجّ", "Hajj", "Fifth", "Pilgrimage",
     "Pilgrimage to Makkah once in a lifetime, for those who are able.",
     [("The pilgrimage",
       "Hajj is the pilgrimage to Makkah during the month of Dhul-Hijjah. Pilgrims follow in the footsteps of Prophet Ibrahim (عليه السلام) and the Holy Prophet ﷺ."),
      ("Who must perform it",
       "Hajj is obligatory once in a lifetime on every adult Muslim who is physically and financially able to make the journey."),
      ("A journey of the heart",
       "Hajj brings Muslims from every country together in equality and devotion, and a Hajj that is accepted wipes away past sins.")]),
]

WORLDWIDE = [
    ("Dawat-e-Islami (global)", "https://www.dawateislami.net/"),
    ("Dawat-e-Islami USA", "https://www.dawateislamiusa.org/"),
    ("Dawat-e-Islami UK", "https://dawateislami.co.uk/"),
    ("Ameer-e-Ahl-e-Sunnat", "https://www.ilyasqadri.com/"),
    ("Faizan Online Academy", "https://www.quranteacher.net/"),
    ("Ask a question (Darul Ifta)", "https://www.fatwaqa.com/en"),
]
