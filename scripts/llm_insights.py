import ollama
import re

def gerar_insights(resumo: dict) -> str:
    prompt = f"""
    Você é um consultor de negócios especializado em empresas de climatização.
    Analise os dados abaixo e gere insights estratégicos em português BRASILEIRO, claros e objetivos.
    
    REGRAS CRÍTICAS:
    - USE APENAS CARACTERES SIMPLES DO PORTUGUÊS
    - NÃO USE caracteres com acento se não conseguir gerá-los corretamente
    - MANTENHA o texto TODO em uma única linha lógica, sem quebras desnecessárias
    - USE palavras sem acento se necessário

    📊 Dados financeiros:
    - Receita total: R$ {resumo.get('receita_total', 0):.2f}
    - Despesa total: R$ {resumo.get('despesa_total', 0):.2f}
    - Lucro líquido: R$ {resumo.get('lucro_liquido', 0):.2f}
    - Ticket medio: R$ {resumo.get('ticket_medio', 0):.2f}

    Receita por mes: {resumo.get('receita_por_mes', {})}
    Despesa por mes: {resumo.get('despesa_por_mes', {})}

    🛠️ Dados operacionais:
    - Clientes ativos: {resumo.get('clientes_ativos', 0)}
    - Total de manutencoes: {resumo.get('total_manutencoes', 0)}
    - Frequencia media de manutencao por cliente: {resumo.get('freq_media_manutencoes', 0):.2f}
    - Ultima manutencao registrada: {resumo.get('ultima_manutencao', 'N/A')}

    Manutencoes por cliente: {resumo.get('manutencoes_por_cliente', {})}

    Gere um relatorio com os seguintes pontos:
    1. SITUACAO FINANCEIRA (comentando lucro, ticket medio e variacoes mensais)
    2. SITUACAO OPERACIONAL (volume de clientes e manutencao)
    3. RISCOS OU PONTOS DE ATENCAO
    4. OPORTUNIDADES DE CRESCIMENTO (ex.: fidelizacao, upsell, corte de custos)
    5. PROJECOES PARA OS PROXIMOS 3 MESES

    Estruture a resposta com subtitulos e marcadores para facilitar a leitura.
    """
    
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": prompt}],
            options={
                'temperature': 0.3,  # Reduz a criatividade para ser mais consistente
            }
        )
        
        texto_insights = response["message"]["content"]
        
        # CORREÇÃO AGGRESSIVA: Remover TODAS as quebras de linha problemáticas
        # Primeiro, normalizar quebras de linha
        texto_insights = texto_insights.replace('\r\n', '\n').replace('\r', '\n')
        
        # Dividir em linhas e processar
        lines = texto_insights.split('\n')
        processed_lines = []
        
        for line in lines:
            line = line.strip()
            # Se a linha tem apenas 1-2 caracteres e não é um marcador, junta com a anterior
            if (len(line) <= 2 and 
                not line.startswith('#') and 
                not line.startswith('*') and 
                not line.startswith('-') and 
                not line.startswith('•') and
                line != '' and
                processed_lines):
                processed_lines[-1] += line
            else:
                processed_lines.append(line)
        
        texto_insights = '\n'.join(processed_lines)
        
        # Substituições diretas para os problemas específicos que vimos
        correcoes = {
            'é': 'e', 'á': 'a', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'ã': 'a', 'õ': 'o', 'ç': 'c', 'eˊ': 'e', 'meˊ': 'me',
            'teˊ': 'te', 'deˊ': 'de', 'ı́': 'i', 'ú': 'u',
            'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
            'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
            ' Saúde': ' Saude', ' estável': ' estavel',
            ' médio': ' medio', ' média': ' media'
        }
        
        for problema, correcao in correcoes.items():
            texto_insights = texto_insights.replace(problema, correcao)
        
        return texto_insights
        
    except Exception as e:
        return f"Erro ao gerar insights: {str(e)}"