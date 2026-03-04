print("Olá, Eu sou a Elisa, o que vai na tua cabeça?")
resposta = input().lower() 

if any(saudacao in resposta for saudacao in ["ola", "oi", "boa tarde", "bom dia"]):
    print("Olá! Como posso ajudar você hoje?")
else:
    print("Interessante, me conte mais sobre isso.")

while resposta != "":
    resposta = input().lower()
    
    if "doi" in resposta:
        if "muito" in resposta:
            print("Sinto muito que a dor esteja forte. Já tentou tomar algum remédio ou usar gelo?")
        elif "pouco" in resposta:
            print("Ainda bem que é pouco, mas cuide-se. Quer falar mais sobre isso?")
        else:
            print("Sinto muito pela dor. É algo físico ou emocional?")

    elif "triste" in resposta:
        if "magoaram" in resposta:
            print("Sinto muito que te tenham magoado. As pessoas às vezes são difíceis. Quer desabafar?")
        elif "perdi" in resposta:
            print("Meus sentimentos pela sua perda. Estou aqui para te ouvir.")
        else:
            print("Sinto muito que esteja triste. O que aconteceu?")

    elif "ajuda" in resposta or "amigo" in resposta:
        print("Eu estou aqui para te ouvir. O que você gostaria de falar primeiro?")

    elif "feliz" in resposta:
        print("Fico feliz em ouvir isso! O que está te fazendo sentir assim?")

    elif "vou me embora" in resposta or "xau" in resposta:
        print("Até logo! Cuide-se.")
        break
        
    else:
        print("Entendo. Pode me contar mais detalhes?")