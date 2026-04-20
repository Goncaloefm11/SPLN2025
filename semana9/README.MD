# Projeto de Reconhecimento de Entidades Mencionadas (NER) em Português

Este repositório contém o trabalho de treino de um modelo de Processamento de Linguagem Natural (NLP) para identificar entidades como **Pessoas (PER)**, **Locais (LOC)** e **Organizações (ORG)** em textos na língua portuguesa.

## 🚀 Tecnologias Utilizadas
* **Python 3**
* **spaCy v3.x** (Biblioteca principal de NLP)
* **Hugging Face Datasets** (Fonte de dados: `lfcc/portuguese_ner`)

## 📊 Performance do Modelo
O modelo foi treinado utilizando uma arquitetura baseada em `Tok2Vec` e um classificador `NER`. Após o treino, o modelo atingiu métricas de excelência:

| Métrica | Valor |
| :--- | :--- |
| **F-Score (ENTS_F)** | **95.60%** |
| **Precisão (ENTS_P)** | **95.54%** |
| **Recall (ENTS_R)** | **95.66%** |
| **Score Final** | **0.96** |

O treino foi concluído com sucesso após aproximadamente 2800 iterações, demonstrando uma convergência estável e alta precisão na identificação de entidades.

## 📂 Estrutura do Repositório
* `aula9.ipynb`: Notebook com o código de conversão de dados e testes.
* `config.cfg`: Ficheiro de configuração gerado para o treino do spaCy.
* `train.spacy` / `dev.spacy`: Datasets convertidos para o formato binário do spaCy.
* `output/model-best`: Pasta contendo o modelo com a melhor performance durante o treino.

## 🛠️ Como Utilizar o Modelo
Para carregar e testar o modelo treinado:

```python
import spacy

# Carregar o melhor modelo
nlp = spacy.load("./output/model-best")

# Exemplo de uso
texto = "O Gonçalo Magalhães estudou na Universidade do Minho e visitou a sede da Google em Portugal."
doc = nlp(texto)

for ent in doc.ents:
    print(f"Entidade: {ent.text: <20} | Categoria: {ent.label_}")