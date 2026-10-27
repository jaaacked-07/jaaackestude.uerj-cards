# UERJ Cards — instruções para o Claude

App PWA de flashcards/quiz da Jacke (interna de medicina) para a prova de residência da **UERJ (01/11/2026)**.
Publicado via GitHub Pages: https://jaaacked-07.github.io/jaaackestude.uerj-cards/

- `index.html` — app inteiro (não mexer ao gerar cards).
- `data/cards.json` — todos os cards. O app lê esse arquivo toda vez que abre.
- `data/notas.json` — anotações que a Jacke guarda no app (vão sozinhas para cá).
- `data/progresso.json` — progresso dela sincronizado entre aparelhos. **Nunca editar.**
- Cards que ela cria pela aba **Criar** (frente e verso, cloze, oclusão de imagem) ficam em `data/progresso.json` → `extra` (com `meu: true`). Nunca edite; só leia para não criar card repetido.
- `data/prevalencia.json` — quanto cada baralho cai na UERJ (Foco UERJ, provas 2022–2026): `baralhos[sub].q` = nº de questões do tema. O app usa isso para pôr primeiro o que mais cai. **Ao criar um baralho novo (ou se ela renomeou um baralho), acrescente a entrada dele com o nome exato que está em `cards.json`** (`"<nome do baralho>": {"q": N, "temas": "..."}`), contando as questões do tema no `DATA` do index.html do repositório jaaacked-07/jaaackestude.prevalenciaUERJ (público). Sem questão = `q: 0`. Nunca invente número.
- `data/chave.json` — acesso do app criptografado com o usuário dela. **Nunca editar nem apagar.**

## ⚠️ PADRÃO OBRIGATÓRIO DE TODO CARD (checklist — nada sai sem isso)

1. **Foco UERJ:** escreva como a UERJ cobra (caso clínico curto, conduta, pegadinha da banca). Fonte = bibliografia/diretriz **vigente** (ver "Qualidade do conteúdo"). Campo `uerj` sempre que der e bloco **"O que mais cai na UERJ:"** no FINAL do contexto.
2. **Contexto do tema (`contexto`) em TODOS os cards — PROIBIDO card sem contexto.** Mesmo texto para o baralho inteiro; se o baralho já existe, copie o contexto dele.
3. **Ilustração do contexto (`ctxvisual`) em TODOS os cards** (mesma do baralho): imagem real se existir; senão esquema SVG.
4. **Visual no card (`visual`) sempre que possível:** imagem real > fluxograma > tabela > comparação (vs) > lista/grupos. Escore/classificação/conduta por etapas → SEMPRE tabela ou fluxo.
5. **Resposta em destaque = gatilho de memória** (regra somada às demais, não substitui nenhuma):
   - **1ª linha:** a resposta OBJETIVA e fácil de lembrar, trazendo imediatamente o que a frente pergunta (curta: idealmente ≤ ~8 palavras). Cria a associação rápida pergunta → informação essencial.
   - **Linhas seguintes da caixinha:** só os detalhes que fazem parte da resposta principal (ex.: adulto × criança, os itens da lista pedida). Explicação, porquê, conduta geral e pegadinha ficam FORA da caixinha, no jeito de sempre.
   - **UM conceito por linha** na caixinha: nada de "A. B.", "A; B", "A · B" nem lista separada por vírgula na mesma linha. Lista = título em negrito (`**Manter:**`) + um item por linha (`- item`) dentro do mesmo bloco.
