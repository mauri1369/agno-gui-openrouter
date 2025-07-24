#!/usr/bin/env python3
"""
Script de teste para verificar a conexão com OpenRouter
"""

import os
from openai import OpenAI

def test_openrouter_connection():
    """Testa a conexão com OpenRouter usando o modelo DeepSeek"""
    
    # Configurar o cliente OpenAI para OpenRouter
    client = OpenAI(
        api_key="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",
        base_url="https://openrouter.ai/api/v1"
    )
    
    try:
        print("🧪 Testando conexão com OpenRouter...")
        
        # Fazer uma chamada de teste
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
                "X-Title": "Agno Agent UI"
            },
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {"role": "user", "content": "Olá! Responda apenas 'Conexão funcionando!' em português."}
            ],
            max_tokens=50
        )
        
        # Verificar a resposta
        if response.choices and response.choices[0].message:
            print("✅ Conexão com OpenRouter funcionando!")
            print(f"📝 Resposta: {response.choices[0].message.content}")
            print(f"🔢 Tokens usados: {response.usage.total_tokens}")
            return True
        else:
            print("❌ Resposta vazia do OpenRouter")
            return False
            
    except Exception as e:
        print(f"❌ Erro na conexão com OpenRouter: {e}")
        return False

def test_claude_connection():
    """Testa a conexão com Claude via OpenRouter"""
    
    client = OpenAI(
        api_key="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",
        base_url="https://openrouter.ai/api/v1"
    )
    
    try:
        print("\n🤖 Testando conexão com Claude...")
        
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
                "X-Title": "Agno Agent UI"
            },
            model="anthropic/claude-3.5-sonnet",
            messages=[
                {"role": "user", "content": "Olá! Responda apenas 'Claude funcionando!' em português."}
            ],
            max_tokens=50
        )
        
        if response.choices and response.choices[0].message:
            print("✅ Conexão com Claude funcionando!")
            print(f"📝 Resposta: {response.choices[0].message.content}")
            print(f"🔢 Tokens usados: {response.usage.total_tokens}")
            return True
        else:
            print("❌ Resposta vazia do Claude")
            return False
            
    except Exception as e:
        print(f"❌ Erro na conexão com Claude: {e}")
        return False

def test_agno_agent():
    """Testa um agente Agno simples"""
    
    try:
        from agno.agent import Agent
        from agno.models.openai import OpenAIChat
        
        print("\n🤖 Testando agente Agno...")
        
        # Criar um agente de teste
        test_agent = Agent(
            name="Test Agent",
            model=OpenAIChat(
                id="deepseek/deepseek-r1-0528:free",
                api_key="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",
                base_url="https://openrouter.ai/api/v1",
                extra_headers={
                    "HTTP-Referer": "https://github.com/agno-agi/agent-ui",
                    "X-Title": "Agno Agent UI"
                }
            ),
            instructions=["Responda sempre em português brasileiro"]
        )
        
        # Testar o agente
        response = test_agent.run("Diga apenas 'Agente Agno funcionando!'")
        
        print("✅ Agente Agno funcionando!")
        print(f"📝 Resposta: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no agente Agno: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando testes de conexão...\n")
    
    # Testar conexão direta com OpenRouter (DeepSeek)
    openrouter_ok = test_openrouter_connection()
    
    # Testar conexão com Claude
    claude_ok = test_claude_connection()
    
    # Testar agente Agno
    agno_ok = test_agno_agent()
    
    print("\n" + "="*50)
    print("📊 RESULTADO DOS TESTES:")
    print(f"OpenRouter (DeepSeek): {'✅ OK' if openrouter_ok else '❌ FALHOU'}")
    print(f"OpenRouter (Claude): {'✅ OK' if claude_ok else '❌ FALHOU'}")
    print(f"Agno Agent: {'✅ OK' if agno_ok else '❌ FALHOU'}")
    
    if openrouter_ok and agno_ok:
        print("\n🎉 Testes principais passaram! Seu setup está funcionando!")
        if claude_ok:
            print("🎉 Claude também funcionando! Você pode usar agentes com ferramentas!")
    else:
        print("\n⚠️  Alguns testes falharam. Verifique a configuração.")
    
    print("="*50) 