# Análise de Word Embeddings: Saga Harry Potter ⚡

Este projeto aplica técnicas de **Processamento de Linguagem Natural (PLN)** para mapear o universo de Harry Potter (Livros 1 e 2) num espaço vetorial, utilizando o algoritmo **Word2Vec**.

## 🎯 Objetivos
* Transformar texto bruto em representações matemáticas (vetores).
* Analisar relações semânticas entre personagens, casas de Hogwarts e professores.
* Demonstrar a eficácia da aritmética vetorial (analogias) na descoberta de conceitos abstratos.

## 🛠️ Metodologia

### 1. Tratamento de Dados (Cleaning)
Para garantir a precisão dos vetores e a pureza dos clusters, o texto passou por um processo de limpeza rigoroso:
* **Tokenização Avançada:** Uso da biblioteca `NLTK` para separar palavras de pontuações, evitando duplicados como "magia" e "magia.".
* **Limpeza Customizada:** Além das *stopwords* tradicionais, foram removidos verbos de elocução (ex: 'disse') e marcadores temporais (ex: 'então') para focar o modelo em entidades (personagens e objetos).
* **Normalização:** Conversão de todo o texto para minúsculas e remoção de palavras com menos de 3 caracteres.

### 2. Configuração do Modelo
* **Algoritmo:** Skip-gram (`sg=1`), escolhido pela sua superioridade em capturar contextos em datasets de tamanho reduzido.
* **Dimensões:** 100 (`vector_size=100`).
* **Janela de Contexto:** 5 palavras (`window=5`).

## 📈 Resultados e Conclusões

### Aritmética de Vetores (Analogias)
O modelo demonstrou "compreender" a hierarquia do mundo mágico através de operações matemáticas:
* **Snape - Sonserina + Grifinória = Lockhart**
    * *Conclusão:* O modelo isolou o conceito de "Professor" e aplicou-o à casa oposta com sucesso.
* **Harry - Grifinória + Sonserina = Draco**
    * *Conclusão:* Identificou a rivalidade e a importância equivalente das personagens nas suas respetivas casas.

### Visualização 3D (TensorFlow Projector)
A análise visual confirmou a formação de clusters coerentes:
* **Cluster de Professores:** Snape, Flitwick, Quirrell e Dumbledore aparecem geometricamente próximos.
* **Cluster de Família:** Os Dursley (Válter, Petúnia, Duda) foram agrupados num setor isolado, refletindo a sua separação do mundo mágico.
* **Alcunhas:** O modelo associou "Mione" a "Hermione" com uma similaridade superior a 0.88.

## 📁 Estrutura do Repositório
* `aula2.ipynb`: Notebook com o código-fonte em Python.
* `vecs.tsv`: Vetores numéricos para exportação.
* `meta.tsv`: Metadados (palavras) para etiquetas no Projector.
* `harryPedra.txt` / `harryCamara.txt`: Corpus utilizado.

---
**Trabalho realizado por:** Gonçalo Magalhães (PG61514)
**Data:** Abril de 2026