6. **Explicação só em tópicos:** depois de uma linha em branco, rótulo curto terminando em `:` + tópicos `- ` (subtópico com 2 espaços). **Proibido texto corrido.**
7. **Nada repetido** entre verso e visual (ver "Qualidade").
8. **Escores destrinchados:** itens, pontos, total e faixas, em tabela.
8b. **Critério/classificação no card → critério COMPLETO + conduta no CONTEXTO.** Se qualquer card do baralho pergunta um pedaço de um critério, escore, estadiamento ou classificação (TNM, FIGO, BI-RADS, Bethesda, Tóquio, Hinchey, Jones, Alvarado, Glasgow, Manning, Los Angeles, Nyhus, Atlanta…), o contexto do baralho tem que trazer o critério INTEIRO destrinchado com a conduta de cada categoria — ela se confunde quando só vê um pedaço. Coloque como tabela no FIM do `ctxvisual` (vira lista: `[ilustração existente, {tabela}]`), com `"crit": true` na tabela, colunas `Categoria | Critério | Conduta` e a 1ª célula do cabeçalho com o nome do critério (ex.: `"FIGO 2018 (colo)"`). Não mude o texto do contexto para isso (as anotações e marcações dela ficam presas a ele). Nunca apague os cards que já perguntam pedaços do critério.
9. **Pelo menos 1 quiz por baralho** (se o baralho já tem quiz, não precisa criar outro) (4 alternativas, comentário em cada uma) e `pegadinha` sempre que der.
9b. **Varie a letra da resposta certa dos quizzes** (`certa` = 0, 1, 2 ou 3 → A, B, C, D). Ela reclamou que estava quase tudo "B". Sorteie a posição da certa em cada quiz novo (e mova o comentário junto); quizzes do mesmo dia não podem ter todos a mesma letra. O validador dá ❌ se uma letra passar de 35% do total ou se todos os quizzes novos do dia tiverem a mesma letra. Não use alternativas que dependam da posição ("todas as anteriores", "A e B").
10. **Baralho novo → entrada em `data/prevalencia.json`** (quanto cai na UERJ). É isso que faz o app priorizar o tema.
11. **Macete em TODO card novo (campo `macete`) — ela pediu, ajuda MUITO a gravar.** Mnemônico, acróstico, rima, associação visual ou "regra de bolso" curta (1–2 linhas). O app mostra numa caixa amarela "🧠 Macete" logo abaixo da resposta. Use macete consagrado quando existir (ex.: "MUDPILES", "Charcot = febre + icterícia + dor"); se não existir, crie um que faça sentido — nunca um macete que distorça o conteúdo. O validador dá ❌ em card novo sem macete.
12. **Cards de digitar (`"tipo": "digitar"`) junto com flash/quiz:** **2 por anotação (no máximo 3)**, só quando houver conceito curto e recorrente (podem repetir a resposta de outro card — servem para fixar). Pergunta DIRETA e objetiva (termina em "?"), cuja resposta é curta e única: um nome, um número, uma droga, um valor de corte (`resposta` ≤ 6 palavras). Ponha em `aceitas` as outras formas certas (sinônimo, sigla, com/sem unidade). O `verso` segue o padrão do flash (1ª linha = a resposta em negrito + explicação em tópicos). Ex.: "Qual o limite de correção do sódio em 24 h?" → `resposta: "8 mmol/L"`, `aceitas: ["8", "8 meq/L", "8 a 10"]`.
13. **Prioridade (`prio`) em TODO card:** `"alta"` (tema frequente na UERJ, fundamental, conduta/critério/1ª linha, pegadinha recorrente), `"media"` (relevante, menos recorrente) ou `"baixa"` (detalhe específico, pouco provável). O app usa isso no filtro 🎯 Essenciais, na fila do dia (prioridade baixa só entra depois) e no modo véspera. Card que repete o que outro card já cobra (mesmo conhecimento com outra frase) **não deve ser criado** — **exceto card de digitar**: ele pode repetir a resposta de outro card, porque o objetivo dele é fixar pela digitação (a curadoria de 25/10 retirou 6 flash/quiz repetidos; cópia em `data/arquivo-curadoria.json`, que o app não lê).
14. **Antes de commitar, rode `python3 tools/validar.py`.** Se aparecer qualquer ❌, corrija e rode de novo. **Nunca commite com erro.** Corrija também os ⚠️ quando der (principalmente card sem visual).

## Rotina: transformar anotações em cards

1. Ler `data/notas.json`. **Ignore as anotações com `"manual": true`** (ela já mandou pelo chat). Se não sobrar nenhuma pendente, **parar sem commitar nada**.
2. Para cada anotação pendente, criar **POUCOS cards: só o mais recorrente e o mais necessário para a prova** (normalmente 1–2 por anotação, no máximo 3 se a anotação cobrir vários temas). Ela já tem 700+ cards e a prova é em dias — card a mais atrapalha. **O contexto/resumão do baralho continua COMPLETO**; o que fica enxuto são as perguntas dos cards (só o que cai e o que ela precisa saber de cor).
   - **Sem repetição:** antes de criar, procure em `data/cards.json` se o conteúdo já existe (mesmo assunto/mesma pergunta). Se já existe, NÃO crie de novo — crie só o que for novo (um detalhe, uma pegadinha, outro ângulo). Se a anotação não acrescenta nada, não crie card.
   - **Anotação curta** (só o nome do tema, ex.: "Classificação FIGO"): cubra o tema completo do jeito que ele cai em prova, deixando claro no card qual classificação é.
