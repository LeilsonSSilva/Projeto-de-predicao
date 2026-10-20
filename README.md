# Sistema IoT em Nuvem para Monitoramento de Ambiente e Predição de Consumo Energético em Estoque Comercial

Relatório Técnico-Científico e Repositório Oficial do Projeto Integrador desenvolvido para os cursos de Engenharia de Computação e Ciência de Dados da Universidade Virtual do Estado de São Paulo (UNIVESP).

---

## 📋 Sobre o Projeto
Este projeto foi desenvolvido em parceria com o estabelecimento comercial **On Sale Shop**. O principal desafio identificado foi a ausência de um monitoramento ambiental contínuo (temperatura e umidade) e a incapacidade de mensurar isoladamente o consumo de energia elétrica do setor de estoque, o que representava riscos para a conservação de produtos eletrônicos e controle de custos.

Como solução, a equipe construiu um ecossistema integrado que combina **Internet das Coisas (IoT)**, **Computação em Nuvem** e **Aprendizagem de Máquina (*Machine Learning*)**.

---

## 🚀 Arquitetura da Solução e Diagrama em Nuvem
O fluxo da solução foi estruturado em quatro camadas principais:
1. **Camada de Hardware & IoT:** Termo-higrômetros e disjuntor inteligente instalados no estoque, integrados em tempo real através da **API Tuya**.
2. **Camada de Persistência:** Base de dados relacional em nuvem estruturada para armazenar as leituras brutas e históricos.
3. **Camada de Processamento & IA:** Script em Python utilizando o algoritmo **Random Forest Regressor** para correlacionar o clima ao consumo energético.
4. **Camada de Apresentação:** Dashboard gerencial com predições de custos e alertas automáticos para a gestora.

<img width="1438" height="736" alt="Arquitetura de Dados" src="https://github.com/user-attachments/assets/b46d9ea1-7876-4c85-9dea-ab113afcdc9b" />


---

## 📈 Análise Exploratória de Dados (AED)
Antes do treino do modelo preditivo, foi realizada uma Análise Exploratória de Dados em Python para compreender a correlação entre as variáveis ambientais e o consumo elétrico. O gráfico gerado automaticamente pelo script (`analise_temperatura_consumo.png`) demonstra o impacto direto da elevação da temperatura no aumento do consumo energético do estoque:

<img width="2128" height="1411" alt="analise_temperatura_consumo" src="https://github.com/user-attachments/assets/e09f079d-5fb4-453e-9290-a62b496fec5d" />



---

## 📊 Dashboard Final e Alertas Automáticos
O painel gerencial consolida as informações em tempo real e exibe as projeções financeiras semanais. Abaixo encontram-se as capturas de tela do sistema em funcionamento, evidenciando as previsões de custo em Reais (R$) e os alertas de temperatura/umidade configurados:

*(Dashboard em construção)*

---

## 📂 Estrutura do Repositório

```text
├── Banco_de_Dados_PI_4.sql        # Script de criação e estruturação do Banco de Dados
├── Algoritmo_Previsao_PI_4.py     # Script em Python com a AED, conexão SQL e modelo de Machine Learning
└── Readmi_PI_4.md                 # Documentação oficial do projeto
