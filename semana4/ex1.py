import spacy
from spacy import displacy


nlp = spacy.load("pt_core_news_sm")

text = "A Maria é aluna da Universidade do Minho que se situa em Braga, Portugal desde 2018."
#PER ORG GEO

doc = nlp(text)

for token in doc:
    print(token.text, " POS:",token.pos_, " Lemma:", token.lemma_, " Dep:",token.dep_, " Entity:",token.ent_type_, " Head:", token.head.text, " Morph:", token.morph)

for ent in doc.ents:
    print(ent, ent.label_)

for sent in doc.sents:
    print(sent)

displacy.serve(doc, style="ent")
