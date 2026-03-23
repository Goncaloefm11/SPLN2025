def gerar_artigo_latex(nome_livro, frases, entidades, matches_lista):
    nome_base = nome_livro.replace(".txt", "").replace(".pdf", "")
    nome_ficheiro = f"artigo_{nome_base}.tex"
    
    # 1. Formatar Frases (Abstract)
    items_frases = "\n".join([f"\\item {f}" for f in frases])
    
    # 2. Formatar Entidades (Corpo)
    lista_entidades = "\n".join([f"\\item \\textbf{{{tipo}}}: {texto}" for texto, tipo in set(entidades)])

    # 3. Formatar Tabela de Matches
    # Criamos as linhas da tabela: Padrão & Texto Extraído
    linhas_tabela = ""
    for tipo, texto in matches_lista:
        # Limpar caracteres especiais que dão erro no LaTeX (como & ou _)
        texto_limpo = texto.replace("&", "\\&").replace("_", "\\_")
        linhas_tabela += f"{tipo} & {texto_limpo} \\\\ \\hline\n"

    conteudo_latex = f"""
\\documentclass{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[portuguese]{{babel}}
\\usepackage{{booktabs}}

\\title{{Análise Linguística: {nome_livro}}}
\\author{{Gonçalo Magalhães}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\begin{{abstract}}
Frases mais relevantes extraídas de \\textit{{{nome_livro}}} através do modelo Bi-grams.
\\begin{{itemize}}
{items_frases}
\\end{{itemize}}
\\end{{abstract}}

\\section{{Entidades Nomeadas (NER)}}
Foram identificadas as seguintes entidades no texto :
\\begin{{itemize}}
{lista_entidades}
\\end{{itemize}}
\\clearpage
\\section{{Análise de Padrões Gramaticais}}
A tabela seguinte apresenta os padrões identificados nas frases selecionadas, utilizando o spaCy :

\\begin{{table}}[h]
\\centering
\\begin{{tabular}}{{|l|p{{8cm}}|}}
\\hline
\\textbf{{Tipo de Padrão}} & \\textbf{{Trecho Extraído}} \\\\ \\hline
{linhas_tabela}
\\end{{tabular}}
\\caption{{Matches identificados nas frases com maior score.}}
\\end{{table}}
\\clearpage
\\bibliographystyle{{plain}}
\\begin{{thebibliography}}{{9}}
\\bibitem{{fonte}} Autor Desconhecido, \\textit{{{nome_livro}}}, Edição Digital.
\\end{{thebibliography}}

\\end{{document}}
"""

    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        f.write(conteudo_latex)
    print(f"Ficheiro LaTeX gerado com tabela: {nome_ficheiro}")