3. Acrescentar os cards ao fim do array `cards` em `data/cards.json` (nunca apagar nem reescrever cards existentes; `id` único).
4. Em `data/notas.json`: mover os `id` processados para `processadas` (manter só os últimos 300) e esvaziar `pendentes`. Isso faz o bloco de notas do app zerar sozinho.
5. Rodar `python3 tools/validar.py` (zero ❌; corrigir e repetir até passar), validar o JSON (`python3 -m json.tool`), commitar, fazer `git pull --rebase origin main` (o app também grava nesses arquivos) e dar push na `main`.

Anotações podem trazer imagens (`imgs`: caminhos como `data/img/1792...-0.jpg` no repositório — são prints que a Jacke colou). Abra cada imagem (Read) para entender o que ela anotou. Se a imagem for útil no card (questão, achado, tabela da prova), use-a direto: `{"tipo":"img","src":"data/img/...jpg","legenda":"..."}`.

Se uma anotação for ilegível ou não tiver conteúdo médico, ainda assim mova-a para `processadas` (não deixe travada) e não invente card.

## Pedido manual pelo chat

Às vezes ela cola no chat um texto que começa com **"Fazer cards agora — UERJ Cards"**, com as anotações e os `ids`. Nesse caso:
1. Anexe e clone `jaaacked-07/jaaackestude.uerj-cards` (add_repo com access "push"), faça `git pull`.
2. Crie os cards dessas anotações seguindo todas as regras deste arquivo (se houver imagens em `data/img/...`, abra-as).
3. Em `data/notas.json`, mova esses `ids` para `processadas` e tire-os de `pendentes`.
4. Rode `python3 tools/validar.py` (zero ❌), valide os JSONs, commit, `git pull --rebase origin main`, push.
5. Responda curto: quantos cards, em quais baralhos, e correções importantes. Diga que ela já pode tocar em **"Confirmar cards feitos"** no app (as anotações só somem quando ela confirma).

## Campos que o app grava (não mexer)

A Jacke edita, renomeia, favorita e oculta cards pelo app, e isso é gravado direto em `data/cards.json`:
`fav`, `oculto`, `minha` (texto dela no card; pode conter fotos coladas no formato `![](data/img/...jpg)` e anotações posicionadas em blocos `@@nota|n|início do trecho` — o app as mostra logo abaixo daquele trecho; se você reescrever esse trecho do card, a anotação cai no fim do card, então evite mexer em trecho que tem anotação dela) e `rev` (no topo do arquivo). Nunca altere nem remova esses campos, e nunca desfaça edições que ela fez em `frente`/`verso`/`tema`/`sub`.
Ao criar cards novos, **reutilize os nomes de `tema` e `sub` que já existem** no arquivo quando o assunto for o mesmo (ela pode ter renomeado). Nunca crie uma matéria ou assunto novo que seja variação de um existente (acento, abreviação, sinônimo, singular/plural: "Preventiva" = "Medicina Preventiva" = "Saúde Coletiva"; "Clínica" = "Clínica Médica"). Se a matéria que ela escreveu na anotação já existir com outro nome, use o nome que já existe.

## Organização: grande área → matéria → assunto

