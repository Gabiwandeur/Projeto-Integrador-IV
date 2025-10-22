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

    IMPORTANTE: Use apenas caracteres simples do português, sem caracteres especiais complexos.
    """
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )
    
    texto_insights = response["message"]["content"]
    
    # CORREÇÃO SIMPLES: Remover todas as quebras de linha problemáticas
    # Primeiro, dividir o texto em linhas
    lines = texto_insights.split('\n')
    cleaned_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Se a linha tem apenas 1 caractere e a próxima linha também tem poucos caracteres,
        # provavelmente é uma palavra quebrada
        if (len(line) <= 2 and i + 1 < len(lines) and 
            len(lines[i + 1].strip()) <= 2 and
            not line.startswith('#') and  # Não é título
            not line.startswith('*') and  # Não é marcador
            not line.startswith('-') and  # Não é item de lista
            not line == ''):  # Não é linha vazia
            
            # Juntar as linhas quebradas
            combined = line
            j = i + 1
            while j < len(lines) and len(lines[j].strip()) <= 2:
                combined += lines[j].strip()
                j += 1
            
            cleaned_lines.append(combined)
            i = j
        else:
            cleaned_lines.append(line)
            i += 1
    
    # Reconstruir o texto
    texto_insights = '\n'.join(cleaned_lines)
    
    # Substituições diretas para caracteres problemáticos
    substituicoes = {
        'é': 'é',
        'á': 'á',
        'í': 'í', 
        'ó': 'ó',
        'ú': 'ú',
        'ã': 'ã',
        'õ': 'õ',
        'ç': 'ç',
        'eˊ': 'é',
        'meˊ': 'mé',
        'teˊ': 'té',
        'deˊ': 'dé',
        'ı́': 'í'
    }
    
    for problema, correcao in substituicoes.items():
        texto_insights = texto_insights.replace(problema, correcao)
    
    return texto_insights