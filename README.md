# Data Quality Pipeline & Observability

## Visão Geral do Projeto
Dados inconsistentes levam a decisões erradas. Este projeto demonstra a implementação de um **Framework de Data Quality** para garantir que apenas dados confiáveis cheguem ao Data Warehouse. 

O foco aqui é **Governança de Dados**, criando um processo automatizado de auditoria que separa registros íntegros de anomalias, garantindo a confiabilidade de dashboards gerenciais.

## Stack Tecnológica
* **Linguagem:** Python (Pandas & Numpy) & SQL Avançado.
* **Conceitos Aplicados:** Data Observability, Governança de Dados, Tratamento de Anomalias, Auditoria de ETL.
* **Ecossistema:** Simulação de Jobs AWS Glue / ClickHouse para processamento de alto volume.

## Estrutura do Repositório

### 1. Auditoria de Dados (`scripts/quality_audit_engine.py`)
Um script de pré-processamento que valida cada registro antes da carga final.
* **Testes Executados:** Verificação de unicidade (PK), integridade de campos obrigatórios (Null check) e validação de regras de negócio (Anomalias financeiras).
* **Resultado:** Os dados são classificados com uma flag de validade e encaminhados para "Gold" ou "Quarentena".

### 2. Monitoramento de Saúde (`scripts/data_health_monitor.sql`)
Query analítica para monitorar a confiabilidade da ingestão ao longo do tempo.
* **Métrica Principal:** *Data Reliability Score (%)*, fornecendo uma visão clara da saúde dos pipelines para gestores técnicos e stakeholders de negócio.

## Valor para o Negócio
A implementação de uma camada de observabilidade reduz o custo de manutenção de relatórios e evita prejuízos financeiros causados por decisões baseadas em dados duplicados ou incorretos. É o alicerce fundamental para uma cultura *Data-Driven* real.
