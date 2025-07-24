from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Configuração do banco de dados
agent_storage: str = "tmp/agents.db"

# Agente Web com Claude (que suporta ferramentas)
web_agent = Agent(
    name="Claude Web Agent",
    model=OpenAIChat(
        id="anthropic/claude-3.5-sonnet",
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        extra_headers={
            "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
            "X-Title": "Agno Agent UI"
        }
    ),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources", "Responda sempre em português brasileiro"],
    storage=SqliteStorage(table_name="claude_web_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Agente Financeiro com Claude
finance_agent = Agent(
    name="Claude Finance Agent",
    model=OpenAIChat(
        id="anthropic/claude-3.5-sonnet",
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        extra_headers={
            "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
            "X-Title": "Agno Agent UI"
        }
    ),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data", "Responda sempre em português brasileiro"],
    storage=SqliteStorage(table_name="claude_finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Agente Geral com Claude
general_agent = Agent(
    name="Claude General Agent",
    model=OpenAIChat(
        id="anthropic/claude-3.5-sonnet",
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
    storage=SqliteStorage(table_name="claude_general_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Criar o playground com agentes que suportam ferramentas
playground = Playground(agents=[web_agent, finance_agent, general_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve("playground:app", reload=True) 