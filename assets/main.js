(function(){
  // Mobile menu
  var toggle=document.querySelector('.menu-toggle'), nav=document.querySelector('.nav');
  if(toggle&&nav){
    toggle.addEventListener('click',function(){
      var open=nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded',open);
    });
    nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');});});
  }
  var yr=document.getElementById('year'); if(yr) yr.textContent=new Date().getFullYear();

  // Copy buttons (e-Transfer emails)
  document.querySelectorAll('.copy[data-copy]').forEach(function(btn){
    btn.addEventListener('click',function(){
      var text=btn.getAttribute('data-copy');
      function ok(){btn.textContent='Copied';btn.classList.add('done');setTimeout(function(){btn.textContent='Copy';btn.classList.remove('done');},1800);}
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(ok,function(){window.prompt('Copy this email:',text);});}
      else{window.prompt('Copy this email:',text);}
    });
  });

  // Events
  var boxes=document.querySelectorAll('[data-events]');
  if(!boxes.length) return;
  var EVENTS=window.DI_EVENTS||[];
  var DAYS=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var today=new Date(); today.setHours(0,0,0,0);

  function nextWeekly(dayName){
    var target=DAYS.indexOf(dayName); if(target<0) return null;
    var d=new Date(today); d.setDate(d.getDate()+((target-d.getDay()+7)%7)); return d;
  }
  function parseDate(s){var p=/^(\d{4})-(\d{2})-(\d{2})$/.exec(s||''); return p?new Date(+p[1],+p[2]-1,+p[3]):null;}
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function safeUrl(u){u=String(u||''); return /^(https?:\/\/|assets\/)/.test(u)?u:'';}

  var items=EVENTS.map(function(e){
    var d=e.weekly?nextWeekly(e.weekly):parseDate(e.date);
    return d&&d>=today?{e:e,d:d}:null;
  }).filter(Boolean).sort(function(a,b){return a.d-b.d;});

  boxes.forEach(function(box){
    var limit=+box.getAttribute('data-limit')||items.length;
    var list=items.slice(0,limit);
    if(!list.length){box.innerHTML='<p class="muted empty-events">No upcoming events right now. Please check back soon.</p>';return;}
    box.innerHTML=list.map(function(it){
      var e=it.e, img=safeUrl(e.image), link=safeUrl(e.link);
      var when=e.weekly?('Every '+esc(e.weekly)):(DAYS[it.d.getDay()]+', '+MON[it.d.getMonth()]+' '+it.d.getDate());
      return '<article class="event">'
        +(img?'<img class="event-img" src="'+esc(img)+'" alt="'+esc(e.title)+' poster" loading="lazy">':'')
        +'<div class="event-date"><span class="m">'+MON[it.d.getMonth()]+'</span><span class="d">'+it.d.getDate()+'</span></div>'
        +'<div class="event-body"><p class="event-when">'+when+(e.time?' · '+esc(e.time):'')+'</p>'
        +'<h3>'+esc(e.title)+'</h3>'
        +(e.centre?'<p class="event-where">'+esc(e.centre)+'</p>':'')
        +(e.details?'<p>'+esc(e.details)+'</p>':'')
        +(link?'<a class="more" href="'+esc(link)+'"'+(/^https?:/.test(link)?' target="_blank" rel="noopener"':'')+'>Details</a>':'')
        +'</div></article>';
    }).join('');
  });
})();
