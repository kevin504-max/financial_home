# 🏡 Escopo de Implementação para Sistema de Gestão de Gastos Residenciais (2 Desenvolvedores)

## 🎯 Objetivo:

Desenvolver um sistema completo e intuitivo para gerenciar os `gastos residenciais`, visando otimizar o controle financeiro e facilitar a tomada de decisões.

**🛠️ Funcionalidades:**

1. **📝 Cadastro:**
* Moradia: Registro do endereço, tipo e área da residência.
* Pessoas: Cadastro dos moradores, suas rendas e responsabilidades financeiras.
* Contas: Registro de fornecedores, tipo de conta (fixa ou variável), datas de vencimento e valores médios.
* Categorias: Classificação das despesas em alimentação, transporte, lazer, etc.
* Formas de pagamento: Inclusão de métodos como dinheiro, cartão, pix, etc.

2. **💸 Lançamentos:**
* Entradas: Registro de salários, rendas e outras fontes de receita.
* Saídas: Inclusão de despesas com contas, compras, etc.
* Importação de transações bancárias: Automatização da entrada de dados.
* Geolocalização de despesas: Visualização dos gastos por local.
* Fotos de comprovantes: Anexação para controle e organização. (?)

3. **📊 Controle e Análises:**
* Painel financeiro: Visão geral dos gastos e receitas, com gráficos e indicadores.
* Relatórios personalizáveis: Geração de relatórios por categoria, período, forma de pagamento, etc.
* Filtros e segmentação: Análise detalhada de gastos específicos.
* Metas financeiras: Definição e acompanhamento de objetivos de economia. (?)
* Alertas de gastos excessivos: Notificações para evitar desequilíbrio financeiro.

4. **🔗 Intgrações: (?)**
* Aplicativos bancários: Sincronização automática de transações.
* Assistentes virtuais: Controle de despesas por voz.
* Planilhas eletrônicas: Exportação de dados para análise externa.

5. **🔒 Segurança:**
* Login seguro: Autenticação multifator para proteger dados.
* Criptografia de dados: Armazenamento seguro de informações financeiras.
* Backups regulares: Prevenção contra perda de dados.

## 💻 Etapas do Projeto:

1. **📋 Especificação de Requisitos:**
* Levantamento de necessidades junto ao cliente.
* Definição de funcionalidades e características do sistema.
* Documentação detalhada dos requisitos.

2. **🏗️ Projeto de Arquitetura:**
* Definição da arquitetura do sistema.
* Escolha de tecnologias, base de dados e interface do usuário.

3. **🛠️ Implementação:**
* Desenvolvimento do sistema conforme a arquitetura definida.
* Testes unitários e de integração.
* Correção de bugs e ajustes.

4. **🔍 Testes funcionais:**
* Testes funcionais, de usabilidade, carga e performance.
* Garantia da qualidade do sistema.

5. **🚀 Entrega:**
* Entrega dos fontes e executável do projeto.
* Documentação completa do sistema.
* Manual do usuário.


## **📊 Tabelas da Base de Dados:**

### 1. Usuário
Guarda as informações dos membros da residência que podem registrar os gastos.

| Campo    | Tipo     | Descrição                    |
|----------|----------|------------------------------|
| `id`     | INT (PK) | Identificador único do usuário|
| `nome`   | VARCHAR  | Nome do usuário               |
| `email`  | VARCHAR  | Email do usuário (opcional)   |
| `senha`  | VARCHAR  | Senha do usuário (opcional)   |

### 2. Gasto
Tabela central que armazena os registros de gastos.

| Campo                | Tipo     | Descrição                           |
|----------------------|----------|--------------------------------------|
| `id`                 | INT (PK) | Identificador único do gasto         |
| `descricao`          | VARCHAR  | Descrição do gasto                   |
| `valor`              | DECIMAL  | Valor do gasto                       |
| `data`               | DATE     | Data em que o gasto ocorreu          |
| `categoria_id`       | INT (FK) | Referência à tabela de categorias    |
| `usuario_id`         | INT (FK) | Referência à tabela de usuários      |
| `recorrencia_id`     | INT (FK) | Referência à tabela de recorrência   |
| `metodo_pagamento_id`| INT (FK) | Referência à tabela de método de pagamento |

### 3. Categoria
Tabela opcional para categorizar os gastos (ex: alimentação, contas, lazer, etc.).

| Campo    | Tipo     | Descrição                            |
|----------|----------|---------------------------------------|
| `id`     | INT (PK) | Identificador único da categoria      |
| `nome`   | VARCHAR  | Nome da categoria                    |

### 4. Recorrência
Guarda informações sobre a periodicidade dos gastos recorrentes.

| Campo     | Tipo     | Descrição                            |
|-----------|----------|---------------------------------------|
| `id`      | INT (PK) | Identificador único da recorrência    |
| `nome`    | VARCHAR  | Nome da recorrência (mensal, anual, etc.)|
| `intervalo`| INT     | Intervalo de dias entre as ocorrências|

### 5. Método de Pagamento
Armazena os diferentes métodos utilizados para pagar os gastos.

| Campo    | Tipo     | Descrição                            |
|----------|----------|---------------------------------------|
| `id`     | INT (PK) | Identificador único do método de pagamento |
| `nome`   | VARCHAR  | Nome do método de pagamento (Cartão, Dinheiro, etc.) |

---

## **🛠️ Operações Pertinentes: (Além do CRUD)**

### Operações para **Gasto**:
1. **Filtrar Gastos por Categoria**: Filtrar todos os gastos de uma determinada categoria (ex.: alimentação, contas, lazer).
2. **Filtrar Gastos por Data**: Filtrar os gastos por período (ex.: mensal, anual).
3. **Buscar Gastos Recorrentes**: Listar apenas os gastos que possuem recorrência definida.
4. **Buscar Gastos por Método de Pagamento**: Filtrar os gastos por método de pagamento (ex.: cartão de crédito, dinheiro).
5. **Cálculo Total de Gastos em um Período**: Calcular o total de gastos em um período específico.
6. **Análise de Gastos por Usuário**: Filtrar gastos feitos por um usuário específico.
7. **Exportar Relatório de Gastos**: Exportar os gastos em formato CSV, PDF ou Excel.

### Operações para **Recorrência**:
1. **Gerar Gastos Automáticos Recorrentes**: Gerar automaticamente um novo gasto com base na recorrência quando o período definido expirar.
2. **Atualizar Recorrências**: Alterar as informações de periodicidade dos gastos recorrentes.
3. **Visualizar Próximos Gastos Recorrentes**: Ver a lista de todos os gastos recorrentes que ocorrerão nos próximos 30 dias.

### Operações para **Usuário**:
1. **Divisão de Gastos por Usuário**: Dividir um gasto entre diferentes usuários da residência.
2. **Relatório de Gastos por Usuário**: Gerar relatórios detalhados de gastos por usuário.
3. **Atribuir Gastos a Múltiplos Usuários**: Permitir que um gasto seja atribuído a mais de um usuário.
