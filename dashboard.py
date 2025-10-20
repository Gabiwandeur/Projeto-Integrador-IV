import streamlit as st
import pandas as pd
from scripts.leitura_db import conectar_db, ler_clientes, ler_financeiro, ler_manutencoes
from scripts.analise import resumo_financeiro, resumo_operacional
from scripts.llm_insights import gerar_insights

# --- CONFIGURAÇÃO BÁSICA ---
st.set_page_config(page_title="Dashboard da Empresa de Ar-Condicionado", layout="wide")
st.title("📊 Dashboard Financeiro e Operacional")

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
if resumo["receita_por_mes"] and resumo["despesa_por_mes"]:
    df_mes = pd.DataFrame({
        "Receita": resumo["receita_por_mes"],
        "Despesa": resumo["despesa_por_mes"]
    }).fillna(0)
    st.subheader("📆 Receita vs Despesa por Mês")
    st.line_chart(df_mes)
else:
    st.info("Sem dados mensais suficientes para exibir gráficos.")

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
st.subheader("🤖 Geração de Insights Automáticos")
if st.button("Gerar insights com LLM"):
    with st.spinner("Analisando dados com IA..."):
        insights = gerar_insights(resumo)
    st.markdown(insights)
