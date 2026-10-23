#!/usr/bin/env python3
"""Confere o padrão dos cards antes do commit. Uso: python3 tools/validar.py
Erro (❌) = NÃO pode commitar. Aviso (⚠️) = corrigir se der."""
import json, re, sys, collections
AREAS = {'Cirurgia','Clínica Médica','Ginecologia','Obstetrícia','Medicina Preventiva','Pediatria'}
CM = {'Cardiologia','Dermatologia','Endocrinologia','Gastroenterologia','Hematologia','Infectologia','Nefrologia','Neurologia','Pneumologia','Psiquiatria','Reumatologia'}
ESCORES = ['Alvarado','Apgar','Glasgow','Manning','perfil biofísico','Bishop','Silverman','Capurro','Ballard','Wells','CURB-65','CHA2DS2','HAS-BLED','Child','MELD','Ranson','BISAP','APACHE','qSOFA','SOFA','Lee','RCRI','Fried','IVCF','Downes','Westley','Centor','Gleason','Breslow','Kupperman','Ferriman','PHQ-9','CAGE','AUDIT','Mini-Mental','Nugent','Amsel','Rockall','Blatchford','Forrest','Hinchey','Mannheim','Killip','TIMI','GRACE','NIHSS','Hunt','Fisher','Spetzler','Wilkins']
erros, avisos = [], []
E = lambda c, m: erros.append(f"❌ {c}: {m}")
W = lambda c, m: avisos.append(f"⚠️  {c}: {m}")
d = json.load(open('data/cards.json'))
try: PREV = json.load(open('data/prevalencia.json')).get('baralhos', {})
except Exception: PREV = {}
cards = d['cards']
ids = collections.Counter(c.get('id') for c in cards)
for i, n in ids.items():
    if n > 1: E(i, 'id repetido')
deck = collections.defaultdict(list)
for c in cards:
    i = c.get('id', '?')
    for f in ('id','tipo','area','tema','sub','frente','contexto','fonte','add'):
        if not c.get(f): E(i, f'falta o campo "{f}"')
    if c.get('area') not in AREAS: E(i, f'área inválida: {c.get("area")}')
    if c.get('area') == 'Clínica Médica' and c.get('tema') not in CM: E(i, f'Clínica Médica usa só as sub-áreas fixas (veio "{c.get("tema")}")')
    if not c.get('ctxvisual'): E(i, 'falta "ctxvisual" (ilustração do contexto do tema)')
    deck[(c.get('area'), c.get('tema'), c.get('sub'))].append(c)
    ctx = c.get('contexto') or ''
    if ctx:
        if not ctx.lstrip().startswith('**'): E(i, 'contexto: 1ª linha tem que ser a definição em **negrito**')
        if 'Como cai:' not in ctx: E(i, 'contexto: falta o bloco "Como cai:"')
        for l in ctx.split('\n'):
            if re.match(r'^\s*[-•◦]\s', l) and ' · ' in l: E(i, f'contexto: itens juntos com "·" na mesma linha → "{l.strip()[:60]}"')
        if len(ctx) > 1600: W(i, 'contexto longo demais (deve caber numa tela)')
    if c.get('tipo') == 'flash':
        v = c.get('verso') or ''
        b0 = v.split('\n\n')[0].strip().split('\n')
        if not b0 or not b0[0].startswith('**'): E(i, 'verso: 1ª linha tem que ser a RESPOSTA DIRETA em **negrito** (é ela que fica em destaque)')
        for l in b0:
            core = l.strip().strip('*')
            if re.match(r'^\s*[-•◦]\s', l): continue
            if ' · ' in core or re.search(r'[.;]\s+\**[A-ZÁÉÍÓÚÂÊÔÃÕÇ]', core): E(i, f'resposta em destaque com 2 ideias na mesma linha (quebre em linhas) → "{l.strip()[:70]}"')
        if len(v.split('\n\n')) < 2 and not c.get('visual'): W(i, 'verso sem explicação em tópicos e sem visual')
        for bl in v.split('\n\n')[1:]:
            ls = [x for x in bl.split('\n') if x.strip()]
            prosa = [x for x in ls if not re.match(r'^\s*[-•◦]\s', x) and not x.strip().endswith(':')]
            if prosa and len(' '.join(prosa)) > 160: E(i, f'verso: explicação em texto corrido — use rótulo + tópicos "- " → "{prosa[0][:60]}"')
        for l in v.split('\n'):
            if re.match(r'^\s*[-•◦]\s', l) and ' · ' in l: E(i, f'verso: itens juntos com "·" no mesmo tópico → "{l.strip()[:60]}"')
        if not c.get('visual'): W(i, 'card sem "visual" (imagem real, tabela, fluxo, vs, lista ou grupos)')
    if c.get('tipo') == 'quiz':
        o = c.get('opcoes') or []
        if len(o) != 4: E(i, 'quiz precisa de 4 alternativas (A–D)')
        if not isinstance(c.get('certa'), int) or not 0 <= c['certa'] < len(o): E(i, '"certa" inválida')
        if len(c.get('comentarios') or []) != len(o): E(i, 'quiz precisa de um comentário por alternativa')
    if not c.get('pegadinha'): W(i, 'sem "pegadinha"')
    for v in (c.get('visual') if isinstance(c.get('visual'), list) else [c.get('visual')] if c.get('visual') else []) + ([c['ctxvisual']] if isinstance(c.get('ctxvisual'), dict) else []):
        if v.get('tipo') == 'img' and not (str(v.get('src','')).startswith('https://upload.wikimedia.org/') or str(v.get('src','')).startswith('data/img/') or str(v.get('src','')).startswith('https://')): E(i, 'imagem com src inválido')
for k, cs in deck.items():
    nome = ' › '.join(map(str, k))
    if k[2] not in PREV: E(nome, 'baralho sem entrada em data/prevalencia.json (quanto cai na UERJ)')
    if len({c.get('contexto') for c in cs}) > 1: E(nome, 'cards do mesmo baralho com contextos diferentes (tem que ser o MESMO texto)')
    if not any(c.get('uerj') for c in cs): W(nome, 'nenhum card do baralho tem o campo "uerj"')
    if not any(c.get('tipo') == 'quiz' for c in cs): W(nome, 'baralho sem questão estilo prova (quiz)')
    txt = ' '.join((c.get('verso') or '') + ' ' + (c.get('contexto') or '') for c in cs)
    for s in ESCORES:
        if re.search(r'\b' + re.escape(s) + r'\b', txt):
            tem = any(isinstance(c.get('visual'), (dict, list)) and 'pont' in json.dumps(c.get('visual'), ensure_ascii=False).lower() for c in cs) or re.search(r'(1 ponto|pontos?\b)', txt)
            if not tem: E(nome, f'escore "{s}" citado sem destrinchar (itens, pontos, total e faixas)')
print('\n'.join(erros + avisos) or 'Tudo certo.')
print(f'\n{len(cards)} cards · {len(deck)} baralhos · {len(erros)} erro(s) · {len(avisos)} aviso(s)')
sys.exit(1 if erros else 0)
