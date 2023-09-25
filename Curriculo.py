from pathlib import Path

import streamlit as st
#import my_custom_theme
from PIL import Image
from streamlit_extras.app_logo import add_logo
from streamlit_lottie import st_lottie
import base64
import requests

import time

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Lucas Henrique de Barros"
PAGE_ICON = ":wave:"
NAME = "Lucas Henrique de Barros"
DESCRIPTION = """
❤️Apaixonado por tecnologia e empresas, possuo vivência no setor privado e público, sempre estando em contato com clientes, patronos e usuários em geral.

🎓 Sou bacharel em Direito (UNIMEP), com especialização em LGPD, e atualmente graduando em Ciência de Dados.

🥼 Durante a graduação e a especialização, obtive conhecimento e experiências com a implementação da LGPD no Brasil, manejo de planilhas em Excel, manutenção de bases de dados, e uma introdução ao mundo de dados.

🎲 Atualmente trabalho como Analista de BI na Transportadora Garbuio, trabalhando com extração, manipulação e visualização de dados, em que diariamente surgem novos desafios, insights e aprendizados.

💻Tenho experiência com Excel, linguagem SQL, MySQL, PostgreSQL e Power BI/Qlik View para análise e visualização de dados, e atualmente estou aprofundando meu conhecimento em Python.
"""
EMAIL = "barroslucash@gmail.com"
SOCIAL_MEDIA = {
    "💻 LinkedIn": "https://www.linkedin.com/in/lucas-h-barros/",
}


st.set_page_config(layout= 'wide', page_title=PAGE_TITLE ,page_icon=":wave:")

#my_custom_theme.apply_custom_theme()

add_logo("logo.png")

