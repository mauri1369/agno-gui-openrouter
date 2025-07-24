# 🦙 Guia Ollama com Agno

## 🎯 Visão Geral

Este guia mostra como usar o **Ollama** com o **Agno Framework** para criar agentes de pesquisa com o modelo `deepseek-r1:1.5b` e ferramentas DuckDuckGo.

## 📋 Pré-requisitos

### 1. **Servidor Ollama**

- Servidor Ollama rodando em: `matrix.o2pos.com.br:11434`
- Modelo `deepseek-r1:1.5b` disponível no servidor

### 2. **Dependências Python**

```bash
pip install agno requests duckduckgo-search
```

## 🚀 Configuração

### 1. **Testar Conexão**

Execute o script de teste para verificar se tudo está funcionando:

```bash
python test_ollama.py
```

### 2. **Iniciar Playground**

Para usar os agentes Ollama:

```bash
python playground_ollama.py
```

## 🤖 Agentes Disponíveis

### 1. **Ollama Researcher Agent**

- **Função**: Assistente de pesquisa especializado
- **Ferramentas**: DuckDuckGo Search
- **Características**:
  - Busca informações atualizadas
  - Inclui fontes e referências
  - Respostas em português brasileiro
  - Formatação markdown

### 2. **Ollama Analysis Agent**

- **Função**: Especialista em análise e interpretação
- **Ferramentas**: DuckDuckGo Search
- **Características**:
  - Análises detalhadas e estruturadas
  - Múltiplas perspectivas
  - Uso de tabelas e listas
  - Coleta de dados relevantes

### 3. **Ollama News Agent**

- **Função**: Repórter especializado em notícias
- **Ferramentas**: DuckDuckGo Search
- **Características**:
  - Informações mais recentes
  - Contexto histórico
  - Tom jornalístico objetivo
  - Organização cronológica

## 🔧 Configuração do Modelo

```python
from agno.models.ollama import Ollama

model = Ollama(
    id="deepseek-r1:1.5b",
    host="http://matrix.o2pos.com.br:11434",
    provider="Ollama"
)
```

### Parâmetros Importantes:

- **`id`**: Nome do modelo no Ollama
- **`host`**: Endereço do servidor Ollama
- **`provider`**: Identificador do provedor

## 🛠️ Exemplo de Uso

### Agente Simples

```python
from agno.agent import Agent
from agno.models.ollama import Ollama

agent = Agent(
    name="Meu Agente",
    model=Ollama(
        id="deepseek-r1:1.5b",
        host="http://matrix.o2pos.com.br:11434"
    ),
    instructions=["Responda sempre em português brasileiro"]
)

response = agent.run("Olá! Como você está?")
print(response)
```

### Agente com Ferramentas

```python
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    name="Agente Pesquisador",
    model=Ollama(
        id="deepseek-r1:1.5b",
        host="http://matrix.o2pos.com.br:11434"
    ),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Você é um assistente de pesquisa",
        "Use as ferramentas disponíveis",
        "Responda em português brasileiro"
    ]
)

response = agent.run("Busque informações sobre inteligência artificial")
print(response)
```

## 🌐 URLs de Acesso

- **Interface Web**: http://localhost:3000
- **Playground Ollama**: http://localhost:7777 (via `playground_ollama.py`)
- **Servidor Ollama**: http://matrix.o2pos.com.br:11434

## 🔍 Testes e Verificação

### 1. **Teste de Conexão**

```bash
python test_ollama.py
```

### 2. **Verificar Modelos Disponíveis**

```bash
curl http://matrix.o2pos.com.br:11434/api/tags
```

### 3. **Teste Direto do Modelo**

```bash
curl -X POST http://matrix.o2pos.com.br:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-r1:1.5b",
    "prompt": "Olá! Responda em português."
  }'
```

## 🎯 Casos de Uso

### 1. **Pesquisa Acadêmica**

- Busca de artigos científicos
- Análise de tendências
- Coleta de dados estatísticos

### 2. **Análise de Mercado**

- Pesquisa de concorrentes
- Análise de tendências
- Coleta de notícias do setor

### 3. **Jornalismo**

- Verificação de fatos
- Coleta de informações atualizadas
- Análise de contexto histórico

## ⚠️ Considerações Importantes

### 1. **Performance**

- O modelo `deepseek-r1:1.5b` é otimizado para velocidade
- Respostas podem ser mais rápidas que modelos maiores
- Ideal para tarefas de pesquisa e análise

### 2. **Limitações**

- Modelo menor pode ter limitações em tarefas complexas
- Dependência da conectividade com o servidor Ollama
- Necessidade de verificar disponibilidade do modelo

### 3. **Segurança**

- Dados processados localmente no servidor Ollama
- Maior privacidade comparado a APIs externas
- Controle total sobre o ambiente de inferência

## 🔧 Solução de Problemas

### 1. **Erro de Conexão**

```bash
# Verificar se o servidor está acessível
ping matrix.o2pos.com.br

# Testar porta
telnet matrix.o2pos.com.br 11434
```

### 2. **Modelo Não Encontrado**

```bash
# Listar modelos disponíveis
curl http://matrix.o2pos.com.br:11434/api/tags

# Baixar modelo se necessário
curl -X POST http://matrix.o2pos.com.br:11434/api/pull \
  -H "Content-Type: application/json" \
  -d '{"name": "deepseek-r1:1.5b"}'
```

### 3. **Erro de Ferramentas**

- Verificar se `duckduckgo-search` está instalado
- Testar conectividade com internet
- Verificar se as ferramentas estão sendo importadas corretamente

## 📚 Recursos Adicionais

- [Documentação Oficial do Agno - Ollama](https://docs.agno.com/models/ollama)
- [Exemplo de Agente Ollama](https://dineshr1493.medium.com/all-you-need-to-know-about-the-evolution-of-generative-ai-to-agentic-ai-part-9-agentic-ai-agno-74d74cd0d9f3)
- [Site Oficial do Ollama](https://ollama.com)

---

## 🎉 Status: **PRONTO PARA USO!**

Seu setup Ollama com Agno está configurado e pronto para criar agentes de pesquisa poderosos! 🚀
