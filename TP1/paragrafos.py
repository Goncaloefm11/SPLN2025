import spacy
import re
from collections import Counter

nlp = spacy.load("pt_core_news_sm")

def obter_3_melhores_frases(texto_completo):
    # Limpeza inicial básica
    texto_limpo = re.sub(r'=+', '', texto_completo)
    texto_limpo = re.sub(r'Conteúdo disponível em Le Livros', '', texto_limpo, flags=re.IGNORECASE)
    
    doc = nlp(texto_limpo)
    
    # 1. Criar modelo de Bigramas
    bigramas_texto = []
    tokens_uteis = [t.lemma_.lower() for t in doc if not t.is_punct and not t.is_stop and len(t.text) > 1]
    
    for i in range(len(tokens_uteis) - 1):
        bigramas_texto.append((tokens_uteis[i], tokens_uteis[i+1]))
    
    contagem_bigramas = Counter(bigramas_texto)
    
    # 2. Pontuar cada frase real com filtros de qualidade
    pontuacao_frases = []
    for sent in doc.sents:
        texto_sent = sent.text.strip()
        
        # Filtro A: Ignorar se a frase for muito curta ou longa demais para um resumo
        if len(texto_sent) < 200 or len(texto_sent) > 500:
            continue

        # Filtro B: Ignorar listas de lixo (muitos números ou colchetes, típico de índices)
        # Se mais de 15% da frase forem dígitos ou [], provavelmente não é uma frase natural
        lixo = len(re.findall(r'[0-9\[\]]', texto_sent))
        if lixo > len(texto_sent) * 0.15:
            continue

        # OBRIGATÓRIO ter pelo menos um Verbo (VERB) ou Auxiliar (AUX)
        # Isso garante que os teus padrões de AÇÃO ou MOVIMENTO funcionem no LaTeX
        tem_verbo = any(t.pos_ in ["VERB", "AUX"] for t in sent)
        if not tem_verbo:
            continue
            
        score = 0
        tokens_sent = [t.lemma_.lower() for t in sent if not t.is_punct and not t.is_stop]
        
        for i in range(len(tokens_sent) - 1):
            bi = (tokens_sent[i], tokens_sent[i+1])
            score += contagem_bigramas[bi]
        
        # Média do score pelo tamanho da frase para não beneficiar apenas frases gigantes
        if tokens_sent:
            pontuacao_frases.append((texto_sent, score / len(tokens_sent)))

    # 3. Retornar as 3 com maior score
    # Se não encontrar 3 frases com os filtros, devolve o que houver
    melhores = sorted(pontuacao_frases, key=lambda x: x[1], reverse=True)
    return [f[0] for f in melhores[:3]]