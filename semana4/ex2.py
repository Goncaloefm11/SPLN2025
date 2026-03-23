import spacy

nlp = spacy.load("pt_core_news_sm")

text = '''Carlo Ancelotti protagonizou, na tarde de segunda-feira, um momento insólito ao esquecer-se de mencionar o nome de João Pedro, avançado do Chelsea, 
na hora de revelar os jogadores convocados para os jogos da seleção do Brasil diante França e Croácia. 
Assim que terminou o anúncio de Ancelotti, um responsável da Confederação Brasileira de Futebol foi chamado a atenção por um jornalista 
e o treiandor italiano acabaria por redimir-se, anunciando o nome de João Pedro. 
Ora, o jogador do Chelsea não escapou ao susto e admitiu mesmo ter pensado que iria ficar de fora dos jogos de preparação para o 
Mundial2026. Parece que é sempre a primeira vez. Há sempre aquele frio na barriga. Aí quando ele terminou a lista, disse: 'Caraca, mané, fiquei de fora'. Pouco depois, toda a gente começa ligar-me e fiquei sem entender. 
Voltei [a ver] e disse: 'Caraca, estou dentro'. 
É o mesmo frio na barriga desde a primeira vez que eu fui. Muito feliz. Estou a viver um momento muito especial na minha vida. 
E agora vamos lá, é ir com tudo contra a França e a Croácia", contou João Pedro, visivelmente bem disposto, em entrevista ao programa "Panela Sportv". 
'''
doc = nlp(text)

for ent in doc.ents:
    if ent.label_ == "PER" or ent.label_ == "ORG":
        print(ent)