def load_lottierur1(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottierur1("https://lottie.host/0c84e0de-6029-46f0-a582-b6429cfc97c4/e5VWao3q69.json")



def mensagem_sucesso():
    sucesso = st.success('Arquivo baixado com sucesso!', icon = "✅")
    #time.sleep(1)
    sucesso.empty()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("logo.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapercave.com/wp/dMCG3T2.jpg");
background-size: 600px 400px;
background-position: bottom right;
background-repeat: no-repeat;
background-attachment: local;
image-rendering: pixelated;
image-rendering: -webkit-optimize-contrast;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

#st.markdown(page_bg_img, unsafe_allow_html=True)


resume_file = "Lucas Henrique de Barros.pdf"
css_file = "styles/main.css"
profile_pic = "logo.png"


st.markdown(
    """
    <style>
    body {
        background-color: #3e36b5; /* Cor de fundo desejada */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---

col1, col2= st.columns(2, gap="medium")
with col1:
    #add_logo('logo.png')
    st.title(NAME)
    st.write('\n')
    st.write(DESCRIPTION)
    st.write('\n')
with col2:
    imagem_local = Image.open("Picture4.png")
    st.image(imagem_local, width= None)
with col1:
    st.download_button(
        label=" 📄 Download do CV",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
        on_click=mensagem_sucesso
    )

with col1:
    st.write('\n')
    for linkedin, link in SOCIAL_MEDIA.items():
        st.write(f"[{linkedin}]({link})")
    st.write("📫", "barroslucash@gmail.com") 
    st.write("📞", "(19) 99263-0596")

st.write('\n')

st.write("---")
st.subheader("Soft Skills")
st.write(
    """
- ✔️ Esforçado e rápido aprendizado com tecnologias
- ✔️ Trabalho com eficiência, moderando os recursos e sendo eficaz na solução de problemas
- ✔️ Apaixonado pelo mundo de dados e sempre buscando aprender
- ✔️ Excelencia em trabalho em equipe e perfil analítico para as tarefas dispostas
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 📊 Visualização de Dados: Power Bi, QlikView, Google Looker, Python (Streamlit, Plotly, Matplotlib)
- 👩‍💻 Programação: Python (Numpy, Pandas), HTML e CSS.
- 🗄️ Bancos de Dados: SQL, MySQL, PostgreSQL.
"""
)


# --- WORK HISTORY ---
st.write('\n')

st.write("---")
st.subheader("Experiências: ")

st.write('\n')
st.write('\n')

col1, col2 = st.columns(2)

# --- JOB 1
with col1:
    st.write("📈", "**Analista de BI  | Transportadora Garbuio**")
    st.write("05/2023 - Atual")
    st.write(
    """
- BI (Data View):
\n
- ►  Gestão de Projetos de BI
- ►  Desenvolvimento de Dashboards de média/alta complexidade com indicadores estratégicos para geração de insights
- ►  Responsável pelo contato com os gestores para entendimento das regras de negócio até a validação dos dados.
- ►  Desenvolvimento em linguagem M e Dax de métricas e análise de dados importantes para o negócio.
- ►  HTML/CSS para criação de animações utilizáveis nos Dashboards 
- ►  Manutenção de Dashboards em funcionamento na empresa.
- ►  Gerenciamento e liberação de acessos via Sharepoint
- ►  Gerar relatórios específicos em Excel
- ►  Gestão de workspaces, deploy, atualização
- ►  Gestão de conjuntos de dados 
\n
- Engenharia de Dados:
\n
- ►  Consultas e manipulação em banco de dados em SQL Server, MySQL e PostgreSQL
- ►  Configuração e gestão de gateway
- ►  Criação, manutenção e gestão de fluxos de dados.
- ►  Automatização de fluxo de dados com Power Automate
- ►  Extração de informações via banco de dados e validação do Totvs/Protheus
"""
)

# --- JOB 2
with col1:
    st.write('\n')
    st.write("📈", "**Assistente de BI | Transportadora Garbuio**")
    st.write("02/2023 - 04/2023")
    st.write(
    """
-   Desenvolvimento de Dashboards com indicadores estratégicos para geração de insights
-   Manutenção de Dashboards em funcionamento na empresa
-   Consultas e manipulação em banco de dados em SQL Server
-   Extração de informações via banco de dados e validação do Totvs/Protheus
"""
)


# --- JOB 3
with col2:
    st.write('\n')
    st.write("👨🏽‍💼", "**Assistente de Defensor | Defensoria Pública do Estado de São Paulo**")
    st.write("04/2022 - 02/2023")
    st.write(
    """
-   Atendimentos presencial e online em grande número
-   Rotina Jurídico-Administrativa
-   Análise e explicação de situações complexas
-   Cobrança de Documentos
-   Alimentação de dados em planilhas e demais atividades administrativas
-   Controle da agenda de prazos internos e cumprimento
-   Elaboração e confecção de relatórios
"""
)


# --- JOB 4
with col2:
    st.write('\n')
    st.write("👨🏽‍💼", "**Estagiário jurídico | Tribunal Regional do Trabalho 15ª Região - Campinas/SP**")
    st.write("06/2019 - 06/2021")
    st.write(
    """
-  Atendimentos presencial e online em grande número
-  Rotina Jurídico-Administrativa
-  Análise e explicação de situações complexas
-  Cobrança de Documentos
-  Alimentação de dados em planilhas e demais atividades administrativas
-  Controle da agenda de prazos internos e cumprimento
-  Elaboração e confecção de relatórios
"""
)
    
# --- JOB 5
with col2:
    st.write('\n')
    st.write("👨🏽‍💼", "**Assistente jurídico | Dr. Vinicius Tomé & Advogados**")
    st.write("04/2015 - 01/2018")
    st.write(
    """
-  Rotina Jurídico-Administrativa
-  Atendimento ao cliente presencial e online
-  Cobrança de Documento
-  Desconto de títulos 
-  Negociação com clientes e parceiros
-  Elaboração, negociação e revisão de contratos
-  Digitação rápida de arquivos e informações
-  Formulação e acompanhamento de planilhas no Excel sobre clientes, prazos 
e financeiro
-  Consulta e manejo de informações
-  Organização de arquivos
"""
)



# --- Projects & Accomplishments ---


PROJECTS_PY = {
"📈 Análise dos preços de gasolina": "https://gaspriceapp.onrender.com",
"📈 Dashboard Simples de Vendas - Analisando a receita da empresa": "https://projeto-dashvendas-python.streamlit.app",
"📈 Análise de Dados da Fifa": "https://fifaproject.streamlit.app"
}


PROJECTS_BI = {
"📈 Dashboard Simples de Faturamento (Google Looker/Data Studio)": "https://lookerstudio.google.com/reporting/3959707c-c28d-4946-b667-d1567753ebc0",
"📈 Dashboard Simples de Perfomance de Campanha (Google Looker/Data Studio)": "https://lookerstudio.google.com/reporting/4157f723-d529-49c9-9baa-732865224df2",
"📈 Dashboard de Vendas (Power BI) ": "https://app.powerbi.com/view?r=eyJrIjoiYzQ5YTgzYWMtYjJkZi00N2U3LWIwNTYtNGYwOWI4NzIxYWY1IiwidCI6ImNjMmE5NWVhLTMzNWMtNDQzYi04NDQzLWU5YWQzM2ZmOWUwNCJ9 "
}

st.write('\n')
st.write("---")
st.subheader("Projetos de Portfólio")
st.write('\n')

st.write("Projetos em Python (Web Apps):")

for projeto_py, linker in PROJECTS_PY.items():
    st.write(f"[{projeto_py}]({linker})")

st.write('\n')
st.write("Projetos em BI:")
st.write('\n')

for projeto_bi, linked in PROJECTS_BI.items():
    st.write(f"[{projeto_bi}]({linked})")
