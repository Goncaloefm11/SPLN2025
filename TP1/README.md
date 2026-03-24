# TP1 — Processamento e Análise de Texto (SPLN)

## Enunciado
Escolha um conjunto de pelo menos 3 fontes sobre um tema do seu interesse (e.g.: Processamento de Linguagem
Natural). Deve utilizar p ́aginas web e documentos em pdf. O trabalho pr ́atico consiste em processar o texto dessas
fontes e selecionar para cada uma das fontes as “3 frases escolhidas” do texto. Dever ́a apresentar cada texto como
um artigo latex e adicionar as frases escolhidas usando o ambiente itemize dentro do abstract. Para selecionar as trˆes
frases dever ́a utilizar um modelo de linguagem baseado em “n-grams” e deve seguir os seguintes passos:
- Recolher e limpar o texto das fontes escolhidas.
- Deve tokenizar o texto e construir um modelo de linguagem baseado em “n-grams”.
- Escolher um m ́etodo de scoring para as frases do texto. Ou seja cada aluno tem a liberdade para definir como vai
usar o modelo de “n-grams” para selecionar as frases escolhidas do texto.
- Use a ferramenta spaCy para fazer NER analysis e identificar as entidades nomeadas presentes no texto.
- Produza um artigo latex para cada fonte, apresentando as frases escolhidas no abstract e as entidades nomeadas
identificadas no texto da fonte original incluido no corpo do LATEX. Lembre-se de citar a fonte na bibliografia do
artigo.
- O resultado final deve conter os 3 pdfs gerados a partir de cada fonte.
1

---

## Estrutura relevante

- `TP1/run_all.py` — **script de orquestração** que executa todo o pipeline automaticamente: gera os `.tex` e compila para PDF.
- `TP1/tokeniz.py` — script principal que processa o texto: lê os ficheiros, extrai as 3 frases mais relevantes (via `paragrafos.py`), executa NER e Matcher, e chama o gerador LaTeX.
- `TP1/paragrafos.py` — lógica de scoring: limpeza básica, construção de bigramas e pontuação para selecionar as 3 melhores.
- `TP1/gera_latex.py` — monta e escreve os ficheiros `.tex` com o título, abstract (as frases), secção NER e tabela de matches.
- `TP1/web_extractor.py` — extrai texto de páginas web (para as fontes online).
- `TP1/*.txt` — ficheiros de origem (`harry.txt`), sendo este ficheiro listado em `tokeniz.py` -> (`fontes = ['harry.txt', 'https://pt.wikipedia.org/wiki/J._K._Rowling', '...']`).
- `TP1/artigo_*.tex` — ficheiros LaTeX gerados automaticamente.
- `TP1/artigo_*.pdf` — PDFs gerados a partir dos `.tex` (compilados automaticamente).
- `TP1/trabalho/spln26tp1.pdf` — PDF do trabalho

---

## Instalação

```zsh
# instalar spaCy
pip install -U pip
pip install spacy


# instalar o modelo pt
python -m spacy download pt_core_news_sm
```

## Como executar o pipeline
### Opção 1:

Execute o script que faz tudo automaticamente:

```zsh
cd TP1/scr
# passar o pdf para .text primeiramente
pdftotext harry.pdf

# executar o script
python3 run_all.py
```

Isto vai:
- executar `tokeniz.py` para processar todas as fontes,
- gerar automaticamente os 3 ficheiros `.tex`,
- compilar cada `.tex` para PDF usando `pdflatex`,
- remover ficheiros temporários,
- mostrar um resumo final com os PDFs gerados.

### Opção 2: Manual

Se preferires executar passo a passo:

```zsh
# 1. Executar o processamento
python3 tokeniz.py

# 2. Compilar cada .tex para PDF
pdflatex artigo_harry.txt.tex
pdflatex artigo_pt_wikipedia_org_wiki_J__K__Rowling.tex
pdflatex artigo_pt_wikipedia_org_wiki_Literatura_fant_C3_A1stica.tex
```

---

## Saída esperada

Após executar `python3 run_all.py`, serão gerados:

- **3 ficheiros `.tex`** com o conteúdo:
  - Título, autor e data;
  - Abstract com as 3 frases selecionadas;
  - Secção de Entidades Nomeadas (NER);
  - Secção com uma tabela contendo os matches do spaCy Matcher;
  - Bibliografia (com referência da fonte).

- **3 ficheiros `.pdf`** compilados automaticamente, prontos para visualizar.

Exemplo de output do script:
```

tokeniz.py executado com sucesso!

3 ficheiros .tex encontrados:
   - artigo_harry.txt.tex
   - artigo_pt_wikipedia_org_wiki_J__K__Rowling.tex
   - artigo_pt_wikipedia_org_wiki_Literatura_fant_C3_A1stica.tex

Ficheiros .tex gerados: 3
Ficheiros compilados com sucesso: 3

Todos os ficheiros foram processados com sucesso!
   PDFs gerados:
   - artigo_harry.txt.pdf
   - artigo_pt_wikipedia_org_wiki_J__K__Rowling.pdf
   - artigo_pt_wikipedia_org_wiki_Literatura_fant_C3_A1stica.pdf
```

---

## Contacto | Autor

pg61524@uminho.pt | Gonçalo Magalhães — autor do código

