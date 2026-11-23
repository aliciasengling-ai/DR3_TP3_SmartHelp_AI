# SmartHelp AI — DR3 TP3

Autora: Alicia Scripelliti

## Problema e objetivo
Provedores de internet recebem perguntas repetitivas sobre planos e falhas de conexão. O agente auxilia clientes e atendentes consultando um catálogo fictício e orientações locais de suporte. Não acessa sistemas reais nem realiza diagnósticos remotos.

## Arquitetura e implementação
Python, LangChain, Groq e LangGraph. `main.py` integra o modelo, a interface e o agente; `ferramentas.py` define duas ferramentas decoradas com `@tool`. O agente usa o ciclo ReAct: seleciona uma ação, recebe a observação da ferramenta e decide se precisa de outra ação ou se pode responder. InMemorySaver mantém o histórico por thread durante a execução, sem persistência após o encerramento. A chave fica no .env, excluído pelo .gitignore. O código trata erros de configuração e execução.

## Execução (Windows CMD, Python 3.10+)
```bat
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
notepad .env
```
Crie uma chave em https://console.groq.com/keys e preencha GROQ_API_KEY no .env. Caso o modelo padrão esteja indisponível, escolha um modelo Groq com suporte a ferramentas e altere GROQ_MODEL.
```bat
python -m unittest test_ferramentas -v
python main.py
```
Digite `sair` para encerrar.

## Casos de uso e validação
| Entrada | Resultado esperado | Resultado observado |
|---|---|---|
| Quais são os planos? | Catálogo com três planos | Pendente de execução integrada |
| Minha internet está lenta | Orientação de teste por cabo | Pendente de execução integrada |
| Estou sem internet | Verificação e reinício do roteador | Pendente de execução integrada |
| Meu nome é Ana; depois: Qual é meu nome? | Recuperação do nome na mesma sessão | Pendente de execução integrada |
| Qual o preço do plano de 500 Mbps e como resolver lentidão? | Consulta das duas ferramentas | Pendente de execução integrada |

Execute os casos e substitua os estados pendentes pelos resultados reais. Os testes unitários verificam as funções das ferramentas, mas não substituem os testes do agente com o LLM.

## Reflexão
Manualmente, o atendente consultaria o catálogo e o manual de suporte separadamente e precisaria manter o contexto de cada cliente. O agente reúne essas consultas em uma conversa e pode reduzir tarefas repetitivas. A vantagem é qualitativa: não foi medido ganho de tempo. Respostas podem conter erros; casos complexos exigem atendimento humano. Não insira dados pessoais reais.

## Publicação
Publique os arquivos em um repositório público do GitHub, sem incluir .env ou venv. Entregue o link do repositório e o ZIP solicitado.

## Resultados dos testes realizados

O agente SmartHelp AI foi executado com sucesso utilizando o framework LangChain e o modelo openai/gpt-oss-120b, disponibilizado pela API do Groq.

Durante o teste prático de consulta de planos, o agente apresentou corretamente os três planos disponíveis e seus respectivos valores.

Os testes automatizados foram executados em 23/11/2026, apresentando os seguintes resultados:

- Consulta de planos: aprovado.
- Diagnóstico de lentidão: aprovado.
- Diagnóstico de queda de conexão: aprovado.
- Total de testes automatizados: 3.
- Tempo de execução: 0,037 segundos.
- Taxa de aprovação: 100%.

A solução facilita o atendimento ao cliente, reduzindo a necessidade de consultas manuais ao catálogo de planos e aos procedimentos de suporte técnico.