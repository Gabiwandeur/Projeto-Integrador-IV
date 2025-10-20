from scripts.leitura_db import conectar_db, ler_clientes, ler_financeiro, ler_manutencoes
from scripts.analise import resumo_financeiro, resumo_operacional
from scripts.llm_insights import gerar_insights

conn = conectar_db("db/empresa_arcondicionado.sqlite")
df_clientes = ler_clientes(conn)
df_financeiro = ler_financeiro(conn)
df_manutencoes = ler_manutencoes(conn)

resumo = {}
resumo.update(resumo_financeiro(df_financeiro))
resumo.update(resumo_operacional(df_clientes, df_manutencoes))

insights = gerar_insights(resumo)
print(insights)
