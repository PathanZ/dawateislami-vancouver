/*
  Events and announcements shown on the home page and the Events page.

  One-off event:
    { date: "2026-11-05", time: "7:00 PM", title: "...", centre: "Vancouver",
      details: "...", image: "assets/img/events/poster.jpg", link: "https://..." }
    It disappears automatically the day after its date.

  Weekly event (repeats every week):
    { weekly: "Thursday", time: "7:00 PM", title: "...", centre: "Vancouver", details: "..." }

  image and link are optional.
*/
window.DI_EVENTS = [
  {
    weekly: "Thursday",
    time: "7:00 PM",
    title: "Weekly Ijtima",
    centre: "Faizan-e-Madina Vancouver, Surrey",
    details: "Tilawat, naat, bayan, zikr, dua and salam. Dinner served, with a separate arrangement for sisters.",
    link: "https://dawateislamivancouver.ca"
  }
];
