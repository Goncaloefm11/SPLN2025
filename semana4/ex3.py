import spacy
from collections import Counter

nlp = spacy.load("pt_core_news_sm")

with open("harry.txt", "r", encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)

dicion = Counter()
for token in doc:
    if token.pos_ == "VERB":
        if token.text not in dicion:
            dicion[token.text] = 1
        else:
            dicion[token.text]+=1

#da os mais comuns organizados
melhores = dicion.most_common(10)
#melhores = sorted(dicion.items(), key=lambda x: x[1], reverse=True)


print(melhores)

