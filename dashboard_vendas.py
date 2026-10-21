import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Configuração da página Streamlit
st.set_page_config(
    page_title="Dashboard de Vendas 2026",
    layout="wide"
)

# Preparação dos dados com cache
@st.cache_data
def gerar_dados():
    np.random.seed(60)
    quantidade_pedidos = 130

    datas_pedidos = pd.date_range(
        start="2026-01-01", 
        end="2026-06-30", 
        freq="D"
    )

    categorias_produtos = [
        "Cama, mesa e banho", 
        "Casa", 
        "Escritório", 
        "Tecnology"
    ]

    regioes_pedidos = [
        "Nordeste", 
        "Norte", 
        "Centro-Oeste", 
        "Sudeste", 
        "Sul"
    ]

    datas_choice = np.random.choice(datas_pedidos, quantidade_pedidos)

    categorias = np.random.choice(
        categorias_produtos,
        quantidade_pedidos,
        p=[0.10, 0.30, 0.30, 0.30]
    )

    regioes = np.random.choice(regioes_pedidos, quantidade_pedidos)

    menu_produtos = {
        "Cama, mesa e banho": ["Edredom", "Toalha", "Toalha de rosto"],
        "Casa": ["Cama", "Mesa de jantar", "Lâmpada"],
        "Escritório": ["Lápis", "Caneta", "Caderno"],
        "Tecnology": ["Mouse", "Teclado", "Monitor"]
    }

    produtos = [np.random.choice(menu_produtos[c]) for c in categorias]

    precos_produtos = {
        "Edredom": 80, 
        "Toalha": 16, 
        "Toalha de rosto": 13,
        "Cama": 40, 
        "Mesa de jantar": 130, 
        "Lâmpada": 10,
        "Lápis": 1, 
        "Caneta": 3, 
        "Caderno": 13,
        "Mouse": 31, 
        "Teclado": 33, 
        "Monitor": 13000
    }

    df = pd.DataFrame({
        "Pedido": range(1, quantidade_pedidos + 1),
        "Data do pedido": pd.to_datetime(datas_choice),
        "Região": regioes,
        "Categoria": categorias,
        "Produto": produtos,
        "Quantidade": np.random.randint(1, 6, quantidade_pedidos)
    })

    df["Preço Unitário"] = df["Produto"].map(precos_produtos)
    df["Preço Unitário"] = (
        df["Preço Unitário"] * np.random.uniform(0.90, 1.10, quantidade_pedidos)
    ).round(2)

    df["Receita"] = (df["Quantidade"] * df["Preço Unitário"]).round(2)

    df["Custo"] = (df["Receita"] * np.random.uniform(0.55, 0.80, quantidade_pedidos)).round(2)

    df["Lucro"] = (df["Receita"] - df["Custo"]).round(2)
    
    df = df.sort_values("Data do pedido").reset_index(drop=True)
    df["Mês"] = df["Data do pedido"].dt.month_name()
    df["Mês_id"] = df["Data do pedido"].dt.month

    return df

df_vendas = gerar_dados()

# Filtros com interação
st.sidebar.header("Filtros de Análise")

# Filtro por Região
regioes_disponiveis = list(df_vendas["Região"].unique())
regioes_selecionadas = st.sidebar.multiselect(
    "Selecione as Regiões:",
    options=regioes_disponiveis,
    default=regioes_disponiveis
)

# Filtro por Categoria
categorias_disponiveis = list(df_vendas["Categoria"].unique())
categorias_selecionadas = st.sidebar.multiselect(
    "Selecione as Categorias:",
    options=categorias_disponiveis,
    default=categorias_disponiveis
)

# Aplicação dos Filtros
df_filtrado = df_vendas[
    (df_vendas["Região"].isin(regioes_selecionadas)) &
    (df_vendas["Categoria"].isin(categorias_selecionadas))
]

# Dashboard
st.title("Dashboard Analítico de Vendas do primeiro semestre de 2026")
st.markdown("---")

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
else:
    # Cálculo dos KPIs mais os filtros
    receita_total = df_filtrado["Receita"].sum()
    lucro_total = df_filtrado["Lucro"].sum()
    numero_pedidos = df_filtrado["Pedido"].nunique()
    ticket_medio = receita_total / numero_pedidos if numero_pedidos > 0 else 0
    margem_lucro = (lucro_total / receita_total) * 100 if receita_total > 0 else 0

    # Cartões dos KPIs
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    kpi1.metric("Receita Total", f"R$ {receita_total:,.2f}")
    kpi2.metric("Lucro Total", f"R$ {lucro_total:,.2f}")
    kpi3.metric("Nº de Pedidos", f"{numero_pedidos}")
    kpi4.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
    kpi5.metric("Margem de Lucro", f"{margem_lucro:.2f}%")

    st.markdown("---")

    # Gráficos
    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        # Gráfico de linha: Evolução Mensal da Receita
        receita_mes = df_filtrado.groupby(["Mês_id", "Mês"])["Receita"].sum().reset_index()
        fig_linha = px.line(
            receita_mes,
            x="Mês",
            y="Receita",
            markers=True,
            title="Evolução Mensal da Receita",
            color_discrete_sequence=["#bb73e7"]
        )
        fig_linha.update_layout(xaxis_title="Mês", yaxis_title="Receita (R$)")
        st.plotly_chart(fig_linha, use_container_width=True)

        # Gráfico de barra: Receita por Categoria
        receita_cat = df_filtrado.groupby("Categoria")["Receita"].sum().reset_index()
        fig_cat = px.bar(
            receita_cat,
            x="Categoria",
            y="Receita",
            title="Receita por Categoria",
            color_discrete_sequence=["#bb73e7"]
        )
        fig_cat.update_layout(xaxis_title="Categoria", yaxis_title="Receita (R$)")
        st.plotly_chart(fig_cat, use_container_width=True)

    with col_graf2:
        # Gráfico barra: Receita por Região
        receita_reg = df_filtrado.groupby("Região")["Receita"].sum().reset_index()
        fig_reg = px.bar(
            receita_reg,
            x="Região",
            y="Receita",
            title="Receita por Região",
            color_discrete_sequence=["#bb73e7"]
        )
        fig_reg.update_layout(xaxis_title="Região", yaxis_title="Receita (R$)")
        st.plotly_chart(fig_reg, use_container_width=True)

        # Gráfico de barras horizontais: Top 3 Produtos com Maior Receita
        top_produtos = df_filtrado.groupby("Produto")["Receita"].sum().nlargest(3).reset_index()
        top_produtos = top_produtos.sort_values("Receita", ascending=True)
        fig_top = px.bar(
            top_produtos,
            x="Receita",
            y="Produto",
            orientation="h",
            title="Top 3 Produtos com Maior Receita",
            color_discrete_sequence=["#bb73e7"]
        )
        fig_top.update_layout(xaxis_title="Receita (R$)", yaxis_title="Produto")
        st.plotly_chart(fig_top, use_container_width=True)

    # Tabela completa
    st.markdown("---")
    with st.expander("Exibir Tabela completa de Vendas"):
        st.dataframe(df_filtrado, use_container_width=True)
