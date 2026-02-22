# CONTROLE-DE-NOTAS-DE-ALUNOS


Sistema de gestão de notas em Python que calcula a média final de alunos, define automaticamente a situação acadêmica e armazena os dados em ficheiros JSON e CSV. Também gera um quadro de honra com os alunos de melhor desempenho, automatizando o controle e organização de resultados escolares.

---

# 📘 README – Sistema de Gestão de Notas (Mini Pauta)

## 📖 Sobre o Projeto

Este projeto é um sistema simples de gestão acadêmica desenvolvido em Python. Ele calcula automaticamente a média final de cada aluno, determina sua situação (Aprovado, Reprovado, Excelência, etc.) e organiza os dados em ficheiros.

Além disso, gera automaticamente um **quadro de honra** com os alunos que obtiveram melhor desempenho.

---

## ⚙️ Funcionalidades

* ✅ Cálculo automático da média final
* ✅ Classificação da situação do aluno
* ✅ Armazenamento em `mini_pauta.json`
* ✅ Exportação para `mini_pauta.csv`
* ✅ Geração automática de `quadro_de_honra.csv`
* ✅ Verificação de nomes duplicados

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* CSV
* Programação Orientada a Objetos (POO)

---

## 📂 Ficheiros Gerados

```
mini_pauta.json
mini_pauta.csv
quadro_de_honra.csv
```

---

## 🎓 Critérios de Avaliação

* ≥ 16 → Aprovado com excelência
* ≥ 10 → Aprovado
* 8.5–9.5 → Aprovado com recurso
* ≤ 8 → Reprovado

---

## 🚀 Como Executar

1. Certifique-se de ter Python instalado.
2. Instancie a classe `Alunos` informando nome e notas:

```python
Alunos("Carlos", 15, 14, 16)
```

O sistema fará todo o processamento automaticamente.

---



