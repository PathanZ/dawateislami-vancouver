"""All the words and lists on the site. Edit this file to change content, then run: python3 build.py"""

SITE = "https://dawateislami.ca"
BN = "81933 5662 RR0001"
EMAIL = "canada@dawateislami.net"
OFFICE = "120 - 32 Westwinds Cres NE, Calgary, AB T3J 5L3"
VANCOUVER_SITE = "https://dawateislamivancouver.ca"

# Fill these in when ready; empty = shown as "TBC" on the preview
DONATE_URL = ""
SOCIAL = {  # name: url
    "Facebook": "",
    "Instagram": "",
    "YouTube": "",
    "TikTok": "",
    "X": "",
}

# ---- Centres (from dawateislamicanada.net/contact-us) -------------------------
# site: the centre's own website, if it has one
CENTRES = [
    {"province": "British Columbia", "city": "Vancouver", "name": "Faizan-e-Madina Masjid",
     "address": "7062 134 St, Surrey, BC V3W 4T2", "phone": "+1 (778) 895-0886", "site": VANCOUVER_SITE, "note": ""},
    {"province": "Alberta", "city": "Calgary", "name": "Faizan-e-Madina",
     "address": "32 Westwinds Crescent NE, Calgary, AB T3J 5H2", "phone": "+1 (403) 618-5408", "site": "", "note": ""},
    {"province": "Alberta", "city": "Calgary", "name": "Faizan-e-Makkah",
     "address": "4250 109 Ave NE, Calgary, AB T3N 1Z3", "phone": "+1 (403) 618-5408", "site": "", "note": ""},
    {"province": "Alberta", "city": "Edmonton", "name": "Faizan-e-Madina Edmonton",
     "address": "11809 96 St, Edmonton, AB T5G 1V4", "phone": "+1 (780) 729-6492", "site": "", "note": ""},
    {"province": "Saskatchewan", "city": "Regina", "name": "Faizan-e-Madina Islamic Center",
     "address": "1169 Athol St, Regina, SK S4T 3C3", "phone": "+1 (438) 401-0782", "site": "", "note": ""},
    {"province": "Manitoba", "city": "Winnipeg", "name": "Faizan-e-Madina Islamic Centre",
     "address": "585 St Anne's Rd, Winnipeg, MB R2M 5R5", "phone": "+1 (204) 998-1979", "site": "", "note": ""},
    {"province": "Manitoba", "city": "Winnipeg", "name": "Faizan-e-Makkah",
     "address": "509 Trans-Canada Hwy, Winnipeg, MB R2M 3L2", "phone": "+1 (204) 998-1979", "site": "",
     "note": "Under construction"},
    {"province": "Ontario", "city": "East York (Thorncliffe)", "name": "Faizan-e-Attar",
     "address": "49 Thorncliffe Park Dr, Unit 120, East York, ON M4H 1J6", "phone": "+1 (647) 366-3786", "site": "", "note": ""},
    {"province": "Ontario", "city": "Etobicoke", "name": "Faizan-e-Madina Etobicoke",
     "address": "595 Albion Rd, Etobicoke, ON M9V 1A1", "phone": "+1 (647) 366-3786", "site": "", "note": ""},
    {"province": "Ontario", "city": "Hamilton", "name": "Faizan-e-Madina Hamilton",
     "address": "1202 Dunsmure Rd, Hamilton, ON L8H 1L4", "phone": "+1 (647) 366-3786", "site": "", "note": ""},
    {"province": "Ontario", "city": "Ottawa", "name": "Faizan-e-Madina Islamic Center",
     "address": "415 McArthur Ave, Ottawa, ON K1K 1G5", "phone": "+1 (514) 983-7861", "site": "", "note": ""},
    {"province": "Quebec", "city": "Montreal", "name": "Faizan-e-Madina Montreal",
     "address": "810 Rue Saint-Roch, Montréal, QC H3N 1L4", "phone": "+1 (514) 983-7861", "site": "", "note": ""},
    {"province": "Quebec", "city": "Montreal", "name": "Faizan-e-Hub-e-Rasool",
     "address": "1008 Rue Jean-Talon O, Montréal, QC H3N 1T1", "phone": "+1 (514) 983-7861", "site": "", "note": ""},
]

