from langchain_core.tools import tool


@tool
def consultar_planos() -> str:
    """Consulta os planos e preços mensais do catálogo fictício do provedor."""
    return '300 Mbps: R$ 79,90; 500 Mbps: R$ 99,90; 700 Mbps: R$ 129,90.'


@tool
def diagnosticar_conexao(sintoma: str) -> str:
    """Consulta orientações de suporte para um sintoma de conexão informado pelo cliente."""
    texto = sintoma.lower()
    if any(p in texto for p in ('lenta', 'lentidão', 'velocidade', 'lento')):
        return 'Teste a velocidade por cabo, interrompa downloads e compare com o plano contratado.'
    if any(p in texto for p in ('sem internet', 'queda', 'offline', 'sem conexão')):
        return 'Verifique os cabos e luzes do roteador. Reinicie o roteador e aguarde. Se persistir, procure o suporte.'
    return 'Verifique se outros dispositivos apresentam o problema e informe o sintoma ao suporte.'