Cada card tem 3 níveis — o app mostra nessa ordem, abrindo conforme ela toca:
- `area` (grande área), sempre uma destas: **Cirurgia**, **Clínica Médica**, **Ginecologia**, **Obstetrícia**, **Medicina Preventiva**, **Pediatria**. (Ginecologia e Obstetrícia são áreas SEPARADAS desde o primeiro nível.)
- `tema` (matéria/sub-área dentro da área). **Clínica Médica usa SEMPRE uma destas sub-áreas, escritas exatamente assim:** Cardiologia, Dermatologia, Endocrinologia, Gastroenterologia, Hematologia, Infectologia, Nefrologia, Neurologia, Pneumologia, Psiquiatria, Reumatologia (o app já mostra todas). Outras áreas, ex.: Cirurgia → Abdome agudo, Trauma, Cirurgia vascular…; Medicina Preventiva → Vigilância em Saúde, Atenção Primária, Epidemiologia, SUS…; Pediatria → Neonatologia, Infectologia pediátrica…
- `sub` (assunto = **baralho**). Baralhos são **abrangentes**: um baralho por doença/tema grande, com tudo dele dentro (quadro, diagnóstico, classificação, conduta). **Nunca** separe por aspecto ("Apendicite — sinais", "Apendicite — diagnóstico" ✗). Exemplos ✓: "Abdome agudo inflamatório — Apendicite", "Câncer de colo do útero", "Mama — nódulo, BI-RADS e rastreamento", "Sofrimento fetal crônico", "Sofrimento fetal agudo — CTG" (tudo de cardiotocografia vai para esse).
- Ela também cria baralhos vazios pelo app para organizar: estão em `data/progresso.json` → `decks` (`{area, tema, sub, subt?}`). **Leia (sem editar) e use esses baralhos** quando o assunto couber neles.
- **Subtema (`subt`, opcional) = 4º nível, DENTRO de um baralho.** Ela organiza assim: baralho "Doenças Tubulointersticiais" → subtemas "NTA Necrose Tubular Aguda", "Necrose de papila"… Se o assunto da anotação for um subtema de um baralho que já existe (dela ou do arquivo), use o MESMO `sub` e ponha o subtema em `subt` — nunca crie baralho "Baralho - Subtema" separado. O contexto continua um só por baralho (`sub`).

**Ginecologia e Obstetrícia são ÁREAS separadas** (nunca "GO" nem "Ginecologia e Obstetrícia"). Gestação, parto, puerpério, pré-natal, abortamento, vitalidade fetal e doenças da gravidez → área Obstetrícia (matérias ex.: Pré-natal, Vitalidade fetal, Parto e puerpério, Hemorragias da gestação, Síndromes hipertensivas, Prematuridade e RPMO). O resto → área Ginecologia (matérias ex.: Oncologia ginecológica, Mastologia, Sangramento uterino, Climatério, Infecções genitais, Reprodução humana, Uroginecologia).

**Antes de criar, olhe as áreas/matérias/assuntos que já existem em `data/cards.json` e reutilize os nomes exatos.** Nunca crie variação de um nome existente (acento, sigla, sinônimo, singular/plural). Se ela já tiver renomeado algo, use o nome que está no arquivo.

## Qualidade do conteúdo