# ---- Services (id, icon, title, short text, longer text) -----------------------
SERVICES = [
    ("weekly-ijtima", "ijtima", "Weekly Ijtima",
     "Weekly gatherings with tilawat, naat, bayan, zikr and dua.",
     "Every centre holds a weekly spiritual gathering, open to everyone. It includes recitation of the Qur'an, naat, a Sunnah-inspired bayan, zikr and a heartfelt dua. Separate gatherings are held for Islamic sisters."),
    ("madrasa", "quran", "Madrasa-tul-Madina",
     "Free Qur'an reading, tajweed and Hifz for children.",
     "Madrasa-tul-Madina teaches children to read the Qur'an correctly with tajweed (Nazra) and to memorise it (Hifz), alongside basic Islamic studies and good manners. Classes are free of charge."),
    ("adult-quran", "quran", "Qur'an classes for adults",
     "Learn to read the Qur'an correctly, at any age.",
     "Madrasa-tul-Madina for adults helps brothers and sisters learn or improve their Qur'an reading with correct pronunciation, at their own pace and whatever their starting point."),
    ("weekly-school", "school", "Faizan Weekly Islamic School",
     "Faith, character and Qur'an for children on weekends.",
     "A weekend Islamic school for children who attend public school during the week. Students learn the basics of faith, prayer, the Qur'an and Islamic character in a friendly environment."),
    ("courses", "courses", "Islamic courses",
     "Short courses on everyday Islamic knowledge.",
     "Short courses on the essentials every Muslim needs, such as wudu, salah, fasting and daily Sunnahs, taught by qualified teachers and open to the community."),
    ("sisters", "sisters", "Programs for sisters",
     "Gatherings, classes and courses by and for sisters.",
     "Islamic sisters have their own weekly gatherings, Qur'an classes and courses, run by sisters in a separate, comfortable setting."),
    ("youth", "jummah", "Youth gatherings",
     "Programs for young brothers and sisters.",
     "Youth gatherings for Islamic brothers and sisters take place in provinces, cities and local areas across Canada, helping young Muslims grow in faith and character together."),
    ("spiritual-cure", "heart", "Spiritual cure (Rohani Ilaj)",
     "Guidance and duas from the Qur'an and Sunnah.",
     "The spiritual cure service offers comfort and guidance to people facing difficulty, through Qur'anic and prophetic remedies and duas."),
    ("jamia", "jamia", "Jamia-tul-Madina",
     "Scholarly training, in Montreal, Quebec.",
     "Jamia-tul-Madina is Dawat-e-Islami's Islamic seminary. In Canada it is producing scholars in Montreal, Quebec."),
    ("online-academy", "online", "Faizan Online Academy",
     "Live online Qur'an and Islamic studies classes.",
     "Faizan Online Academy offers live online classes in Qur'an reading, tajweed and Islamic studies, so you can learn from home."),
]

# ---- Departments (from dawateislamicanada.net/departments) ---------------------
DEPARTMENTS = [
    ("Madrasa-tul-Madina for Boys", "Free Qur'an reading, tajweed and Hifz classes for boys."),
    ("Madrasa-tul-Madina for Girls", "Free Qur'an reading, tajweed and Hifz classes for girls, taught by female teachers."),
    ("Madrasa-tul-Madina for Adults", "Qur'an classes for adult brothers and sisters, at any level."),
    ("Faizan Weekly Islamic School", "Weekend Islamic education for children in public school."),
    ("Jamia-tul-Madina", "Training future Islamic scholars, in Montreal, Quebec."),
    ("Islamic Courses", "Short courses on the essentials of Islamic knowledge and practice."),
    ("Dar-ul-Ifta Ahl-e-Sunnat", "Answers to religious questions from qualified muftis."),
    ("Spiritual Cures", "Comfort and guidance through Qur'anic and prophetic remedies."),
    ("Madani Qafila", "Groups that travel to learn and share the teachings of Islam."),
    ("Khuddam-ul-Masajid", "Building, maintaining and serving our masajid and centres."),
    ("FGRF", "Faizan Global Relief Foundation, Dawat-e-Islami's welfare and relief work."),
    ("Health Care", "Support and guidance for the community's health and wellbeing."),
    ("Madani Channel", "Dawat-e-Islami's Islamic television channel, in English and other languages."),
    ("Donation Boxes", "Collection boxes that support the work of Dawat-e-Islami."),
    ("Finances", "Managing donations transparently and responsibly."),
    ("I.T.", "Websites, apps and technology for Dawat-e-Islami Canada."),
]

# ---- Donations (Interac e-Transfer, Faizan-e-Madina Vancouver) -----------------
ETRANSFERS = [
    ("Zakat", "Zakat2dawat@gmail.com"),
    ("Sadaqah", "FMsurrey@gmail.com"),
    ("Mortgage payment donation", "Surrey@dawateislamicanada.net"),
    ("Qarz-e-Hasana contribution", "Surrey@dawateislamicanada.net"),
    ("Fitrah", "Fitra2dawat@gmail.com"),
]

DONATION_TYPES = [
    ("Zakat", "The obligatory annual charity of 2.5% on eligible wealth, used only for those entitled to receive it."),
    ("Sadaqah", "Voluntary charity of any amount, given at any time, for the general work of the centres."),
    ("Fitrah", "Sadaqat-ul-Fitr, paid before the Eid-ul-Fitr prayer on behalf of each member of the household."),
    ("Masjid and mortgage", "Helps pay the mortgage and running costs of our masajid and Islamic centres."),
    ("Qarz-e-Hasana", "An interest-free loan to the centre, returned to you as agreed."),
]

PILLARS = [
    ("شَهَادَة", "Shahadah", "Belief in the oneness of Allah and that Muhammad ﷺ is His final messenger."),
    ("صَلَاة", "Salah", "Worshipping Allah through the five daily prayers."),
    ("زَكَاة", "Zakat", "Giving 2.5% of eligible wealth each year to those in need."),
    ("صَوْم", "Sawm", "Fasting from dawn to sunset through the month of Ramadan."),
    ("حَجّ", "Hajj", "Pilgrimage to Makkah once in a lifetime, for those who are able."),
]

WORLDWIDE = [
    ("Dawat-e-Islami (global)", "https://www.dawateislami.net/"),
    ("Dawat-e-Islami USA", "https://www.dawateislamiusa.org/"),
    ("Dawat-e-Islami UK", "https://dawateislami.co.uk/"),
    ("Ameer-e-Ahl-e-Sunnat", "https://www.ilyasqadri.com/"),
    ("Ask a question (Darul Ifta)", "https://www.fatwaqa.com/en"),
    ("Islamic books library", "https://www.dawateislami.net/bookslibrary/"),
]
