from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

# Configuração do banco de dados
agent_storage: str = "tmp/agents.db"

# Agente Pesquisador com Ollama (DeepSeek R1 1.5B)
researcher_agent = Agent(
    name="Ollama Researcher Agent",
    model=Ollama(
        id="deepseek-r1:1.5b",
        host="http://matrix.o2pos.com.br:11434",
        provider="Ollama"
    ),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Você é um assistente de pesquisa especializado",
        "Responda sempre em português brasileiro",
        "Use as ferramentas de busca para encontrar informações atualizadas",
        "Sempre inclua fontes e referências nas suas respostas",
        "Seja preciso e objetivo em suas análises",
        "Use formatação markdown para organizar informações"
    ],
    storage=SqliteStorage(table_name="ollama_researcher_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Agente de Análise com Ollama
analysis_agent = Agent(
    name="Ollama Analysis Agent",
    model=Ollama(
        id="deepseek-r1:1.5b",
        host="http://matrix.o2pos.com.br:11434",
        provider="Ollama"
    ),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Você é um especialista em análise e interpretação de dados",
        "Responda sempre em português brasileiro",
        "Use ferramentas de busca para coletar dados relevantes",
        "Forneça análises detalhadas e bem estruturadas",
        "Apresente diferentes perspectivas sobre os tópicos",
        "Use tabelas e listas para organizar informações"
    ],
    storage=SqliteStorage(table_name="ollama_analysis_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Agente de Notícias com Ollama
news_agent = Agent(
    name="Ollama News Agent",
    model=Ollama(
        id="deepseek-r1:1.5b",
        host="http://matrix.o2pos.com.br:11434",
        provider="Ollama"
    ),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Você é um repórter especializado em notícias e atualidades",
        "Responda sempre em português brasileiro",
        "Busque as informações mais recentes sobre os tópicos",
        "Forneça contexto histórico quando relevante",
        "Mantenha um tom jornalístico objetivo",
        "Organize as informações por relevância e cronologia"
    ],
    storage=SqliteStorage(table_name="ollama_news_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Criar o playground com agentes Ollama
playground = Playground(agents=[researcher_agent, analysis_agent, news_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve("playground:app", reload=True) 