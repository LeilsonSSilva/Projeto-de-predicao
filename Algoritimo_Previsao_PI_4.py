"""
=============================================================================
PROJETO INTEGRADOR - UNIVESP (Ciência de Dados / Engenharia de Computação)
Módulo: Modelo de Aprendizagem de Máquina (Machine Learning)
Objetivo: Prever o consumo energético semanal de um estoque comercial 
          com base em variáveis ambientais (temperatura e umidade).
Estabelecimento Parceiro: On Sale Shop
=============================================================================
"""

# Importação das bibliotecas principais necessárias para manipulação de dados, 
# visualização gráfica, criação do modelo de inteligência artificial e avaliação.
import pandas as pd                  # Biblioteca para manipulação e estruturação de dados em tabelas (DataFrames)
import numpy as np                   # Biblioteca para operações matemáticas e numéricas avançadas
import matplotlib.pyplot as plt      # Biblioteca para geração de gráficos e visualização de dados
import seaborn as sns                # Biblioteca para criação de gráficos estatísticos atraentes
from sklearn.ensemble import RandomForestRegressor  # Algoritmo de Machine Learning (Floresta Aleatória para Regressão)
from sklearn.model_selection import train_test_split  # Função para dividir os dados entre treino e teste
from sklearn.metrics import mean_absolute_error, r2_score # Métricas para medir a precisão e erro do modelo

# Se for utilizar conexão direta ao banco de dados relacional (ex: MySQL/PostgreSQL), descomente a biblioteca necessária:
# from sqlalchemy import create_engine


def carregar_dados_historicos():
    """
    Função para carregar os dados históricos coletados pelos termo-higrômetros 
    e disjuntor inteligente instalados no estoque.
    """
    
    # =========================================================================
    # CÓDIGO REAL DE CONEXÃO AO BANCO DE DADOS (DESCOMENTAR QUANDO EM PRODUÇÃO)
    # =========================================================================
    #
    # 1. Definição das credenciais do Banco de Dados Relacional na Nuvem:
    # usuario = "seu_usuario_aqui"
    # senha = "sua_senha_aqui"
    # host = "seu_servidor_host_aqui.com"
    # porta = "3306"  # Porta padrão MySQL (ou 5432 para PostgreSQL)
    # nome_banco = "onsale_iot_db"
    #
    # 2. String de Conexão com o Banco usando SQLAlchemy:
    # string_conexao = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{nome_banco}"
    # engine = create_engine(string_conexao)
    #
    # 3. Consulta SQL para agrupar e extrair as médias diárias/semanais coletadas pelos sensores:
    # query_sql = """
    #     SELECT 
    #         AVG(temperatura) AS temperatura_media,
    #         AVG(umidade) AS umidade_media,
    #         5 AS dias_operacao,
    #         SUM(consumo_kwh) AS consumo_kwh
    #     FROM sensores_leituras
    #     GROUP BY YEARWEEK(data_hora);
    # """
    #
    # 4. Leitura direta do Banco de Dados para um DataFrame do Pandas:
    # df = pd.read_sql(query_sql, con=engine)
    # return df
    # =========================================================================

    # -------------------------------------------------------------------------
    # DADOS SIMULADOS (UTILIZADOS PARA VALIDAÇÃO DO ALGORITMO ANTES DA CONEXÃO REAL)
    # -------------------------------------------------------------------------
    np.random.seed(42)  # Garante a reprodutibilidade dos dados gerados
    n_semanas = 52      # Simula um histórico de 52 semanas (1 ano de dados)
    
    # Gera valores simulados de temperatura média (23°C a 29°C) e umidade (55% a 80%)
    temperatura_media = np.random.uniform(23.0, 29.0, n_semanas)
    umidade_media = np.random.uniform(55.0, 80.0, n_semanas)
    dias_operacao = np.full(n_semanas, 5)
    
    # Relação física simulada: consumo aumenta conforme a temperatura no estoque eleva
    consumo_energetico_kwh = (
        50 
        + (temperatura_media * 3.5) 
        + (umidade_media * 0.2) 
        + np.random.normal(0, 3, n_semanas)
    )
    
    # Organiza os dados simulados na estrutura de tabela do Pandas
    df = pd.DataFrame({
        'temperatura_media': temperatura_media,
        'umidade_media': umidade_media,
        'dias_operacao': dias_operacao,
        'consumo_kwh': consumo_energetico_kwh
    })
    
    return df  # Retorna a tabela pronta para o modelo


