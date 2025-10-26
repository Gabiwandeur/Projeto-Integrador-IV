# Dashboard Empresa de Ar-Condicionado

Este projeto é um **dashboard interativo** para análise financeira e operacional de uma empresa de climatização, desenvolvido em **Python** com **Streamlit** e integração com **LLM** para geração de insights automáticos.

---

## 📋 Pré-requisitos

* Python 3.10
* Git
* 4GB de RAM disponível (mínimo recomendado)

---

## 🛠️ Instalação

### Windows com WSL

1. **Instale o WSL com Ubuntu**

* [Guia de Instalacao do WSL no Windows 11](https://learn.microsoft.com/pt-br/windows/wsl/install)

2. **Clone o repositório**

```cmd
git clone https://github.com/seu-usuario/dashboard-ar-condicionado.git
cd dashboard-ar-condicionado
```

3. **Crie um ambiente virtual (recomendado)**

```cmd
python3.10 -m venv venv
source venv/bin/activate
```

4. **Instale as dependências**

```cmd
cd /mnt/c/Users/gabiw/github/Projeto-Integrador-IV
pip install -r requirements.txt
```

### Linux (Ubuntu/Debian)

1. **Atualize o sistema e instale dependências**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```

2. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/dashboard-ar-condicionado.git
cd dashboard-ar-condicionado
```

3. **Crie um ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate
```

4. **Instale as dependências**

```bash
pip install -r requirements.txt
```

---

## 🚀 Configuração do Banco de Dados

1. **Crie a estrutura de diretórios**

```bash
mkdir -p db
```

2. **Coloque seu arquivo SQLite em:**

```
db/empresa_arcondicionado.sqlite
```

> ⚠️ Nota: Certifique-se de que o banco de dados possui as tabelas:
>
> * `clientes`
> * `financeiro`
> * `manutencoes`

---

## 🤖 Configuração do Ollama (para Insights com IA)

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Download do Modelo LLM

```bash
ollama pull llama3.2
```

---

## 🎯 Executando o Projeto

### Opção 1: Dashboard Web (Streamlit)

1- Abrir o powershell
2- Entre na pasta do projeto (ex cd .\github\Projeto-Integrador-IV\)
2- Rode o seguinte comando:

```bash
python -m streamlit run dashboard.py
```

O dashboard estará disponível em: [http://localhost:8501](http://localhost:8501)

Para fechar o console, utilize crtl+c.

---

## 📁 Estrutura do Projeto

```
dashboard-ar-condicionado/
├── dashboard.py          # Aplicação principal Streamlit
├── main.py               # Versão console
├── scripts/
│   ├── leitura_db.py     # Leitura do banco de dados
│   ├── analise.py        # Análises financeiras e operacionais
│   └── llm_insights.py   # Geração de insights com IA
├── db/
│   └── empresa_arcondicionado.sqlite  # Banco de dados
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

---

## 📊 Funcionalidades

* ✅ Dashboard financeiro com métricas principais
* ✅ Gráficos de receita vs despesa
* ✅ Análise operacional de clientes e manutenções
* ✅ Insights automáticos com IA (LLM)
* ✅ Interface web responsiva
* ✅ Versão console para uso em terminal

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.
