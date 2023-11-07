import streamlit as st
from cliente import mostra_tela_user  # Importe a função da "Página 1"
from cliente_filtrado import mostra_filtrado

# Variável para controlar a página atual

logo = "robochefe.png"
header_container = st.container()
header_container.image(logo, width= 40)

style = "font-size: 25px; margin-top: -30px;"
text = "<h1 style='{}'>Bem-vindo Ao Restaurante do Robô</h1>".format(style)
header_container.markdown(text, unsafe_allow_html=True)


pagina_atual = "cliente_completo"

numero_pedido = st.text_input("Insira o número do pedido:")

filtrar = st.button("Filtrar")

# Verifique se o botão de filtro foi pressionado
if filtrar:
    pagina_atual = "filtro"

if pagina_atual == "cliente_completo":
    mostra_tela_user()  # Chame a função da "Página 1"

    
elif pagina_atual == "filtro":
    mostra_filtrado(numero_pedido)  # Chame a função da "Página 1"
    voltar = st.button("voltar")

    # Verifique se o botão de filtro foi pressionado
    if voltar:
        pagina_atual = "cliente_completo"