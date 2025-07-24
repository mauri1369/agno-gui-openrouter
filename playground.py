from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Configuração do banco de dados
agent_storage: str = "tmp/agents.db"

# Agente Geral com DeepSeek via OpenRouter (sem ferramentas)
general_agent = Agent(
    name="DeepSeek General Agent",
    model=OpenAIChat(
        id="deepseek/deepseek-r1-0528:free",
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        extra_headers={
            "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
            "X-Title": "Agno Agent UI"
        }
    ),
    instructions=[
        "Você é um assistente inteligente e útil",
        "Responda sempre em português brasileiro",
        "Seja claro e conciso em suas respostas",
        "Use formatação markdown quando apropriado"
    ],
    storage=SqliteStorage(table_name="deepseek_general_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Agente de Conversação com DeepSeek
conversation_agent = Agent(
    name="DeepSeek Conversation Agent",
    model=OpenAIChat(
        id="deepseek/deepseek-r1-0528:free",
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        extra_headers={
            "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
            "X-Title": "Agno Agent UI"
        }
    ),
    instructions=[
        "Você é um assistente de conversação amigável",
        "Responda sempre em português brasileiro",
        "Mantenha conversas naturais e envolventes",
        "Ajude com perguntas gerais e curiosidades"
    ],
    storage=SqliteStorage(table_name="deepseek_conversation_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Agente de Análise com DeepSeek
analysis_agent = Agent(
    name="DeepSeek Analysis Agent",
    model=OpenAIChat(
        id="deepseek/deepseek-r1-0528:free",
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        extra_headers={
            "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
            "X-Title": "Agno Agent UI"
        }
    ),
    instructions=[
        "Você é um especialista em análise e resolução de problemas",
        "Responda sempre em português brasileiro",
        "Forneça análises detalhadas e bem estruturadas",
        "Use formatação markdown para organizar informações"
    ],
    storage=SqliteStorage(table_name="deepseek_analysis_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Criar o playground com agentes compatíveis
playground = Playground(agents=[general_agent, conversation_agent, analysis_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve("playground:app", reload=True) 