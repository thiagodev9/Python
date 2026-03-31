#Tipos complexos e type hint (dicionarios vs dataframes vs Tabelas vs excel )

"""
                AULA: TIPOS COMPLEXOS E TYPE HINTING
                Dicionários vs DataFrames vs Tabelas
"""

from typing import Dict, Any, List
import pandas as pd

# --- 1. DICIONÁRIOS (A FICHA INDIVIDUAL) ---
# Use Type Hint para dizer que as chaves são Strings e os valores podem ser Qualquer Coisa (Any)
print("--- Exemplo 1: Dicionário ---")

pessoa: Dict[str, Any] = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

print(f"Nome da ficha: {pessoa['nome']}")
print("-" * 30)


# --- 2. DATAFRAMES (O ARQUIVO COMPLETO) ---
# O DataFrame é como uma planilha do Excel viva dentro do Python.
print("--- Exemplo 2: DataFrame (Pandas) ---")

# Criando um DataFrame a partir de uma lista de dicionários
dados_lista: List[Dict[str, Any]] = [
    {"Nome": "Alice", "Idade": 30},
    {"Nome": "Bob", "Idade": 25},
    {"Nome": "Charlie", "Idade": 35}
]

df: pd.DataFrame = pd.DataFrame(dados_lista)

print("Tabela completa:")
print(df)
print("\nEstatísticas rápidas:")
print(df.describe())
print("-" * 30)


# --- 3. EXERCÍCIOS PARA VOCÊ COMPLETAR ---

# EXERCÍCIO 1: 
# Crie uma função com Type Hint que receba um dicionário de produto 
# e retorne uma string formatada.
def formatar_produto(produto: Dict[str, Any]) -> str:
    # Escreva seu código aqui
    pass

# EXERCÍCIO 2:
# No DataFrame 'df' acima, tente filtrar apenas as pessoas com mais de 28 anos.
# Dica: df_filtrado = df[df['Idade'] > 28]

print("Pronto para os exercícios!") 





