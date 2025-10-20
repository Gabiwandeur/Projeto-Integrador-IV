import ollama

def gerar_insights(resumo: dict) -> str:
    prompt = f"""
    Você é um consultor de negócios especializado em empresas de climatização.
    Analise os dados abaixo e gere insights estratégicos em português, claros e objetivos.

    📊 Dados financeiros:
    - Receita total: R$ {resumo.get('receita_total', 0):.2f}
    - Despesa total: R$ {resumo.get('despesa_total', 0):.2f}
    - Lucro líquido: R$ {resumo.get('lucro_liquido', 0):.2f}
    - Ticket médio: R$ {resumo.get('ticket_medio', 0):.2f}

    Receita por mês: {resumo.get('receita_por_mes', {})}
    Despesa por mês: {resumo.get('despesa_por_mes', {})}

    🛠️ Dados operacionais:
    - Clientes ativos: {resumo.get('clientes_ativos', 0)}
    - Total de manutenções: {resumo.get('total_manutencoes', 0)}
    - Frequência média de manutenção por cliente: {resumo.get('freq_media_manutencoes', 0):.2f}
    - Última manutenção registrada: {resumo.get('ultima_manutencao', 'N/A')}

    Manutenções por cliente: {resumo.get('manutencoes_por_cliente', {})}

    Gere um relatório com os seguintes pontos:
    1. 📉 Situação financeira (comentando lucro, ticket médio e variações mensais).
    2. 🔧 Situação operacional (volume de clientes e manutenção).
    3. ⚠️ Riscos ou pontos de atenção.
    4. 🚀 Oportunidades de crescimento (ex.: fidelização, upsell, corte de custos).
    5. 📅 Projeções para os próximos 3 meses.

    Estruture a resposta com subtítulos e marcadores para facilitar a leitura.
    """
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
