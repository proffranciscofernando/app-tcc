import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Configuração do cliente Groq com chave de API (recomenda-se definir via variável de ambiente)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# ----------------------------
# Função para gerar ideias de TCC
# ----------------------------
def gerar_ideias_tcc(curso, instituicao, area, tipo, restricoes):
    prompt = f"""
Você é um especialista em orientação de trabalhos de conclusão de curso (TCC) para alunos de engenharia.

Com base nas seguintes informações:

Curso: {curso}
Instituição: {instituicao or "não informada"}
Área de Interesse: {area}
Tipo de Trabalho: {tipo}
Restrições e Recomendações: {restricoes}

Gere três sugestões de TCC. Para cada uma, inclua:
1. Título
2. Descrição do projeto
3. Objetivos principais
4. Metodologia sugerida
5. Ferramentas e tecnologias recomendadas

Use linguagem clara, técnica e acadêmica.
""".strip()

    # Chamada à API Groq
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    resposta = ""
    for chunk in completion:
        resposta += chunk.choices[0].delta.content or ""
    return resposta

# ----------------------------
# Interface do usuário (sem função)
# ----------------------------


st.set_page_config(page_title="Gerador de TCC com IA", page_icon="🎓", layout="centered")

st.image("image.png", use_container_width=True)

st.markdown("""
# 🎓 Assistente de Ideias para TCC

Bem-vindo ao seu assistente inteligente para trabalhos de conclusão de curso!

Este aplicativo usa **Inteligência Artificial** para gerar sugestões completas de temas para TCC,
com base em informações do curso, área de interesse, tipo de projeto e restrições/recomendações.

""", unsafe_allow_html=True)

st.divider()

st.markdown("### ✍️ Para gerar temas de TCC, por favor preencha os campos abaixo:")

curso = st.text_input("Curso", placeholder="Ex: Engenharia Mecânica, Engenharia Civil, Engenharia de Produção, etc")
instituicao = st.text_input("Instituição (opcional)")
area = st.text_input("Área de interesse", placeholder="Ex: Inteligência Artificial, Sustentabilidade, Materiais, etc.")

# Dropdown com opção "Outro"
tipo_opcao = st.selectbox(
    "Tipo de trabalho",
    [
        "Selecionar",
        "Projeto aplicado",
        "Experimental",
        "Teórico",
        "Computacional",
        "Revisão bibliográfica",
        "Outro (especificar)"
    ]
)

if tipo_opcao == "Outro (especificar)":
    tipo_custom = st.text_input("Digite o tipo de trabalho:")
    tipo = tipo_custom.strip() if tipo_custom else "Outro"
elif tipo_opcao != "Selecionar":
    tipo = tipo_opcao
else:
    tipo = None

restricoes = st.text_area("Restrições e Recomendações", placeholder="Ex: Trabalho individual, sem acesso a laboratório,"
                                                                    " prazo de 6 meses...")

if st.button("Gerar sugestões de TCC"):
    with st.spinner("Consultando a IA..."):
        resultado = gerar_ideias_tcc(curso, instituicao, area, tipo, restricoes)
        st.markdown("### 💡 Sugestões de TCC")
        st.markdown(resultado)

