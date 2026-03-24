import subprocess
import sys
import os
import glob

# Diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

def executar_script(nome_script):
    """Executa um script Python e retorna o status"""
    caminho_completo = os.path.join(script_dir, nome_script)
    try:
        subprocess.run(
            [sys.executable, caminho_completo],
            cwd=script_dir,
            check=True
        )
        print(f"\n {nome_script} executado com sucesso!\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n Erro ao executar {nome_script}: {e}\n")
        return False
    except FileNotFoundError:
        print(f"\n Arquivo não encontrado: {caminho_completo}\n")
        return False

def encontrar_artigos_tex():
    """Encontra todos os ficheiros artigo_*.tex na pasta"""
    padrao = os.path.join(script_dir, "artigo_*.tex")
    ficheiros = sorted(glob.glob(padrao))
    return ficheiros

def compilar_latex_para_pdf(caminho_tex):
    """Compila um ficheiro .tex para PDF usando pdflatex"""
    nome_ficheiro = os.path.basename(caminho_tex)
    
    try:
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory=" + script_dir, caminho_tex],
            cwd=script_dir,
            check=True,
            capture_output=True
        )
        
        # Remover ficheiros temporários
        base_nome = os.path.splitext(nome_ficheiro)[0]
        extensoes_temp = [".aux", ".log", ".out"]
        for ext in extensoes_temp:
            ficheiro_temp = os.path.join(script_dir, base_nome + ext)
            if os.path.exists(ficheiro_temp):
                os.remove(ficheiro_temp)
        
        pdf_nome = base_nome + ".pdf"
        print(f"\n {nome_ficheiro} compilado com sucesso!")
        print(f"    PDF gerado: {pdf_nome}\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n Erro ao compilar {nome_ficheiro}: {e}\n")
        return False
    except FileNotFoundError:
        print("\n  pdflatex não encontrado. Instala com: brew install basictex")
        print("   Pulando compilação para PDF.\n")
        return False

def main():
    """Função principal"""
    
    # 1. Executar tokeniz.py (que gera os 3 artigos .tex)
    if not executar_script("tokeniz.py"):
        print("\n Erro ao executar tokeniz.py. Abortando.")
        sys.exit(1)
    
    # 2. Encontrar os ficheiros .tex gerados
    artigos_tex = encontrar_artigos_tex()
    
    if not artigos_tex:
        print("\n  Nenhum ficheiro artigo_*.tex foi gerado!")
        sys.exit(1)
    
    print(f"\n {len(artigos_tex)} ficheiros .tex encontrados:")
    for tex in artigos_tex:
        print(f"   - {os.path.basename(tex)}")
    
    # 3. Compilar cada .tex para PDF
    erros_compilacao = []
    for caminho_tex in artigos_tex:
        if not compilar_latex_para_pdf(caminho_tex):
            erros_compilacao.append(os.path.basename(caminho_tex))
    
    # Resumo final
    
    print(f"\n Ficheiros .tex gerados: {len(artigos_tex)}")
    print(f" Ficheiros compilados com sucesso: {len(artigos_tex) - len(erros_compilacao)}")
    
    if erros_compilacao:
        print("\n  Ficheiros com erro na compilação:")
        for erro in erros_compilacao:
            print(f"   - {erro}")
    else:
        print("\n Todos os ficheiros foram processados com sucesso!")
        print("   PDFs gerados:")
        for tex in artigos_tex:
            pdf = tex.replace(".tex", ".pdf")
            if os.path.exists(pdf):
                print(f"   - {os.path.basename(pdf)}")
    
    print()
    sys.exit(0 if not erros_compilacao else 1)

if __name__ == "__main__":
    main()
