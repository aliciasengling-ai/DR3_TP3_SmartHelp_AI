import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from ferramentas import consultar_planos, diagnosticar_conexao


def criar_agente():
    load_dotenv()
    if not os.getenv('GROQ_API_KEY'):
        raise ValueError('Configure GROQ_API_KEY no arquivo .env.')
    modelo = ChatGroq(model=os.getenv('GROQ_MODEL', 'llama-3.3-70b-versatile'), temperature=0)
    # O agente executa ciclos de seleção de ferramentas e observação (ReAct).
    return create_agent(model=modelo, tools=[consultar_planos, diagnosticar_conexao],
                        checkpointer=InMemorySaver(),
                        system_prompt='Você é o SmartHelp AI. Responda em português. Use as ferramentas para preços e diagnóstico. O catálogo é fictício. Não invente preços nem afirme ter inspecionado a rede. Use o histórico da sessão.')


def main():
    try:
        agente = criar_agente()
    except Exception as erro:
        print(f'Erro de configuração: {erro}')
        return
    config = {'configurable': {'thread_id': 'sessao-local'}, 'recursion_limit': 20}
    print('SmartHelp AI — digite sair para encerrar.')
    while True:
        try:
            pergunta = input('\nVocê: ').strip()
            if pergunta.lower() == 'sair':
                break
            if not pergunta:
                continue
            resposta = agente.invoke({'messages': [{'role': 'user', 'content': pergunta}]}, config)
            print('Agente:', resposta['messages'][-1].content)
        except (KeyboardInterrupt, EOFError):
            break
        except Exception as erro:
            print(f'Não foi possível responder: {erro}')


if __name__ == '__main__':
    main()