- **SEMPRE INFORMAÇÕES ATUALIZADAS E BIBLIOGRAFIA DA UERJ.** Antes de escrever, confira o conteúdo na versão **vigente** das fontes:
  - a bibliografia/conteúdo programático do edital da UERJ/CEPUERJ em vigor (página oficial: https://www.cepuerj.uerj.br — Residência Médica 2027), quando o edital trouxer;
  - os livros-texto de referência que a UERJ usa e as diretrizes/protocolos brasileiros atuais (Ministério da Saúde/PCDT, FEBRASGO, SBP, SBC, SBD, SBEM, Diretrizes AMB etc.) e internacionais quando forem o padrão (ex.: FIGO, ACOG, GOLD, GINA, KDIGO, ADA).
  - Se uma diretriz mudou (nova portaria, nova classificação, nova meta), use a versão nova e, se a mudança for cobrável, cite em `pegadinha` o que mudou. Coloque em `fonte` o nome e o ano da fonte usada.
  - Nunca invente fonte, ano, portaria ou referência. Na dúvida, pesquise (WebSearch) antes de afirmar.
- **FOCO NA PROVA DA UERJ.** Escreva pensando em como a UERJ cobra o tema (recorte, nível de detalhe, tipo de enunciado). Português do Brasil, linguagem direta.
- **Sempre que der:** `pegadinha` (o detalhe que derruba) e `uerj` (o que a UERJ costuma cobrar daquele tema — ex.: "cobra mais caso clínico com conduta do que o nome do estádio"). Para saber o que a UERJ cobra, use o histórico de provas (o app Foco UERJ dela está no repositório jaaacked-07/jaaackestude.prevalenciaUERJ, se estiver acessível) e o seu conhecimento das provas; não invente frequência que não conhece.
- As questões `quiz` devem imitar o estilo UERJ: caso clínico curto, 4 alternativas (A–D), uma pegadinha plausível entre os distratores.
- Corrigir o que a anotação tiver de errado; conferir fatos duvidosos (portarias, doses, classificações) na fonte oficial vigente antes de escrever.
- Frente curta e objetiva.
- **Verso direto, mas BEM EXPLICADO e SEMPRE ESTRUTURADO** (ela não suporta texto corrido, uma frase atrás da outra):
  - 1ª linha: a resposta direta, com o termo-chave em `**negrito**`. **Todo card flash começa assim**: o app mostra esse 1º bloco em DESTAQUE como "resposta para lembrar"; o que vem depois da linha em branco aparece como explicação. **Uma ideia por linha** também no destaque (ex.: `**Nissen → 360° posterior**\n**Toupet → 270° posterior**`). Se a resposta for uma lista: `**Título:**` + tópicos `- ` no mesmo bloco.
  - Linha em branco (`\n\n`) e depois a explicação em **tópicos** (linhas começando com `- `), uma ideia por linha.
  - Mudou de assunto/definição dentro do card (ex.: "Por quê:", "Conduta:", "Via:") → nova linha em branco + rótulo curto + tópicos.
  - Cada item de classificação em sua própria linha: `- **IIA** → ...` / `- **IIB** → ...`.
  - Detalhe de um item → subtópico recuado com 2 espaços: `  - IIA1 → ≤ 4 cm`. Nunca separe itens com `·` na mesma linha.
  - O app entende: cada linha = uma linha; `- ` = tópico; `**texto**` = destaque; `__texto__` = sublinhado; `{v}texto{/v}` = vermelho (marcas sempre dentro da MESMA linha). Nunca junte várias definições numa frase só.
  - Exemplo:
    `**Sinal do Psoas.**\n\n- O apêndice retrocecal encosta no psoas.\n- Estender a coxa direita estira o músculo → dói.`
- **ESCORES SEMPRE DESTRINCHADOS.** Nunca só cite um escore/classificação com pontuação (Alvarado, Apgar, Manning, Glasgow, Bishop, Silverman, Wells, CURB-65, Child-Pugh etc.). Sempre que um escore aparecer (no verso ou no contexto), mostre: cada item, quantos pontos vale, o total e a interpretação/conduta por faixa — em tabela (`Item | Pontos`) + faixas em tópicos. Se o baralho ainda não tem um card do escore, crie um.
- **Nada repetido entre verso e tabela/visual.** Se a tabela (ou lista, fluxo, vs) já mostra os itens, o verso traz só a resposta direta e o que a tabela NÃO tem (o porquê, a lógica, a pegadinha). Se não precisa de explicação teórica, o verso fica só com a 1ª linha e a tabela faz o resto. Se o verso é mais completo que o visual, tire o visual.
- **Sempre que possível, uma ilustração** em `visual`. Só deixe sem quando não houver nada visual que ajude. Layout limpo: a Jacke é visual e se cansa com excesso.
- **IMAGEM REAL TEM PRIORIDADE** sobre desenho: achado de exame, foto clínica, peça, lâmina, radiografia, ECG, anatomia, dermatologia, sinais semiológicos etc. → use `{"tipo":"img"}` com imagem real. **Não desenhe em SVG algo que existe como imagem real.**
- Tabela, fluxograma, comparação (`vs`), lista e grupos você pode e deve criar. SVG só para esquema conceitual que não existe como foto (ex.: mapa de estadiamento).
- Use `pegadinha` para o ponto que a banca usa para derrubar.
- Pelo menos 1 `quiz` por baralho (estilo prova, 4 alternativas, comentário para cada uma); quando a anotação vier de uma questão, faça o quiz a partir dela.

## Contexto do tema (em TODO card)

Todo card leva o campo **`contexto`**: um resumo do que **ENVOLVE** o tema, para ela se contextualizar — não só do detalhe que a pergunta cobra.
- Ex.: pergunta sobre notificação imediata → o contexto explica notificação compulsória como um todo (o que é, prazos imediata × semanal, exemplos de semanais e imediatas, para quem notificar).
- Ex.: pergunta sobre DIP tardia → o contexto explica a CTG inteira (linha de base, variabilidade, acelerações, tipos de DIP, categorias, conduta).
- **Um contexto por baralho**: todos os cards do mesmo baralho recebem o MESMO texto. As marcações (marca-texto) e as anotações que ela faz dentro do contexto (valem para todos os cards que mostram aquele contexto) ficam presas à **1ª linha** do contexto: ao ampliar um contexto existente, **nunca mude a 1ª linha** (só acrescente/edite as de baixo), senão ela perde as marcações. Se o baralho já tem contexto, reutilize (pode ampliar com o que faltar e atualizar em todos os cards do baralho).
- Estruturado como o verso (1ª linha em negrito com a definição; blocos com rótulo e tópicos `- `), direto e sem enrolação.
- **É o RESUMÃO do tema inteiro, para relembrar:** explique de forma direta o tema como um todo — o que é (definição/fisiopatologia em 1–2 linhas), clínica, diagnóstico, classificação (se houver), tratamento/conduta e complicações — até chegar no recorte da UERJ. Ex.: card sobre a classificação de Los Angeles → o contexto resume a esofagite de refluxo inteira (o que é, clínica, diagnóstico, tratamento, complicações). Use rótulos curtos (`O que é:`, `Clínica:`, `Diagnóstico:`, `Tratamento:`…) só para os blocos que o tema tiver.
- **Profundidade com foco UERJ:** o contexto tem que trazer o que a UERJ realmente cobra do tema, já destrinchado (ex.: meningite → a diferença do líquor bacteriana × viral × tuberculosa × fúngica). Use o Foco UERJ (repositório jaaacked-07/jaaackestude.prevalenciaUERJ: temas, pontos cobrados e pegadinhas de 2022–2026) e a diretriz vigente. Contexto raso é erro.
- **Termina com o bloco `O que mais cai na UERJ:`** (no FINAL, depois da explicação): tópicos curtos com o que a banca cobra e as pegadinhas recorrentes.
- **Nada repetido:** o que já está na explicação, no `ctxvisual` ou nos cards do baralho não se repete no contexto (ex.: se a tabela do líquor é o `ctxvisual`, o texto não repete a tabela; o bloco final só aponta o que cai).
- **Hierarquia obrigatória também no contexto** (igual ao verso): rótulo do bloco numa linha terminando em `:`; cada item numa linha própria `- **termo** → explicação`; detalhes de um item como subtópico recuado (`  - ` com 2 espaços).
- **Nunca** junte vários itens numa linha com `·`, `;` ou `/` (✗ `- 0 → completar · 1/2 → rotina · 3 → controle`). Uma ideia por linha.
- O app mostra no fim da explicação, num quadro próprio. Não use mais o campo `resumo`.
- **Todo baralho tem `ctxvisual`** (imagens/ilustrações SEMPRE que der, no contexto e no card): imagem real do tema quando existir; senão um esquema SVG que ilustre (não uma tabela que repita o texto). Mesmo formato de `visual`, igual em todos os cards do baralho; aparece dentro do contexto. Baralho novo → crie o `ctxvisual`; baralho existente → reutilize.
- **Não copie as anotações dela (`minha`) para o contexto**, a não ser que ela peça. Blocos que já existem começando com "Minha anotação" são texto dela: nunca apague nem reescreva.

## Formato de um card

```json
{
  "id": "tema-curto-07",            // único
  "tipo": "flash",                  // "flash", "quiz" ou "digitar"
  "area": "Medicina Preventiva",    // grande área (ver lista acima)
  "tema": "Vigilância em Saúde",    // matéria
  "sub": "Notificação imediata",    // assunto = baralho (vira filtro no app)
  "subt": "Prazos",                 // opcional: subtema dentro do baralho
  "frente": "Pergunta",
  "verso": "Resposta curta",        // só flash
  "opcoes": ["A", "B", "C", "D"],   // só quiz
  "certa": 1,                       // só quiz (índice 0-based)
  "resposta": "8 mmol/L",           // só digitar: o que ela digita (curto)
  "aceitas": ["8", "8 meq/L"],      // só digitar: outras formas aceitas (opcional)
  "macete": "texto curto",          // OBRIGATÓRIO em card novo: mnemônico/associação
  "comentarios": ["...", "...", "...", "..."], // só quiz, um por alternativa
  "visual": { ... },                // opcional
  "pegadinha": "texto",             // opcional (use sempre que der)
  "uerj": "como a UERJ cobra isso",  // opcional (use sempre que der)
  "contexto": "resumo do tema amplo",  // obrigatório (igual para o baralho todo)
  "ctxvisual": { ... },             // obrigatório: ilustração do contexto (igual para o baralho todo)
  "fonte": "Portaria X / comentário UERJ",
  "add": "AAAA-MM-DD"               // data de hoje
}
```

### Tipos de `visual`

- Tabela: `{"tipo":"tabela","cab":["Sinal","Como","Sugere"],"linhas":[["Psoas","...","..."]]}`
- Fluxograma: `{"tipo":"fluxo","passos":["Passo 1","Passo 2",["Ramo A","Ramo B"]]}` (array interno = ramos lado a lado)
- Comparação: `{"tipo":"vs","a":{"t":"X","itens":["..."]},"b":{"t":"Y","itens":["..."]}}`
- Lista: `{"tipo":"lista","itens":["item","!item destacado"]}` (`!` no início = destaque; também vale numa célula de tabela)
- Grupos: `{"tipo":"grupos","grupos":[{"t":"Grupo","itens":["a","b"]}]}`

- Desenho SVG: `{"tipo":"svg","svg":"<svg viewBox=...>...</svg>","legenda":"..."}` — use as cores do app por variável CSS (`var(--wine)`, `var(--rose)`, `var(--rose-soft)`, `var(--ink)`, `var(--mute)`, `var(--line)`, `var(--card)`) para funcionar no modo escuro; sem fontes externas.
- Imagem real: `{"tipo":"img","src":"https://upload.wikimedia.org/...","legenda":"...","fonte":"Wikimedia Commons · autor/licença"}` — use imagens de licença livre (Wikimedia Commons, Open-i/PMC com licença aberta, CDC PHIL). Como achar e montar a URL (o acesso direto ao Wikimedia pode estar bloqueado no ambiente):
  1. WebSearch com `commons.wikimedia.org File: <termo em inglês>` para achar o nome exato do arquivo (ex.: `Diagram_showing_stage_2B_cervical_cancer_CRUK_216.svg`).
  2. Monte a URL: `h = md5(nome_com_underscores)`. Miniatura (fotos grandes e SVG): `https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[0:2]}/{nome}/600px-{nome}` (+ `.png` no fim se o arquivo for `.svg`). Se a imagem original puder ter menos de 600 px de largura, use o arquivo original: `https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[0:2]}/{nome}` (miniatura maior que o original dá erro).
  3. Se conseguir abrir a URL ou a página do arquivo, confira que a imagem mostra o que a legenda diz. Se a imagem falhar, o app simplesmente a esconde.
- Vários visuais no mesmo card: `"visual": [ {...}, {...} ]`.

SVG: textos com no mínimo 8,5 de tamanho, `viewBox` com até ~340 de largura (cabe no celular) e sem texto saindo da área.

Escolha o formato pelo conteúdo: critérios/comparação de várias colunas → tabela; conduta/algoritmo → fluxo; X versus Y → vs; enumeração → lista ou grupos.

## Como o app usa os cards (para entender as prioridades)

- **Fila do dia:** todos os cards errados que venceram + **15 novos** + pelo menos 5 revisões, completando 20 (passa de 20 se houver muito erro).
- **Prioridade:** quanto o baralho cai na UERJ (`data/prevalencia.json`) + se o card está fraco + quantas vezes ela errou + favorito/marca-texto + atraso. Os baralhos são intercalados (não vêm 10 cards seguidos do mesmo tema).
- **Fraco** = errou ou marcou "Quase" e ainda não acertou 3× seguidas. **Sanguessuga** = errou 4 ou mais vezes.
- **Modo véspera** (30–31/10): sanguessugas, fracos, favoritos, marcados e o que mais cai na UERJ, sem novos.
- Revisão comprimida até a prova: nenhum intervalo passa da metade dos dias que faltam; nada fica para depois de 31/10.
