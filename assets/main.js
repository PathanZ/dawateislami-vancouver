/* Dawat-e-Islami Canada: small scripts for menu, slider, videos, maps, donation and forms. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };

  // Year in footer
  var y = $('#year'); if (y) y.textContent = new Date().getFullYear();

  // Mobile menu
  var btn = $('.menu-toggle'), nav = $('#nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
      btn.textContent = open ? 'Close' : 'Menu';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded', false); btn.textContent = 'Menu'; btn.focus(); }
    });
  }

  // Copy buttons (e-Transfer emails)
  $$('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-copy');
      function ok() { b.textContent = 'Copied'; b.classList.add('ok'); setTimeout(function () { b.textContent = 'Copy'; b.classList.remove('ok'); }, 1800); }
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(ok, function () { window.prompt('Copy this email:', t); });
      else window.prompt('Copy this email:', t);
    });
  });

  // Home slider
  var sl = $('[data-slider]');
  if (sl) {
    var slides = $$('.slide', sl), dots = $$('.slide-dots span', sl), i = 0, timer;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      dots.forEach(function (d, k) { d.classList.toggle('on', k === i); });
    }
    function start() { if (!reduce) { clearInterval(timer); timer = setInterval(function () { show(i + 1); }, 5500); } }
    $('[data-next]', sl).addEventListener('click', function () { show(i + 1); start(); });
    $('[data-prev]', sl).addEventListener('click', function () { show(i - 1); start(); });
    var x0 = null;
    sl.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    sl.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) { show(i + (dx < 0 ? 1 : -1)); start(); }
    });
    start();
  }

  // Videos: load YouTube only when tapped
  $$('[data-yt]').forEach(function (f) {
    var b = $('button', f);
    if (!b) return;
    b.addEventListener('click', function () {
      var id = f.getAttribute('data-yt');
      f.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="YouTube video" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
    });
  });

  // Centres page: "Show on map"
  var frame = $('#mapFrame');
  if (frame) {
    $$('.map-btn').forEach(function (a) {
      a.addEventListener('click', function (ev) {
        ev.preventDefault();
        var q = a.getAttribute('data-q');
        frame.src = 'https://www.google.com/maps?q=' + encodeURIComponent(q) + '&output=embed';
        $('#mapName').textContent = a.getAttribute('data-name');
        $('#mapAddr').textContent = q;
        $('#map').scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  // Donate page
  var df = $('#donateForm');
  if (df) {
    var params = new URLSearchParams(location.search);
    var pp = params.get('purpose'), pc = params.get('centre');
    if (pp) { var r = $('input[name=purpose][value="' + pp.replace(/[^a-z-]/g, '') + '"]', df); if (r) r.checked = true; }
    if (pc) { var sel = $('#d_centre'); if ([].some.call(sel.options, function (o) { return o.value === pc; })) sel.value = pc; }
    var other = $('#d_other'), otherWrap = $('#d_other_wrap'), sum = $('#d_summary'), err = $('#d_err');
    function val() {
      var p = $('input[name=purpose]:checked', df), a = $('input[name=amount]:checked', df), f = $('input[name=freq]:checked', df);
      var amt = a.value === 'other' ? parseFloat(other.value) : parseFloat(a.value);
      var c = $('#d_centre'); var cname = c.value ? c.options[c.selectedIndex].text : '';
      return { purpose: p.getAttribute('data-label'), pkey: p.value, amount: amt, freq: f.value, centre: cname, ckey: c.value };
    }
    function money(n) { return '$' + (Math.round(n * 100) / 100).toLocaleString('en-CA'); }
    function update() {
      otherWrap.hidden = $('input[name=amount]:checked', df).value !== 'other';
      var v = val(); err.textContent = '';
      var amt = isFinite(v.amount) && v.amount > 0 ? money(v.amount) : 'an amount';
      sum.innerHTML = 'You are giving <b>' + amt + '</b> ' + (v.freq === 'monthly' ? 'every month' : 'one time') +
        ' for <b>' + v.purpose + '</b>' + (v.centre ? ' at <b>' + v.centre.replace(/</g, '') + '</b>' : '') + '.';
    }
    df.addEventListener('change', update); df.addEventListener('input', update); update();
    df.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = val();
      if (!(v.amount > 0)) { err.textContent = 'Please enter an amount.'; other.focus(); return; }
      var url = df.getAttribute('data-url');
      if (url) {
        var u = url + (url.indexOf('?') < 0 ? '?' : '&') + 'amount=' + v.amount + '&purpose=' + encodeURIComponent(v.purpose) +
          (v.ckey ? '&centre=' + encodeURIComponent(v.ckey) : '') + '&frequency=' + v.freq;
        window.location.href = u;
      } else {
        err.textContent = 'Online payments are not set up yet. Please use Interac e-Transfer or give at a centre.';
        var et = $('#etransfer'); if (et) et.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }

  // Receipt + contact forms: send to a Google Form when connected (data-gform)
  $$('form.gform').forEach(function (form) {
    var err = $('.form-err', form), done = $('.done', form), sbtn = $('button[type=submit]', form);
    var dt = $('input[type=date]', form); if (dt) dt.max = new Date().toISOString().slice(0, 10);
    form.addEventListener('input', function (e) { if (e.target.classList) e.target.classList.remove('bad'); err.textContent = ''; });
    form.addEventListener('submit', function (e) {
      e.preventDefault(); err.textContent = '';
      var bad = null;
      $$('[required]', form).forEach(function (el) {
        var ok = el.checkValidity() && String(el.value).trim() !== '';
        if (!ok) { el.classList.add('bad'); if (!bad) bad = el; }
      });
      if (bad) { err.textContent = 'Please fill in the highlighted fields.'; bad.focus(); return; }
      if (form.website && form.website.value) return;
      var cfg = {}; try { cfg = JSON.parse(form.getAttribute('data-gform') || '{}'); } catch (x) {}
      if (!cfg.action) { err.textContent = 'This form is not connected yet. Please email canada@dawateislami.net instead.'; return; }
      var data = new URLSearchParams();
      Object.keys(cfg).forEach(function (k) {
        if (k === 'action') return;
        var vals = $$('[name="' + k + '"]', form).filter(function (el) { return (el.type !== 'checkbox' && el.type !== 'radio') || el.checked; })
          .map(function (el) { return el.value.trim(); });
        vals.forEach(function (v) { data.append('entry.' + String(cfg[k]).replace(/^entry\./, ''), v); });
      });
      sbtn.disabled = true; sbtn.textContent = 'Sending…';
      fetch(cfg.action, { method: 'POST', mode: 'no-cors', body: data }).then(function () {
        $$('.field,.row2,fieldset,h2,button[type=submit]', form).forEach(function (el) { el.hidden = true; });
        done.hidden = false; done.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }).catch(function () {
        sbtn.disabled = false; sbtn.textContent = 'Try again';
        err.textContent = 'Could not send. Check your internet connection and try again.';
      });
    });
  });

  // Announcements from assets/events.js (one-off events disappear after their date)
  var box = $('[data-events]');
  if (box && window.DI_EVENTS) {
    var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var today = new Date(); today.setHours(0, 0, 0, 0);
    function esc(s) { return String(s || '').replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
    function safeUrl(u) { u = String(u || ''); return /^(https?:\/\/|assets\/)/.test(u) ? u : ''; }
    function nextWeekly(day) { var d = new Date(today), n = DAYS.indexOf(day); if (n < 0) return null; d.setDate(d.getDate() + ((n - d.getDay() + 7) % 7)); return d; }
    function parseDate(s) { var p = String(s).split('-'); return p.length === 3 ? new Date(+p[0], +p[1] - 1, +p[2]) : null; }
    var list = window.DI_EVENTS.map(function (ev) {
      var d = ev.weekly ? nextWeekly(ev.weekly) : parseDate(ev.date);
      return d && d >= today ? { ev: ev, d: d } : null;
    }).filter(Boolean).sort(function (a, b) { return a.d - b.d; });
    var lim = parseInt(box.getAttribute('data-limit') || '0', 10); if (lim) list = list.slice(0, lim);
    if (list.length) {
      var wrap = document.querySelector('[data-announce-wrap]'); if (wrap) wrap.hidden = false;
      box.innerHTML = list.map(function (x) {
        var ev = x.ev, pic = safeUrl(ev.image), link = safeUrl(ev.link);
        var pre = document.querySelector('link[rel=stylesheet][href*="assets/style.css"]').getAttribute('href').split('assets/')[0];
        if (pic && pic.indexOf('assets/') === 0) pic = pre + pic;
        return '<article class="event"><div class="date"><small>' + (ev.weekly ? 'Every' : MONTHS[x.d.getMonth()]) + '</small><b>' + (ev.weekly ? esc(ev.weekly.slice(0, 3)) : x.d.getDate()) + '</b></div><div>' +
          '<h3>' + esc(ev.title) + '</h3><p>' + esc(ev.time) + (ev.centre ? ' · ' + esc(ev.centre) : '') + '</p>' +
          (ev.details ? '<p>' + esc(ev.details) + '</p>' : '') +
          (pic ? '<img src="' + esc(pic) + '" alt="" loading="lazy">' : '') +
          (link ? '<p><a href="' + esc(link) + '" target="_blank" rel="noopener">More details →</a></p>' : '') + '</div></article>';
      }).join('');
    }
  }
})();
