import sqlite3
import pandas as pd

def conectar_db(caminho_db):
    return sqlite3.connect(caminho_db)

def ler_clientes(conn):
    df = pd.read_sql_query("SELECT * FROM clientes", conn)
    # Se tiver coluna de data de cadastro, converte
    if "data_cadastro" in df.columns:
        df["data_cadastro"] = pd.to_datetime(df["data_cadastro"])
    return df

def ler_financeiro(conn):
    df = pd.read_sql_query("SELECT * FROM financeiro", conn)
    # Converte colunas de data para datetime
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"])
    return df

def ler_manutencoes(conn):
    df = pd.read_sql_query("SELECT * FROM manutencoes", conn)
    # Converte colunas de data para datetime
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"])
    return df
