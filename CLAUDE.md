# UERJ Cards — instruções para o Claude

App PWA de flashcards/quiz da Jacke (interna de medicina) para a prova de residência da **UERJ (01/11/2026)**.
Publicado via GitHub Pages: https://jaaacked-07.github.io/jaaackestude.uerj-cards/

- `index.html` — app inteiro (não mexer ao gerar cards).
- `data/cards.json` — todos os cards. O app lê esse arquivo toda vez que abre.
- `data/notas.json` — anotações que a Jacke guarda no app (vão sozinhas para cá).
- `data/progresso.json` — progresso dela sincronizado entre aparelhos. **Nunca editar.**
- `data/chave.json` — acesso do app criptografado com o usuário dela. **Nunca editar nem apagar.**

## Rotina: transformar anotações em cards

1. Ler `data/notas.json`. Se `pendentes` estiver vazio, **parar sem commitar nada**.
2. Para cada anotação pendente, criar cards (normalmente 2–5 por questão/tema; mais se a anotação cobrir vários temas — separe por tema).
   - **Sem repetição:** antes de criar, procure em `data/cards.json` se o conteúdo já existe (mesmo assunto/mesma pergunta). Se já existe, NÃO crie de novo — crie só o que for novo (um detalhe, uma pegadinha, outro ângulo). Se a anotação não acrescenta nada, não crie card.
   - **Anotação curta** (só o nome do tema, ex.: "Classificação FIGO"): cubra o tema completo do jeito que ele cai em prova, deixando claro no card qual classificação é.
3. Acrescentar os cards ao fim do array `cards` em `data/cards.json` (nunca apagar nem reescrever cards existentes; `id` único).
4. Em `data/notas.json`: mover os `id` processados para `processadas` (manter só os últimos 300) e esvaziar `pendentes`. Isso faz o bloco de notas do app zerar sozinho.
5. Validar o JSON (`python3 -m json.tool`), commitar, fazer `git pull --rebase origin main` (o app também grava nesses arquivos) e dar push na `main`.

Se uma anotação for ilegível ou não tiver conteúdo médico, ainda assim mova-a para `processadas` (não deixe travada) e não invente card.

## Campos que o app grava (não mexer)

A Jacke edita, renomeia, favorita e oculta cards pelo app, e isso é gravado direto em `data/cards.json`:
`fav`, `oculto`, `minha` (texto dela no card) e `rev` (no topo do arquivo). Nunca altere nem remova esses campos, e nunca desfaça edições que ela fez em `frente`/`verso`/`tema`/`sub`.
Ao criar cards novos, **reutilize os nomes de `tema` e `sub` que já existem** no arquivo quando o assunto for o mesmo (ela pode ter renomeado). Nunca crie uma matéria ou assunto novo que seja variação de um existente (acento, abreviação, sinônimo, singular/plural: "Preventiva" = "Medicina Preventiva" = "Saúde Coletiva"; "Clínica" = "Clínica Médica"). Se a matéria que ela escreveu na anotação já existir com outro nome, use o nome que já existe.

## Matérias (`tema`)

Use sempre uma destas, escritas exatamente assim: **Cirurgia**, **Clínica Médica**, **Ginecologia**, **Obstetrícia**, **Pediatria**, **Preventiva**, **Psiquiatria**.
**Ginecologia e Obstetrícia são matérias SEPARADAS** — nunca use "GO" nem "Ginecologia e Obstetrícia". Gestação, parto, puerpério, pré-natal, abortamento e doenças da gravidez → Obstetrícia. Tudo fora do ciclo gravídico-puerperal (ciclo menstrual, contracepção, climatério, infecções genitais, mama, oncologia ginecológica, uroginecologia) → Ginecologia. Se ela já tiver renomeado uma matéria, use o nome que está no arquivo.

## Qualidade do conteúdo

- Português do Brasil, linguagem direta, foco em **acertar questão de prova** (UERJ, ENARE, SES-RJ).
- Corrigir o que a anotação tiver de errado; conferir fatos duvidosos (portarias, doses, classificações) na fonte oficial vigente antes de escrever.
- Frente curta e objetiva.
- **Verso direto, mas BEM EXPLICADO:** comece com a resposta em uma frase e depois explique o porquê (mecanismo, lógica, como a banca cobra) em 2–4 frases. Pode usar parágrafos separados por linha em branco (`\n\n`).
- **Sempre que possível, uma ilustração** em `visual`: imagem real, desenho SVG, tabela, fluxograma, comparação etc. Só deixe sem quando não houver nada visual que ajude. Layout limpo: a Jacke é visual e se cansa com excesso.
- Use `pegadinha` para o ponto que a banca usa para derrubar.
- Inclua pelo menos 1 `quiz` (estilo prova, 4 alternativas, comentário para cada uma) por tema quando a anotação vier de uma questão.

## Formato de um card

```json
{
  "id": "tema-curto-07",            // único
  "tipo": "flash",                  // "flash" ou "quiz"
  "tema": "Preventiva",             // matéria (ver lista abaixo)
  "sub": "Notificação imediata",    // assunto (vira filtro no app)
  "frente": "Pergunta",
  "verso": "Resposta curta",        // só flash
  "opcoes": ["A", "B", "C", "D"],   // só quiz
  "certa": 1,                       // só quiz (índice 0-based)
  "comentarios": ["...", "...", "...", "..."], // só quiz, um por alternativa
  "visual": { ... },                // opcional
  "pegadinha": "texto",             // opcional
  "fonte": "Portaria X / comentário UERJ",
  "add": "AAAA-MM-DD"               // data de hoje
}
```

### Tipos de `visual`

- Tabela: `{"tipo":"tabela","cab":["Sinal","Como","Sugere"],"linhas":[["Psoas","...","..."]]}`
- Fluxograma: `{"tipo":"fluxo","passos":["Passo 1","Passo 2",["Ramo A","Ramo B"]]}` (array interno = ramos lado a lado)
- Comparação: `{"tipo":"vs","a":{"t":"X","itens":["..."]},"b":{"t":"Y","itens":["..."]}}`
- Lista: `{"tipo":"lista","itens":["item","!item destacado"]}` (`!` no início = destaque)
- Grupos: `{"tipo":"grupos","grupos":[{"t":"Grupo","itens":["a","b"]}]}`

- Desenho SVG: `{"tipo":"svg","svg":"<svg viewBox=...>...</svg>","legenda":"..."}` — use as cores do app por variável CSS (`var(--wine)`, `var(--rose)`, `var(--rose-soft)`, `var(--ink)`, `var(--mute)`, `var(--line)`, `var(--card)`) para funcionar no modo escuro; sem fontes externas.
- Imagem real: `{"tipo":"img","src":"https://upload.wikimedia.org/...","legenda":"...","fonte":"Wikimedia Commons"}` — só imagens de licença livre com URL direta conferida (abrir a URL antes de usar).
- Vários visuais no mesmo card: `"visual": [ {...}, {...} ]`.

Escolha o formato pelo conteúdo: critérios/comparação de várias colunas → tabela; conduta/algoritmo → fluxo; X versus Y → vs; enumeração → lista ou grupos.
