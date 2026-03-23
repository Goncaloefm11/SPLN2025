import spacy
from spacy.matcher import Matcher
from paragrafos import obter_3_melhores_frases
from gera_latex import gerar_artigo_latex
import os

# 1. Carregar o modelo
nlp = spacy.load("pt_core_news_sm")

# Explicação: Procura um Nome Próprio seguido de qualquer Verbo.
pattern_simples = [
    {"POS": "PROPN", "OP": "+"},  # Um ou mais Nomes Próprios (ex: Harry, Clark)
    {"POS": "VERB"}               # Seguido de um Verbo (ex: disse, correu, olhou)
]

# Explicação: Procura um Verbo seguido de um Substantivo.
pattern_posse = [
    {"POS": "VERB"},                # Um verbo qualquer
    {"POS": "DET", "OP": "?"},  # Um artigo opcional (o, a, um)
    {"POS": "NOUN"}                 # Um substantivo (coisa/objeto)
]

# Explicação: Verbo seguido de preposição e local.
# Exemplo: "entrou no castelo", "foi para a sala"
pattern_movimento = [
    {"POS": "VERB"},              # O verbo de movimento
    {"POS": "ADP"},               # A preposição (em, de, para)
    {"POS": "DET", "OP": "?"},    # Artigo opcional
    {"POS": "NOUN"}               # O destino/local
]

# 2. Definir o Matcher e o Padrão FORA do loop
matcher = Matcher(nlp.vocab)
matcher.add("ACAO", [pattern_simples])
matcher.add("OBJETO", [pattern_posse])
matcher.add("MOVIMENTO", [pattern_movimento])

livros = ['harry.txt', 'submarino.txt', 'palhaco.txt']

for livro in livros:
    print(f"\n--- PROCESSANDO: {livro} ---")
    try:
        with open(livro, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"Erro: Ficheiro {livro} não encontrado.")
        continue
    
    # Obter a lista de 3 frases
    frases_escolhidas = obter_3_melhores_frases(conteudo)

    matches_do_livro = []
    for frase in frases_escolhidas:
        doc_frase = nlp(frase)
        res_matches = matcher(doc_frase)
        
        for match_id, start, end in res_matches:
            nome_match = nlp.vocab.strings[match_id]
            texto_match = doc_frase[start:end].text
            matches_do_livro.append((nome_match, texto_match))

    # NER no texto original
    doc_completo = nlp(conteudo[:10000])
    entidades_encontradas = [(ent.text, ent.label_) for ent in doc_completo.ents]

    # 3. Gerar o Artigo LaTeX
    gerar_artigo_latex(livro, frases_escolhidas, entidades_encontradas, matches_do_livro)

    print("\nAs 3 frases escolhidas:")
    for i, frase in enumerate(frases_escolhidas, 1):
        print(f"{i}. {frase}")
        
        #Processar cada frase individualmente
        doc_frase = nlp(frase) 
        matches = matcher(doc_frase)
        
        for match_id, start, end in matches:
            nome_match = nlp.vocab.strings[match_id]
            print(f"   [{nome_match}]: {doc_frase[start:end].text}")