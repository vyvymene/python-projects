

# 💰 Controle de Gastos Pessoais

Sistema de linha de comando (CLI) desenvolvido em Python para gerenciar gastos pessoais, com persistência de dados em JSON. Projeto prático desenvolvido durante o primeiro semestre do curso de Análise e Desenvolvimento de Sistemas (ADS).

## 📋 Funcionalidades

- **Cadastrar gasto**: registra descrição, categoria, quantidade, valor unitário e data — o valor total é calculado automaticamente (quantidade × valor unitário)
- **Listar gastos**: exibe todos os gastos cadastrados, com quantidade, valor unitário e valor total
- **Editar gasto**: atualiza os dados de um gasto já existente, recalculando o valor total
- **Remover gasto**: exclui um gasto da lista
- **Total de gastos**: soma automaticamente o valor total de todos os gastos cadastrados
- **Persistência de dados**: todas as informações são salvas em um arquivo `gastos.json`, mantendo os dados entre execuções do programa

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo `json` (leitura e escrita de dados estruturados)
- Módulo `os` (verificação de existência de arquivos)

## 🚀 Como executar

1. Clone o repositório:
```bash
git clone https://github.com/vyvymene/python-aulas.git