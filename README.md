
# 🛒 Análise de Cesta de Mercado — Algoritmo Apriori e MBA


Este projeto implementa uma **Análise de Cesta de Mercado (Market Basket Analysis)** utilizando o **algoritmo Apriori** para identificar **regras de associação entre produtos** em um conjunto de transações de supermercado.

A partir de um dataset sintético (ou real), são descobertos padrões de compra que ajudam a entender **quais produtos tendem a ser adquiridos juntos**, apoiando estratégias de marketing, vendas cruzadas e organização de prateleiras. </br>

## Objetivos Principais
- Aplicar o algoritmo **Apriori** para encontrar itemsets frequentes;  
- Gerar **regras de associação** com base em suporte, confiança e lift;  
- **Visualizar graficamente** os produtos mais vendidos e as principais regras;  
- Explorar e interpretar os resultados de forma crítica e compreensível.


## Tecnologias Utilizadas
- **Python 3.x**
- **Pandas** — manipulação de dados  
- **NumPy** — operações numéricas  
- **Matplotlib** — visualização gráfica  
- **mlxtend** — implementação do Apriori  
- **unidecode** — normalização textual  


## Estrutura do Projeto
```
📂 Projeto_Apriori/
├── dataset_cesta_mercado.csv        # Dataset sintético (gerado automaticamente)
├── mba.py                           # Classe que gera regras de associação
├── regras_apriori.csv               # Saída com regras geradas
├── notebook_apriori.ipynb           # Notebook principal com as células
└── README.md                        # Este arquivo
```


## Etapas do Projeto (Resumo)

1. **Instalação das bibliotecas**
   ```bash
   !pip install -q mlxtend unidecode
   ```

2. **Importação e configuração**
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   from mlxtend.frequent_patterns import apriori
   from mlxtend.preprocessing import TransactionEncoder
   from unidecode import unidecode
   import os
   ```

3. **Geração ou leitura do dataset**
   - O notebook pode gerar 2.500 transações sintéticas automaticamente;  
   - Ou, se preferir, basta carregar um CSV com a estrutura:  
     `data_compra`, `id_compra`, `itens_comprados`.

4. **Pré-processamento e padronização**
   - Conversão para minúsculas, remoção de acentos e limpeza textual.

5. **Transformação para formato transacional**
   - Uso do `TransactionEncoder` para criar o *One-Hot Encoding* das compras.

6. **Execução do Apriori**
   - Aplicação do algoritmo com `min_support` informado pelo usuário.

7. **Geração das regras (MBA)**
   - Utiliza os parâmetros de **confiança mínima** e **lift mínimo**.  
   - Regras no formato:  
     `('arroz',) → ('feijão',)` com suporte/confiança/lift calculados.

8. **Visualizações**
   - Gráfico de barras dos produtos mais frequentes;  
   - Gráfico horizontal das regras com maior lift.

9. **Exportação dos resultados**
   - Arquivo `regras_apriori.csv` contendo todas as regras geradas.


## Exemplo de Saída

### Produtos mais comprados
| Produto | Suporte |
|----------|----------|
| arroz | 0.22 |
| feijão | 0.21 |
| leite | 0.19 |

### Exemplo de Regra
```
('pão',) → ('manteiga',)
Suporte: 0.05 | Confiança: 0.45 | Lift: 2.3
```

## Conclusões
- O algoritmo Apriori é eficiente para encontrar **relações significativas entre produtos**.  
- Mesmo com dados sintéticos, é possível visualizar comportamentos típicos de consumo.  
- Em bases reais, como supermercados ou e-commerces, essas regras ajudam em:
  - Recomendações de compra;
  - Promoções conjuntas;
  - Estratégias de precificação.


## Como Executar o Projeto no Google Colab

1. Acesse: [https://colab.research.google.com](https://colab.research.google.com)
2. Faça upload do notebook (`.ipynb`) e do arquivo `mba.py`.
3. Execute as células em ordem (de 1 a 13).  
4. Ajuste os parâmetros conforme solicitado:
   - `min_support` (ex: `0.01`)
   - `min_confidence` (ex: `0.4`)
   - `min_lift` (ex: `1.0`)
5. Analise os gráficos e o arquivo `regras_apriori.csv` gerado.

