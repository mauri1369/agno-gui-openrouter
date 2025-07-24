# Agno Agent UI - Interface de Chat para Agentes de IA

Uma interface moderna de chat para agentes de IA construída com Next.js, Tailwind CSS e TypeScript. Este template fornece uma UI pronta para uso para interagir com agentes Agno.

## 🚀 Características

- 💬 **Interface de Chat Moderna**: Design limpo com suporte a streaming em tempo real
- 🧩 **Suporte a Chamadas de Ferramentas**: Visualiza chamadas de ferramentas do agente e seus resultados
- 🧠 **Passos de Raciocínio**: Exibe o processo de raciocínio do agente (quando disponível)
- 📚 **Suporte a Referências**: Mostra fontes utilizadas pelo agente
- 🖼️ **Suporte Multi-modal**: Gerencia diversos tipos de conteúdo incluindo imagens, vídeo e áudio
- 🎨 **UI Customizável**: Construída com Tailwind CSS para fácil estilização
- 🧰 **Construída com Stack Moderna**: Next.js, TypeScript, shadcn/ui, Framer Motion e mais

## 📋 Pré-requisitos

Antes de configurar o Agent UI, você pode querer ter um Agno Playground rodando. Se você ainda não configurou o Agno Playground, siga o [guia oficial](https://agno.link/agent-ui#connect-to-local-agents) para executar o Playground localmente.

## 🛠️ Instalação

### Instalação Automática (Recomendada)

```bash
npx create-agent-ui@latest
```

### Instalação Manual

1. Clone o repositório:

```bash
git clone https://github.com/agno-agi/agent-ui.git
cd agent-ui
```

2. Instale as dependências:

```bash
pnpm install
```

3. Inicie o servidor de desenvolvimento:

```bash
pnpm dev
```

4. Abra [http://localhost:3000](http://localhost:3000) no seu navegador para ver o resultado.

## 🔗 Conectando a um Backend de Agente

Por padrão, o Agent UI se conecta a `http://localhost:7777`. Você pode facilmente alterar isso passando o mouse sobre a URL do endpoint e clicando na opção de edição.

O endpoint padrão funciona com a configuração padrão do Agno Playground descrita na [documentação oficial](https://agno.link/agent-ui#connect-to-local-agents).

## 🧪 Testando o Projeto

Para testar se tudo está funcionando:

1. Certifique-se de que o servidor está rodando:

```bash
pnpm dev
```

2. Acesse http://localhost:3000 no seu navegador

3. Você deve ver a interface de chat do Agno Agent UI

## 📦 Scripts Disponíveis

- `pnpm dev` - Inicia o servidor de desenvolvimento
- `pnpm build` - Constrói o projeto para produção
- `pnpm start` - Inicia o servidor de produção
- `pnpm lint` - Executa o linter
- `pnpm lint:fix` - Corrige problemas do linter
- `pnpm format` - Verifica a formatação do código
- `pnpm format:fix` - Corrige a formatação do código
- `pnpm typecheck` - Verifica os tipos TypeScript
- `pnpm validate` - Executa lint, format e typecheck

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, veja [CONTRIBUTING.md](./CONTRIBUTING.md) para diretrizes de contribuição.

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](./LICENSE).

## 🔗 Links Úteis

- [Repositório Original](https://github.com/agno-agi/agent-ui)
- [Documentação do Agno](https://agno.link/agent-ui#connect-to-local-agents)
- [Demo Online](https://agno-agent-ui.vercel.app)
