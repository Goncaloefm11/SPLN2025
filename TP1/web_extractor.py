import requests
from bs4 import BeautifulSoup

def extrair_texto_da_web(url):
    try:
        # Simular um browser para evitar bloqueios
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remover elementos inúteis (scripts, estilos, navegação)
        for script_or_style in soup(["script", "style", "nav", "footer", "header"]):
            script_or_style.decompose()

        # Obter o texto e limpar espaços em branco excessivos
        texto = soup.get_text(separator=' ') #separa por um espaço apenas
        linhas = (line.strip() for line in texto.splitlines())
        '''
        ENTRADA (texto):
        Olá mundo
            
            Como vai
        Tudo bem"
QUAL 
        APÓS splitlines():
        ["Olá mundo", "  ", "   Como vai", "Tudo bem"]

        APÓS strip():
        ["Olá mundo", "", "Como vai", "Tudo bem"]
        '''
        chunks = (phrase.strip() for line in linhas for phrase in line.split("  "))
        texto_limpo = '\n'.join(chunk for chunk in chunks if chunk)
        '''
        ENTRADA (chunks):
        ["Olá mundo", "", "Como vai", "", "Tudo bem"]

        APÓS if chunk (remove vazios):
        ["Olá mundo", "Como vai", "Tudo bem"]

        APÓS '\n'.join():
        "Olá mundo
        Como vai
        Tudo bem"
        '''
        
        return texto_limpo
    except Exception as e:
        print(f"Erro ao aceder à URL {url}: {e}")
        return None