const V='uerjcards-v48';
const SHELL=['./','index.html','manifest.webmanifest','icon.svg','icon-192.png','icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(SHELL)));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(e.request.method!=='GET'||u.hostname==='api.github.com')return;
  // conteúdo e página: rede primeiro sem cache HTTP do navegador (o GitHub Pages guarda 10 min), cache se offline
  if(u.pathname.includes('/data/')||e.request.mode==='navigate'||u.pathname.endsWith('index.html')){
    e.respondWith(fetch(e.request.url,{cache:'no-cache'}).then(r=>{const c=r.clone();caches.open(V).then(x=>x.put(e.request.mode==='navigate'?'index.html':e.request.url.split('?')[0],c));return r}).catch(()=>caches.match(e.request.mode==='navigate'?'index.html':e.request.url.split('?')[0])));
    return;
  }
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(n=>{if(n.ok||n.type==='opaque'){const c=n.clone();caches.open(V).then(x=>x.put(e.request,c))}return n})));
});
