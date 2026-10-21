# 📊 Aplicação Analítica Interativa de Vendas — 1º Semestre de 2026

Uma aplicação analítica web desenvolvida em Python e Streamlit para substituição de relatórios estáticos manuais. O sistema oferece visualização em tempo real de Key Performance Indicators (KPIs), evolução de vendas e comportamento de categorias e regiões com filtros interativos, sem a necessidade de alteração de código por parte dos utilizadores de negócio.

## 🎯 Objetivos do Projeto

- **Automação Analítica:** Substituir processos manuais de geração de dados por um pipeline centralizado e dinâmico.
- **Interatividade & Autonomia:** Permitir aos stakeholders explorar indicadores por regiões e categorias através de uma interface intuitiva no navegador.
- **Monitorização Estratégica:** Acompanhar de forma ágil métricas essenciais como Receita, Lucro, Ticket Médio e Margem de Lucro.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Distribuição:** Anaconda / Jupyter Environment
- **Análise & Manipulação de Dados:** Pandas, NumPy
- **Visualização Web Interativa:** Streamlit, Plotly Express
- **Visualização Estática (Notebook):** Matplotlib

## 📊 Estrutura de Métricas e Visualizações

### Indicadores (KPIs)

1. **Receita Total:** Valor bruto acumulado de vendas.
2. **Lucro Total:** Receita total subtraída dos custos operacionais simulados.
3. **Número de Pedidos:** Total de transações únicas registradas.
4. **Ticket Médio:** Receita média gerada por pedido.
5. **Margem de Lucro (%):** Percentual do lucro em relação à receita.

### Gráficos

- **Evolução Mensal da Receita:** Gráfico de linha temporal.
- **Receita por Categoria:** Gráfico de barras verticais.
- **Receita por Região:** Gráfico de barras verticais organizadas por ordem de receita.
- **Top 3 Produtos mais Vendidos:** Gráfico de barras horizontais destacando os líderes de faturação.

## 🚀 Tutorial de Preparação do Ambiente e Execução

Abaixo encontra-se o passo a passo completo para configurar o seu ambiente no Anaconda e executar a aplicação web.

### 1. Pré-requisitos

Certifique-se de ter o Anaconda Distribution instalado no seu sistema (Windows, macOS ou Linux).

### 2. Abrir o Terminal ou Anaconda Prompt

- **Windows:** Abra o menu Iniciar e procure por **Anaconda Prompt**.
- **macOS / Linux:** Abra o terminal padrão do sistema (se o Anaconda estiver adicionado ao `PATH`) ou o Anaconda Navigator.

### 3. Instalar as Bibliotecas Necessárias

No terminal/prompt de comando, execute o seguinte comando para garantir que possui o Streamlit e o Plotly instalados no ambiente ativo:

```bash
pip install streamlit plotly pandas numpy matplotlib
```

*(Nota: Caso utilize ambientes virtuais dedicados do Conda, certifique-se de ativar o ambiente desejado antes da instalação via `conda activate <nome_do_ambiente>`)*.

## 📂 Organização dos Ficheiros

Para o projeto funcionar corretamente, organize a sua pasta de trabalho da seguinte forma:

```text
dashboard_vendas_web/
├── dashboard_vendas_visual.ipynb   # Notebook Jupyter (para análise exploratória / prototipagem)
├── dashboard_vendas.py                 # Arquivo do código principal da aplicação Streamlit
└── README.md              # Documentação do projeto
```

## 💻 Como Executar a Aplicação Web

Como o Streamlit cria um servidor web, ele não deve ser executado célula a célula dentro do Jupyter Notebook. Siga os passos abaixo:

1. Guarde o código da aplicação num ficheiro chamado `dashboard_vendas.py` na pasta do seu projeto.
2. Abra o **Anaconda Prompt** ou Terminal.
3. Navegue até à pasta onde o ficheiro `dashboard_vendas.py` está guardado usando o comando `cd`:
   ```bash
   cd /caminho/para/sua/pasta/dashboard_vendas_web/
   ```
4. Inicie o servidor do Streamlit executando:
   ```bash
   streamlit run dashboard_vendas.py ou app.py
   ```
5. O terminal exibirá mensagens de inicialização e o seu navegador padrão será aberto automaticamente no endereço:
   `http://localhost:8501`

## 💡 Dicas de Uso para o Usuário Final

- **Filtros Laterais:** Utilize os menus na barra lateral (*sidebar*) para selecionar uma ou mais Regiões e Categorias de produtos. Todos os cartões de KPI e gráficos serão atualizados instantaneamente.
- **Interatividade nos Gráficos:** Passe o cursor sobre as linhas e barras para visualizar os valores exatos de receita e lucro.
- **Visualização de Dados Brutos:** Expanda o painel `"📋 Exibir Tabela Detalhada de Vendas"` no fundo da página para inspecionar ou ordenar o DataFrame diretamente na interface.
