import pandas as pd

def resumo_financeiro(df_financeiro: pd.DataFrame):
    # Totais
    receita = df_financeiro[df_financeiro["tipo"] == "Receita"]["valor"].sum()
    despesa = df_financeiro[df_financeiro["tipo"] == "Despesa"]["valor"].sum()
    lucro = receita - despesa

    # Ticket médio de receita por transação
    receita_transacoes = df_financeiro[df_financeiro["tipo"] == "Receita"]
    ticket_medio = receita_transacoes["valor"].mean() if not receita_transacoes.empty else 0

    # Receita e despesa por mês (supondo que existe coluna "data")
    if "data" in df_financeiro.columns:
        df_financeiro["mes"] = pd.to_datetime(df_financeiro["data"]).dt.to_period("M")
        receita_por_mes = (
            df_financeiro[df_financeiro["tipo"] == "Receita"]
            .groupby("mes")["valor"].sum()
            .to_dict()
        )
        despesa_por_mes = (
            df_financeiro[df_financeiro["tipo"] == "Despesa"]
            .groupby("mes")["valor"].sum()
            .to_dict()
        )
    else:
        receita_por_mes, despesa_por_mes = {}, {}

    return {
        "receita_total": receita,
        "despesa_total": despesa,
        "lucro_liquido": lucro,
        "ticket_medio": ticket_medio,
        "receita_por_mes": receita_por_mes,
        "despesa_por_mes": despesa_por_mes,
    }


def resumo_operacional(df_clientes: pd.DataFrame, df_manutencoes: pd.DataFrame):
    clientes_ativos = len(df_clientes)
    total_manutencoes = len(df_manutencoes)

    # Manutenções por cliente
    manutencoes_por_cliente = (
        df_manutencoes["id_cliente"].value_counts().to_dict()
        if "id_cliente" in df_manutencoes.columns else {}
    )

    # Frequência média de manutenção por cliente
    freq_media_manutencoes = (
        total_manutencoes / clientes_ativos if clientes_ativos > 0 else 0
    )

    # Última manutenção registrada
    ultima_manutencao = (
        pd.to_datetime(df_manutencoes["data"]).max()
        if "data" in df_manutencoes.columns and not df_manutencoes.empty
        else None
    )

    return {
        "clientes_ativos": clientes_ativos,
        "total_manutencoes": total_manutencoes,
        "manutencoes_por_cliente": manutencoes_por_cliente,
        "freq_media_manutencoes": freq_media_manutencoes,
        "ultima_manutencao": str(ultima_manutencao) if ultima_manutencao else None,
    }
