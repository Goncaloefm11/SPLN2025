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

- `TP1/scr/tokeniz.py` — script principal que orquestra o processamento: lê os ficheiros de texto, extrai as 3 frases mais relevantes (via `paragrafos.py`), executa NER e Matcher, e chama o gerador LaTeX.
- `TP1/scr/paragrafos.py` — lógica de scoring: limpeza básica, construção de bigramas e pontuação para selecionar as 3 melhores.
- `TP1/scr/gera_latex.py` — monta e escreve os ficheiros `.tex` com o título, abstract (as frases), secção NER e tabela de matches.
- `TP1/scr/*.txt` — ficheiros de origem (`harry.txt`, `submarino.txt`, `palhaco.txt`), tendo estes ficheiros ter de ser escritos dentro da lista presente no `tokeniz.py` -> (`livros = ['harry.txt', 'submarino.txt', 'palhaco.txt']`).
- `TP1/scr/artigo_NOME_DO_LIVRO.pdf` — PDFs gerados a partir dos `.tex` (quando compilados).
- `TP1/spln26tp1.pdf` — PDF do trabalho

---

## Instalação

```zsh
# instalar spaCy
pip install -U pip
pip install spacy

# instalar o modelo pt
python -m spacy download pt_core_news_sm
pdftotext livros.pdf 
```

Observação: Deverá fazer previamente a conversão do pdf em questao para a extensão .txt como mostra em baixo:

```zsh
pdftotext harry.pdf
pdftotext submarino.pdf
pdftotext palhaco.pdf  
```

---

## Como executar o pipeline

Execute o processamento (script principal):

```zsh
python3 tokeniz.py
```

Isto vai:
- abrir cada ficheiro de texto listado em `tokeniz.py` (`harry.txt`, `submarino.txt`, `palhaco.txt`),
- extrair as 3 frases mais relevantes,
- executar o spaCy NER e o Matcher com os padrões definidos em `tokeniz.py`,
- gerar um ficheiro `.tex` por fonte usando `gera_latex.py`.

---

## Saída esperada

- Para cada ficheiro de entrada é gerado `artigo_<nome>.tex`.
- O `.tex` contém:
  - Título, autor e data;
  - Abstract com as 3 frases selecionadas;
  - Secção de Entidades Nomeadas (NER);
  - Secção com uma tabela contendo os matches do spaCy Matcher;
  - Bibliografia (entrada simples com a referência do ficheiro de origem).

```zsh
pdflatex artigo_harry.tex
pdflatex artigo_submarinoy.tex
pdflatex artigo_palhaco.tex
```
Será então criado um pdf para esse ficheiro latex de entrada que mostrará a saida esperada mencionada em cima.

---

## Contacto | Autor

pg61524@uminho.pt | Gonçalo Magalhães — autor do código

