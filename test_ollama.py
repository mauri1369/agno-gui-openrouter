#!/usr/bin/env python3
"""
Script de teste para verificar a conexão com Ollama
"""

import requests
from agno.agent import Agent
from agno.models.ollama import Ollama

def test_ollama_connection():
    """Testa a conexão direta com o servidor Ollama"""
    
    try:
        print("🧪 Testando conexão com Ollama...")
        
        # Testar se o servidor está respondendo
        response = requests.get("http://matrix.o2pos.com.br:11434/api/tags", timeout=10)
        
        if response.status_code == 200:
            print("✅ Servidor Ollama está respondendo!")
            
            # Listar modelos disponíveis
            models = response.json()
            print(f"📋 Modelos disponíveis: {len(models.get('models', []))}")
            
            for model in models.get('models', []):
                print(f"  - {model.get('name', 'N/A')}")
            
            return True
        else:
            print(f"❌ Servidor respondeu com status: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na conexão com Ollama: {e}")
        return False

def test_ollama_model():
    """Testa o modelo específico deepseek-r1:1.5b"""
    
    try:
        print("\n🤖 Testando modelo deepseek-r1:1.5b...")
        
        # Criar um agente de teste
        test_agent = Agent(
            name="Test Agent",
            model=Ollama(
                id="deepseek-r1:1.5b",
                host="http://matrix.o2pos.com.br:11434",
                provider="Ollama"
            ),
            instructions=["Responda sempre em português brasileiro"]
        )
        
        # Testar o agente
        response = test_agent.run("Diga apenas 'Modelo Ollama funcionando!'")
        
        print("✅ Modelo Ollama funcionando!")
        print(f"📝 Resposta: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no modelo Ollama: {e}")
        return False

def test_ollama_with_tools():
    """Testa o agente Ollama com ferramentas DuckDuckGo"""
    
    try:
        from agno.tools.duckduckgo import DuckDuckGoTools
        
        print("\n🔍 Testando agente Ollama com ferramentas...")
        
        # Criar um agente com ferramentas
        research_agent = Agent(
            name="Research Test Agent",
            model=Ollama(
                id="deepseek-r1:1.5b",
                host="http://matrix.o2pos.com.br:11434",
                provider="Ollama"
            ),
            tools=[DuckDuckGoTools()],
            instructions=[
                "Você é um assistente de pesquisa",
                "Responda sempre em português brasileiro",
                "Use as ferramentas disponíveis quando necessário"
            ]
        )
        
        # Testar o agente
        response = research_agent.run("Busque informações sobre inteligência artificial e resuma em 2 frases.")
        
        print("✅ Agente Ollama com ferramentas funcionando!")
        print(f"📝 Resposta: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no agente com ferramentas: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando testes do Ollama...\n")
    
    # Testar conexão com servidor
    server_ok = test_ollama_connection()
    
    # Testar modelo específico
    model_ok = test_ollama_model()
    
    # Testar com ferramentas
    tools_ok = test_ollama_with_tools()
    
    print("\n" + "="*50)
    print("📊 RESULTADO DOS TESTES:")
    print(f"Servidor Ollama: {'✅ OK' if server_ok else '❌ FALHOU'}")
    print(f"Modelo deepseek-r1:1.5b: {'✅ OK' if model_ok else '❌ FALHOU'}")
    print(f"Agente com ferramentas: {'✅ OK' if tools_ok else '❌ FALHOU'}")
    
    if server_ok and model_ok:
        print("\n🎉 Testes principais passaram! Seu setup Ollama está funcionando!")
        if tools_ok:
            print("🎉 Ferramentas também funcionando! Você pode usar o playground_ollama.py!")
    else:
        print("\n⚠️  Alguns testes falharam. Verifique a configuração.")
    
    print("="*50) 