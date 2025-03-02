# Azure OpenAI no PlayGround

Explore o Playground do Azure OpenAI para gerar conteúdos e compreender as diferentes configurações e parâmetros.

**Azure OpenAI | Inteligência Artificial (IA)**

**Full-Stack | Básico**

[**Playground de chat**](https://pauci-m7r4nsxv-northcentralus.cognitiveservices.azure.com/openai/deployments/gpt-35-turbo-16k/chat/completions?api-version=2024-08-01-preview)

## Objetivo Geral

Vamos aprender a como utilizar o Azure OpenAI no Playground e configurar que precisamos usar para usar o Azure OpenAI.

O objetivo deste desafio é utilizar o Playground do Azure OpenAI para gerar conteúdos e compreender as diferentes configurações e parâmetros.

Explore a demonstração apresentada no conteúdo prático ou faça um resumo do que aprendeu neste conteúdo. 

## Pré-requisitos

* Ter uma conta Azure válida
* Ter Permissão de Administrador para o Azure OpenAI
* Créditos ou método de pagamento pré-configurado

## Conteúdo Programático

* Aprender a como dar deploy num recurso de Azure OpenAI
* Entender sobre como o Azure OpenAI Playground Funciona para multimodalidade
* Aprender sobre configurações do Chat
* Como integrar Blobs e outras informações prévias

## Base e Setup do Azure OpenAI

Primeiramente, deploy. Verifique se você tem o acesso de Admin ou o suficiente para lançar o recurso do OpenAI no Azure.

## Vamos dar deploy em nosso recurso!

* Primeiramente, dê um deploy no Site
* Verifique com o aluno sobre segurança
* Delete o recurso que foi dado deploy
* Depois, mostre o mesmo deploy, só que na CLI

### Tudo certo, vamos ver nossa UI

Agora, vamos ver nossos recursos no Azure AI Foundry!

## Explorando a base do Azure AI Foundry

* Fale o que é o Azure AI Foundry
* Mostre que tem acesso a várias coisas
* Mostre tem acesso aos endpoints e APIs
* Mostre o catalogo de modelos que você pode usar
* Mostre a precificação dos modelos que pode usar e dar deploy
* Dê Deploy no seu recurso

## Explorando o Playground

Mas o quê é o Playground? Primeiramente, vamos entender por qual motivo temos o Playground.

* **O que é o Playground?**
* Ambiente de teste interativo
* Experimentação com modelos
* Ajuste de parâmetros
* Teste de prompts

### Quais os recursos do Playground?

Basicamente, desenvolver prompts e preparar o modelo

* **Recursos Principais**
1. Interface intuitiva
2. Feedback em tempo real
3. Múltiplos modelos disponíveis
4. Configurações ajustáveis

### Antes de pularmos fundo na prática…

Vamos aprender sobre a palavra estocástica

* Elemento de aleatoriedade 
* Variação nas respostas 
* Criatividade vs. Consistência

**Estocástico**: Diz-se dos processos que depenmdem das leis do acaso.

* **Como Funciona?**
1. Análise de probabilidade
2. Seleção de tokens
3. Geração de sequência
4. Influência dos parâmetros

:exclamation: Atenção 
Nota: Mesmo prompt pode gerar respostas diferentes

## Tokenizador

Brincar de [tokenização no OpenAI](https://platform.openai.com/tokenizer) `https://platform.openai.com/tokenizer`. Depois mostra no código o tokenizador

**O que são Tokens?**
* Unidades de texto  
* Palavras e subpalavras
* Números e pontuação
* Caracteres especiais
**Como são Gerados?**
1. Tokenização 
    1. Divisão do texto
    2. Mapeamento para IDs
    3. Processamento

2. Contagem 
    1. Limite por requisição
    2. Custos associados
    3. Otimização

**Quais são os parametros para gerar texto?**
* Temperatura
* Top P
* Tokens máximos
* Penalidades
* Sistema de mensagens

**Vamos aprender sobre variáveis**
* Temperatura
* Top P
* Tokens máximos
* Penalidades
* Sistema de mensagens

## Vamos para o Playground

* Temperatura
* Top P
* Tokens máximos
* Penalidades
* Sistema de mensagens

* **Melhores Práticas**
1. Testar múltiplas vezes
2. Documentar configurações
3. Comparar resultados
4. Iterar com ajustes

* **Perguntas Frequentes**
* Como otimizar tokens?
* Por que respostas variam?
* Qual modelo escolher?

## Configurando o Playground

**Vamos entender essa sopa de Parâmetros agora**
* Temperatura
* Top P
* Tokens máximos
* Penalidades
* Sistema de mensagens

### Agora, vamos praticar!

* Vamos criar e conversar com um blob
* Fazer nosso prompt engineering
* Testar um chat em CLI
* Gerar audio e imagens!

### System Message

* Contexto inicial do modelo
* Definição de comportamento
* Instruções base

* **O que é?**
* Contexto inicial do modelo
* Definição de comportamento
* Instruções base

* **Melhores Práticas**
1. Ser específico
2. Definir tom
3. Estabelecer limites
4. Incluir requisitos

#### Mas como fazer um bom System Message?

Shots! 
* O quê são Shots?
* São maneiras exemplo de como deve se portar a LLM se for agir de tal forma.

#### Mas como fazer um bom System Message?

Zero-Shot
    * Sem exemplos
    * Resposta direta
    * Baseada apenas no prompt

#### Como funciona a formulação?

Resposta Máxima do Modelo e Mensagens Anteriores Incluidas

* Limite de contexto
* Tamanho de resposta 
* Otimização de custos

#### Temperatura vs. Top-P

Como melhorar a criatividade e a criação de respostas diferentes? 
Temperatura: Configuração de pegar palavras enquanto tem a criação de texto, controlando quão randômico são as ligações.

* **Como Funciona?**
1. Análise de probabilidade
2. Seleção de tokens
3. Geração de sequência
4. Influência dos parâmetros

Temperatura 0: Respostas muito previsíveis, determinísticas
Temperatura 1: Respostas muito improváveis, sem sentido

* **Baixa Temperature (0.2)** 
* Fatos técnicos
* Respostas precisas
* Código
* **Alta Temperature (0.8)**
* Criação de conteúdo
* Brainstorming
* Respostas criativas
* **Melhores Práticas**
1. Começar com defaults
2. Ajustar um parâmetro por vez
3. Documentar resultados
4. Iterar baseado em feedback

Top-P: Quais palavras podem ser usadas na possível escolha

* Nucleus sampling 
* Controle de variabilidade 
* Complementa temperatura

Top-P 0.1: Só considera o primeiro eixo de palavras prováveis até dar 10% das possibilidades
Top-P 0.9: Considera muitas palavras até dar o eixo de 90% das possibilidades

:exclamation: Atenção
Nota: Use Top P ou Temperatura, raramente ambos

#### Frequency Penalty vs. Presence Penalty

Que significa isso?

* **Frequency Penalty (-2.0 to 2.0)**   
* Repetição de termos
* Variação vocabular
* Penalidade por frequência
* **Presence Penalty (-2.0 to 2.0)**
* Novos tópicos
* Diversidade temática
* Penalidade por presença

#### Mas Podemos gerar bem mais que texto!

* Como multimodal, podemos gerar muita coisa com esses modelos!
* Ruim: "Faça uma imagem" 
* Bom: "Crie uma imagem de um robô azul amigável, estilo cartoon, em um parque ensolarado"

#### Como fazer boas imagens no Dall-E?

* Clareza
* Especificidade
* Contexto
* Estrutura
* Ruim: "Faça uma imagem" 
* Bom: "Crie uma imagem de um robô azul amigável, estilo cartoon, em um parque ensolarado"

Atenção:exclamation:
Nota: Pessoalmente, recomendo usar o Dall-E somente para prototipar coisas. É muito fácil notar algo feito por IA.

#### Melhores práticas!

* Começar com defaults
* Ajustar um parâmetro por vez
* Documentar resultados
* AIterar baseado em feedback
* **Frequency Penalty (-2.0 to 2.0)**
* Repetição de termos
* Variação vocabular
* Penalidade por frequência
* **Presence Penalty (-2.0 to 2.0)**
* Novos tópicos
* Diversidade temática
* Penalidade por presença

#### Vamos para o Playground

Quando usar cada shot? 
Fazer exemplo zero shot, one shot e multiple shot
Como balancear parâmetros? 
Testar com temp e top p diferentes
Temp alta – top p low e high
Temp baixa – top p low e high
Deixar a temp e top p ok
Ir brincar com o freq. penalty

#### Vamos criar nosso blob!

* **Adicionando Dados ao Blob**
1. Upload de arquivos 
    1 Portal Azure
    2. Azure Storage Explorer
    3. APIs
2. Organização 
   1. Estrutura de pastas
   2. Nomenclatura
   3. Metadados

#### Conectando-se ao Playground e System Messaging

* **Integração com Playground**
1. Conexão
   1. Seleção de fonte
   2. Autenticação
   3. Permissões
2. Validação 
   1. Teste de acesso
   2. Verificação de dados
   3. Logs

#### Criando o nosso chat CLI!

* **Integração com Playground**
1. Conexão
   1. Seleção de fonte
   2. Autenticação
   6. Permissões
2. Validação
   1. Teste de acesso
   2. Verificação de dados
   3. Logs

#### Criando Som e Imagem!

* **Prompt Engineering Básico**
* Princípios
1. Clareza
2. Especificidade
3. Contexto
4. Estrutura
* **Exemplos**
* text
* Copy
* Ruim: "Faça uma imagem" Bom: "Crie uma imagem de um robô azul amigável, estilo cartoon, em um parque ensolarado"

* **Geração de Áudio**
* **Configuração**
1. Selecionar serviço
2. Definir voz
3. Ajustar parâmetros

## Links Úteis

* [Documentação Oficial](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/role-based-access-control)

* [Documentação Oficial](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

* [Documentação Oficial](https://medium.com/@1511425435311/understanding-openais-temperature-and-top-p-parameters-in-language-models-d2066504684f)

* [Documentação Oficial](https://learn.microsoft.com/pt-br/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Cjavascript-keyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-studio)

* [Documentação Oficial](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

* [Documentação Oficial](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart?tabs=command-line%2Cjavascript-keyless%2Ctypescript-keyless%2Cpython-new&pivots=ai-foundry-portal)

* [Documentação Oficial](https://learn.microsoft.com/en-us/azure/ai-services/openai/dall-e-quickstart?tabs=dalle3%2Ccommand-line%2Cjavascript-keyless%2Ctypescript-keyless&pivots=programming-language-studio)

* [Documentação Oficial](https://learn.microsoft.com/en-us/azure/ai-services/openai/text-to-speech-quickstart?tabs=command-line%2Cjavascript-keyless%2Ctypescript-keyless&pivots=programming-language-dotnet)

* [Platform Tokenizerl](https://platform.openai.com/tokenizer)

* [Estocastico](https://www.dicio.com.br/estocastico/)

* [Referências](https://huggingface.co/docs/transformers/llm_tutorial)

##

Projeto desenvolvido durante o [**Bootcamp Microsoft AI for Tech - OpenAI Services**](https://www.dio.me/bootcamp/microsoft-azure-open-ai), fornecido pela [**DIO**](https://www.dio.me/)

##

- [By Páucinha](https://github.com/Paucinha)