def executar_pipeline_predicao():
    """
    Função principal que orquestra todo o fluxo de Ciência de Dados:
    Carregamento -> Análise Exploratória (Gráfico) -> Separação -> Treinamento -> Avaliação -> Predição Futura.
    """
    print("--- 1. A carregar os dados históricos do estoque ---")
    df = carregar_dados_historicos()  # Obtém os dados (via SQL ou simulação)
    
    # =========================================================================
    # ANÁLISE EXPLORATÓRIA DE DADOS (GERAÇÃO E SALVAMENTO DO GRÁFICO PARA O RELATÓRIO)
    # =========================================================================
    print("--- Gerando gráfico da Análise Exploratória de Dados (AED) ---")
    
    plt.figure(figsize=(8, 5))
    
    # Gráfico de dispersão cruzando Temperatura Média e Consumo Energético
    sns.scatterplot(x='temperatura_media', y='consumo_kwh', data=df, color='royalblue', s=70)
    
    # Configuração de títulos e rótulos dos eixos
    plt.title('Relação entre Temperatura Média do Estoque e Consumo Energético', fontsize=12, fontweight='bold')
    plt.xlabel('Temperatura Média (°C)', fontsize=10)
    plt.ylabel('Consumo de Energia (kWh)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Salva o gráfico em alta resolução para colar no relatório do PI
    plt.savefig('analise_temperatura_consumo.png', dpi=300, bbox_inches='tight')
    plt.show()
    # =========================================================================
    
    # Define as variáveis de entrada (Features / X): o que o modelo vai analisar para tomar a decisão
    X = df[['temperatura_media', 'umidade_media', 'dias_operacao']]
    
    # Define a variável alvo (Target / y): o que o modelo tenta prever (o consumo de energia)
    y = df['consumo_kwh']
    
    # Divide a base de dados: 80% dos dados serão usados para o modelo aprender (treino) 
    # e 20% guardados para testar se ele realmente aprendeu corretamente (teste).
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("--- 2. A treinar o Modelo de Inteligência Artificial (Random Forest) ---")
    # Inicializa o algoritmo Random Forest (composto por 100 árvores de decisão para maior precisão)
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # O comando .fit() realiza o treinamento cruzando as variáveis de clima com o consumo histórico
    modelo.fit(X_train, y_train)
    
    # Pede para o modelo tentar adivinhar o consumo dos 20% de dados reservados para teste
    y_pred = modelo.predict(X_test)
    
    # Calcula a margem de erro média do modelo (MAE - Erro Absoluto Médio em kWh)
    mae = mean_absolute_error(y_test, y_pred)
    
    # Calcula a confiabilidade do modelo (R² - Coeficiente de Determinação, onde valores próximos de 1 indicam alta precisão)
    r2 = r2_score(y_test, y_pred)
    
    print(f"-> Acurácia avaliada | Erro Médio (MAE): {mae:.2f} kWh | Coeficiente R²: {r2:.2f}")
    
    print("--- 3. A calcular a Previsão Energética para a Próxima Semana ---")
    # Captura as médias climáticas recentes registradas pelos termo-higrômetros no estoque
    clima_atual_semana = pd.DataFrame({
        'temperatura_media': [25.7],  # Temperatura média recente dos sensores (°C)
        'umidade_media': [71.1],      # Umidade média recente dos sensores (%)
        'dias_operacao': [5]          # Dias de funcionamento previstos para a semana
    })
    
    # O modelo utiliza o aprendizado anterior para prever o consumo exato em kWh para esta nova condição
    previsao_kwh = modelo.predict(clima_atual_semana)[0]
    
    # Define uma tarifa média de referência por kWh (ex: R$ 0,95) para calcular o impacto financeiro
    tarifa_media_kwh = 0.95 
    custo_previsto = previsao_kwh * tarifa_media_kwh
    
    # Exibe os resultados finais projetados para a gestão financeira da empresa parceira
    print(f">> Consumo Energético Estimado para a próxima semana: {previsao_kwh:.2f} kWh")
    print(f">> Custo Financeiro Previsto para a Gestão: R$ {custo_previsto:.2f}")
    print("--- 4. Processo concluído com sucesso! ---")


# Bloco de execução padrão em Python
if __name__ == "__main__":
    executar_pipeline_predicao()
