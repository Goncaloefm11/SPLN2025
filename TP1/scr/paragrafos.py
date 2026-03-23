import spacy
import re
from collections import Counter

nlp = spacy.load("pt_core_news_sm")

def obter_3_melhores_frases(texto_completo):
    texto_limpo = re.sub(r'=+', '', texto_completo)
    texto_limpo = re.sub(r'Conteúdo disponível em Le Livros', '', texto_limpo, flags=re.IGNORECASE)
    
    doc = nlp(texto_limpo)
    
    # 1. Criar modelo de Bigramas (ignora pontuação e stop words para melhor score)
    bigramas_texto = []                             #ignora virgulas.   determinantes (a, o, de...)
    tokens_uteis = [t.lemma_.lower() for t in doc if not t.is_punct and not t.is_stop and len(t.text) > 1]
    
    #exemplo: harry usa varinha 
    #harry usa tokens_uteis[0]
    #usa varinha tokens_uteis[0+1]
    for i in range(len(tokens_uteis) - 1):
        bigramas_texto.append((tokens_uteis[i], tokens_uteis[i+1]))
    
    contagem_bigramas = Counter(bigramas_texto)
    
    # 2. Pontuar cada frase real
    pontuacao_frases = []
    for sent in doc.sents:
        texto_sent = sent.text.strip()
        if len(texto_sent) < 200 or "Le Livros" in texto_sent:
            continue
            
        score = 0
        tokens_sent = [t.lemma_.lower() for t in sent if not t.is_punct and not t.is_stop]
        
        for i in range(len(tokens_sent) - 1):
            bi = (tokens_sent[i], tokens_sent[i+1])
            score += contagem_bigramas[bi]
        
        # Média do score pelo tamanho da frase
        if tokens_sent:
            pontuacao_frases.append((texto_sent, score / len(tokens_sent)))

    # 3. Retornar as 3 com maior score
    melhores = sorted(pontuacao_frases, key=lambda x: x[1], reverse=True)
    return [f[0] for f in melhores[:3]]