# Dashboard Empresa de Ar-Condicionado

Este projeto é um **dashboard interativo** para análise financeira e operacional de uma empresa de climatização, desenvolvido em **Python** com **Streamlit** e integração com **LLM** para geração de insights automáticos.

---

## 📋 Pré-requisitos

* Python 3.10.11
* Git
* 4GB de RAM disponível (mínimo recomendado)

---

## 🛠️ Instalação

### Windows

1. **Instale o Python**

   * Acesse [python.org](https://www.python.org/)
   * Baixe a versão mais recente do Python
   * Durante a instalação, **marque a opção "Add Python to PATH"**

2. **Instale o Git**

   * Acesse [git-scm.com](https://git-scm.com/)
   * Baixe e instale o Git for Windows
   * Use as configurações padrão durante a instalação

3. **Clone o repositório**

```cmd
git clone https://github.com/seu-usuario/dashboard-ar-condicionado.git
cd dashboard-ar-condicionado
```

4. **Crie um ambiente virtual (recomendado)**

```cmd
python -m venv venv
venv\Scripts\activate
```

5. **Instale as dependências**

```cmd
pip3 install -r requirements.txt
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
python3 -m venv venv
source venv/bin/activate
```

4. **Instale as dependências**

```bash
pip3 install -r requirements.txt
```

---



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

### Instalação do Ollama

* **Windows:**
  Baixe do site [ollama.ai](https://ollama.ai/) e execute o instalador.
  O Ollama será instalado como serviço.

* **Linux:**

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
python3 -m streamlit run dashboard.py
```

O dashboard estará disponível em: [http://localhost:8501](http://localhost:8501)

Para fechar o console, utilize crtl+c.

### Opção 2: Versão Console

```bash
python main.py
```

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
