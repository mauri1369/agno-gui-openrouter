# 🚀 Configuração do Agno com OpenRouter e DeepSeek

Este guia mostra como configurar o Agno para usar o modelo DeepSeek via OpenRouter.

## 📋 Pré-requisitos

- Python 3.8+
- Node.js e pnpm (já configurados)
- Chave API do OpenRouter

## 🔧 Configuração Rápida

### 1. Execute o script de configuração:

```bash
./setup_agno.sh
```

### 2. Ou configure manualmente:

#### Criar ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Instalar dependências:

```bash
pip install -r requirements.txt
```

#### Criar diretório tmp:

```bash
mkdir -p tmp
```

## 🎯 Configuração dos Agentes

O arquivo `playground.py` já está configurado com:

### 🤖 Agentes Disponíveis:

1. **DeepSeek Web Agent**

   - Modelo: `deepseek/deepseek-r1-0528:free`
   - Ferramentas: DuckDuckGo para busca na web
   - Instruções: Sempre incluir fontes e responder em português

2. **DeepSeek Finance Agent**

   - Modelo: `deepseek/deepseek-r1-0528:free`
   - Ferramentas: YFinance para dados financeiros
   - Instruções: Usar tabelas para exibir dados

3. **DeepSeek General Agent**
   - Modelo: `deepseek/deepseek-r1-0528:0528:free`
   - Ferramentas: Nenhuma (conversação geral)
   - Instruções: Assistente inteligente em português

## 🚀 Como Executar

### 1. Iniciar o Playground (Backend):

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Executar playground
python playground.py
```

O playground estará disponível em: **http://localhost:7777**

### 2. Iniciar a Interface Web (Frontend):

```bash
# Em outro terminal
pnpm dev
```

A interface estará disponível em: **http://localhost:3000**

### 3. Conectar Interface ao Playground:

1. Acesse http://localhost:3000
2. Clique no endpoint (geralmente mostra localhost:7777)
3. Se não estiver conectado, clique para editar e configure: `http://localhost:7777`
4. Selecione um dos agentes disponíveis
5. Comece a conversar!

## 🔑 Configuração da API Key

A API key do OpenRouter já está configurada no `playground.py`:

```python
api_key="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"
```

## 🛠️ Personalização

### Adicionar Novos Agentes:

Edite o `playground.py` e adicione novos agentes:

```python
novo_agente = Agent(
    name="Meu Agente",
    model=OpenAIChat(
        id="deepseek/deepseek-r1-0528:free",
        api_key="sua-api-key",
        api_base="https://openrouter.ai/api/v1"
    ),
    instructions=["Suas instruções aqui"],
    storage=SqliteStorage(table_name="meu_agente", db_file=agent_storage),
    # ... outras configurações
)
```

### Usar Outros Modelos do OpenRouter:

Substitua o `id` do modelo por qualquer um disponível no OpenRouter:

```python
model=OpenAIChat(
    id="anthropic/claude-3.5-sonnet",  # Claude
    # ou
    id="meta-llama/llama-3.1-8b-instruct",  # Llama
    # ou
    id="google/gemini-pro",  # Gemini
    api_key="sua-api-key",
    api_base="https://openrouter.ai/api/v1"
)
```

## 📊 Monitoramento

- **Logs**: O playground mostra logs detalhados no terminal
- **Banco de dados**: As conversas são salvas em `tmp/agents.db`
- **Interface**: Use a interface web para visualizar histórico e interagir

## 🔧 Solução de Problemas

### Erro de conexão:

- Verifique se o playground está rodando na porta 7777
- Confirme se a API key está correta
- Verifique se o modelo está disponível no OpenRouter

### Erro de dependências:

```bash
pip install --upgrade -r requirements.txt
```

### Limpar banco de dados:

```bash
rm tmp/agents.db
```

## 📚 Recursos Adicionais

- [Documentação do Agno](https://docs.agno.com/)
- [OpenRouter Models](https://openrouter.ai/models)
- [Agent UI Repository](https://github.com/agno-agi/agent-ui)

## 🎉 Pronto!

Agora você tem um ambiente completo do Agno configurado com o modelo DeepSeek via OpenRouter, pronto para uso!
