# 🎓 Gerador de Ideias para TCC com IA

Este é um aplicativo web desenvolvido com **Streamlit** e a **API da Groq (LLaMA 3)** que gera sugestões de temas de TCC para estudantes de engenharia. Ele utiliza inteligência artificial para criar títulos, descrições, objetivos, metodologias e ferramentas recomendadas com base em informações fornecidas pelo usuário.

## 🚀 Funcionalidades

- Geração de **3 sugestões completas de TCC** com base nos inputs do aluno
- Personalização por curso, instituição, área de interesse, tipo de trabalho e restrições
- Interface simples, interativa e pronta para ser usada em workshops e disciplinas

## 📦 Requisitos

- Python 3.8+
- Conta na [Groq API](https://console.groq.com/)
- Chave da API válida

## ⚙️ Instalação

1. Clone o repositório ou copie os arquivos para seu diretório local:

```bash
git clone https://github.com/seu-usuario/gerador-tcc-ia.git
cd gerador-tcc-ia
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🔐 Configuração do `.env`

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> **Importante:** não compartilhe sua chave de API e mantenha o arquivo `.env` fora do controle de versão.

## ▶️ Como executar o app

No terminal, execute:

```bash
streamlit run main.py
```

O navegador será aberto automaticamente (ou acesse `http://localhost:8501`).

## 🧠 Tecnologias utilizadas

- [Streamlit](https://streamlit.io/)
- [Groq API](https://console.groq.com/)
- [LLaMA 3](https://groq.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 📝 Licença

Este projeto é destinado ao uso educacional e acadêmico. Sinta-se livre para adaptar conforme necessário.