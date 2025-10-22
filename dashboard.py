import streamlit as st
import pandas as pd
from scripts.leitura_db import conectar_db, ler_clientes, ler_financeiro, ler_manutencoes
from scripts.analise import resumo_financeiro, resumo_operacional
from scripts.llm_insights import gerar_insights

# --- CONFIGURAÇÃO BÁSICA ---
st.set_page_config(page_title="Dashboard da Empresa EDS Climatizações", layout="wide")
#--- LOGO E NOME DA EMPRESA ---
from PIL import Image
logo = Image.open("logo.png")  # Certifique-se de que o arquivo está na mesma pasta que o dashboard.py
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    st.image(logo, width=120)
with col_titulo:
    st.title(" Dashboard Financeiro e Operacional - EDS Climatizações")

# --- CONEXÃO COM BANCO ---
conn = conectar_db("db/empresa_arcondicionado.sqlite")

df_clientes = ler_clientes(conn)
df_financeiro = ler_financeiro(conn)
df_manutencoes = ler_manutencoes(conn)

# --- ANÁLISES ---
resumo = {}
resumo.update(resumo_financeiro(df_financeiro))
resumo.update(resumo_operacional(df_clientes, df_manutencoes))

# --- LAYOUT ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Receita Total", f"R$ {resumo['receita_total']:.2f}")
col2.metric("📉 Despesa Total", f"R$ {resumo['despesa_total']:.2f}")
col3.metric("📈 Lucro Líquido", f"R$ {resumo['lucro_liquido']:.2f}")
col4.metric("🎟️ Ticket Médio", f"R$ {resumo['ticket_medio']:.2f}")

st.divider()

# --- GRÁFICOS FINANCEIROS ---
if not df_financeiro.empty:
    df_financeiro["data"] = pd.to_datetime(df_financeiro["data"])
    df_financeiro["tipo"] = df_financeiro["tipo"].str.strip().str.capitalize()

    # Extrai número e nome do mês
    df_financeiro["mes_num"] = df_financeiro["data"].dt.month
    df_financeiro["mes_nome"] = df_financeiro["data"].dt.strftime("%b")
    
    # Ordem correta dos meses
    meses_ordem = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", 
                   "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    
    # Agrupa por número do mês e tipo
    df_mes = (
        df_financeiro.groupby(["mes_num", "tipo"])["valor"]
        .sum()
        .unstack(fill_value=0)
        .rename(columns={"Receita": "Receita", "Despesa": "Despesa"})
        .sort_index()
    )
    
    # Adiciona coluna com nome do mês
    df_mes["Mês"] = [meses_ordem[i - 1] for i in df_mes.index]
    
    # Converte a coluna "Mês" para categoria com ordem correta
    df_mes["Mês"] = pd.Categorical(df_mes["Mês"], categories=meses_ordem, ordered=True)
    
    # Ordena pelo mês corretamente
    df_mes = df_mes.sort_values("Mês")
    
    # Formata os valores monetários com R$
    for coluna in df_mes.columns:
        if coluna in ["Receita", "Despesa"]:
            df_mes[coluna] = df_mes[coluna].apply(lambda x: f"R$ {x:,.2f}" if pd.notnull(x) else "R$ 0,00")
    
    # Define Mês como índice
    df_mes = df_mes.set_index("Mês")

    st.subheader("📆 Receita vs Despesa")
    
    # Prepara dados para o gráfico (sem formatação R$ para o gráfico)
    df_grafico = (
        df_financeiro.groupby(["mes_num", "tipo"])["valor"]
        .sum()
        .unstack(fill_value=0)
        .rename(columns={"Receita": "Receita", "Despesa": "Despesa"})
        .sort_index()
    )
    df_grafico["Mês"] = [meses_ordem[i - 1] for i in df_grafico.index]
    df_grafico["Mês"] = pd.Categorical(df_grafico["Mês"], categories=meses_ordem, ordered=True)
    df_grafico = df_grafico.sort_values("Mês").set_index("Mês")
    
    # Exibe tabela formatada e gráfico (CORREÇÃO APLICADA AQUI)
    st.dataframe(df_mes, width='stretch')
    st.line_chart(df_grafico)
else:
    st.info("Sem dados financeiros suficientes para exibir gráficos.")


st.divider()

# --- DADOS OPERACIONAIS ---
col1, col2, col3 = st.columns(3)
col1.metric("👥 Clientes Ativos", resumo["clientes_ativos"])
col2.metric("🛠️ Total de Manutenções", resumo["total_manutencoes"])
col3.metric("🔁 Média de Manutenções/Cliente", f"{resumo['freq_media_manutencoes']:.2f}")

if resumo["ultima_manutencao"]:
    st.caption(f"🗓️ Última manutenção registrada: {resumo['ultima_manutencao']}")

st.divider()

# --- INSIGHTS COM IA ---
st.subheader("🤖 Geração de Insights com IA")
if st.button("Gerar insights com LLM"):
    with st.spinner("Analisando dados com IA..."):
        insights = gerar_insights(resumo)
    st.markdown(insights)