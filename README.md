# 📊 Dashboard de Estoque Digital de e-SIM

## 📌 Visão Geral do Projeto

Este projeto tem como objetivo demonstrar a **coleta, organização, tratamento e visualização de dados** utilizando Python e Looker Studio, aplicados ao **controle de estoque digital de e-SIM**.

O trabalho foi desenvolvido como parte de um **Projeto de Extensão em Ciência de Dados**, com foco em **inovação de processos**, **governança de dados** e **boas práticas de segurança da informação**.

---

## 🚀 Objetivo

Criar um **dashboard interativo** que permita acompanhar indicadores de estoque digital de e-SIM, com base em:

* Quantidade total de e-SIMs
* Quantidade em uso
* Quantidade disponível
* Distribuição por DDD

O dashboard fornece uma visão gerencial clara e pode apoiar decisões operacionais relacionadas à gestão de estoque digital.

---

## 🧠 Contexto e Inovação

A estrutura de dados utilizada neste projeto foi inspirada em um **robô de coleta via API privada**, utilizado em ambiente corporativo real. Para fins acadêmicos e de conformidade legal:

* Nenhum dado real de produção foi utilizado
* Nenhuma credencial ou endpoint real foi exposto
* Os dados apresentados são **simulados (mockados)**, mantendo apenas o **formato e a lógica estrutural** do pipeline original

Essa abordagem permite demonstrar o processo completo de engenharia e análise de dados **sem violar a LGPD ou acordos de confidencialidade**.

---

## 🔐 Segurança e Confidencialidade

Este repositório **não contém dados sensíveis**.

As seguintes medidas foram adotadas:

* Tokens, chaves de API e URLs reais foram removidos
* Credenciais são carregadas via variáveis de ambiente
* Arquivos sensíveis não são versionados
* Apenas arquivos de exemplo (`.example`) são disponibilizados

### 📄 Exemplos de arquivos de configuração

* `.env.example` → exemplo de configuração de variáveis de ambiente
* `json_de_acesso.example.json` → exemplo de credencial de acesso ao BigQuery

⚠️ **Os arquivos reais (`.env` e `json_de_acesso.json`) não fazem parte do repositório e devem ser criados localmente pelo usuário.**

---

## 🧱 Estrutura dos Dados

A tabela final utilizada no dashboard possui o seguinte schema:

| Coluna     | Descrição                              |
| ---------- | -------------------------------------- |
| DDD        | Código de área (região)                |
| Total      | Total de e-SIMs disponíveis            |
| Em uso     | Quantidade de e-SIMs atualmente em uso |
| Disponível | Quantidade de e-SIMs disponíveis       |

> O campo **Disponível** é derivado de: `Total - Em uso`

---

## 🐍 Tecnologias Utilizadas

* **Python 3.x**
* **Pandas** (tratamento e geração de dados)
* **BigQuery** (armazenamento – ambiente simulado)
* **Looker Studio** (visualização de dados)
* **Git / GitHub** (versionamento)

---

## 📊 Dashboard

O dashboard foi desenvolvido no **Looker Studio** e apresenta:

* Indicadores gerais de estoque
* Distribuição por DDD
* Comparativo de uso e disponibilidade
* Visão agregada para apoio à decisão

> Para fins acadêmicos, prints do dashboard podem ser utilizados como evidência no relatório do projeto.

---

## ⚠️ Aviso Importante

Este projeto possui **finalidade exclusivamente acadêmica**.

Qualquer semelhança com estruturas reais de produção é proposital apenas no nível **estrutural**, não representando dados reais, sistemas internos ou informações confidenciais da organização.

---

## 👤 Autor

Projeto desenvolvido para fins acadêmicos no curso de **Ciência de Dados**, como parte das atividades de **Projeto de Extensão**.

---

## 📄 Licença

Este projeto é distribuído apenas para fins educacionais e de demonstração técnica.
