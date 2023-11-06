import streamlit as st
from app import exibir_cardapio  # Importe a função da "Página 1"
from pedidos import exibir_pedidos
from pedido_filtrado import exibir_pedido_filtrado
from pedidos import id_pedidos



# Variável para controlar a página atual
cardapio = "http://localhost:5000/cardapio"
pedidos = "http://localhost:5000/pedidos"

pagina_atual = st.selectbox("Selecione uma página", ["Cardápio",
                                                      "Pedidos"]) 
#seleciona a página que quer ir. parte apenas do restaurante.

logo = "robochefe.png"
header_container = st.container()
header_container.image(logo, width= 40)

style = "font-size: 25px; margin-top: -30px;"
text = "<h1 style='{}'>Restaurante do Robô</h1>".format(style)
header_container.markdown(text, unsafe_allow_html=True)

if pagina_atual == "Cardápio":
    exibir_cardapio(cardapio)  # Chame a função da "Página 1"

if pagina_atual == "Pedidos":
    st.subheader("Buscar Pedido ")
    pedido_id = st.text_input("Insira a senha do Pedido que deseja buscar")
    buscar = st.button("Buscar")
    if buscar:
        voltar = st.button("Voltar")
        exibir_pedido_filtrado(id_pedidos, pedido_id    )
        if voltar:
            pagina_atual = "Pedidos"

    elif pagina_atual == "Pedidos":
        exibir_pedidos(id_pedidos)

elif pagina_atual == "filtrado":
    st.title("Página 3")
    st.write("Conteúdo da Página 3")