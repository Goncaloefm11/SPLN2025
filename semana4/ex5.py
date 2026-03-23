import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_sm")

with open("harry.txt", "r", encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)
matcher = Matcher(nlp.vocab)

pattern = [
    {"ENT_TYPE": "PER", "OP": "+"},
    {"POS": {"IN": ["AUX", "VERB"]}},
    {"POS": "DET", "OP": "*" },
    {"POS": {"IN": ["NOUM", "PROPN"]}, "OP": "+"}
]
matcher.add("match_id", [pattern], greedy="LONGEST")
matches = matcher(doc)

#print(matches)

for id, start, end in matches:
    print(doc[start:end])