#!/bin/bash

echo "🚀 Configurando ambiente Agno com OpenRouter..."

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv .venv

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source .venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

# Criar diretório tmp se não existir
echo "📁 Criando diretório tmp..."
mkdir -p tmp

# Configurar variável de ambiente
echo "🔑 Configurando API key do OpenRouter..."
export OPENROUTER_API_KEY="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"

echo "✅ Configuração concluída!"
echo ""
echo "📋 Para iniciar o playground:"
echo "1. Ative o ambiente virtual: source .venv/bin/activate"
echo "2. Execute: python playground.py"
echo "3. Acesse: http://localhost:7777"
echo ""
echo "🌐 Para conectar a interface web:"
echo "1. Certifique-se de que o Agent UI está rodando: pnpm dev"
echo "2. Acesse: http://localhost:3000"
echo "3. Conecte ao endpoint: http://localhost:7777" 