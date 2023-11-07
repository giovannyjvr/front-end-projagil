import streamlit as st
from cardapio import exibir_cardapio  # Importe a função da "Página 1"
from pedidos import exibir_pedidos
from pedido_filtrado import exibir_pedido_filtrado
from pedidos import id_pedidos
from add_prato import exibir_add
from delete_prato import deletar_prato


logo = "robochefe.png"
st.image(logo, width=100)  # Ajuste a largura conforme necessário
header_container = st.container()
style = "font-size: 40px; display: flex; align-items: center; justify-content: center; margin-top: -17%; margin-left: 30%;"
text = f"<h1 style='{style}'>Restaurante do Robô</h1>"
header_container.markdown(text, unsafe_allow_html=True)

# Variável para controlar a página atual
cardapio = "https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio"
pedidos = "https://restaurante-robo-2d22d9a49cb9.herokuapp.com/pedidos"

pagina_atual = st.selectbox("Selecione uma página", ["Cardápio",
                                                      "Pedidos",
                                                      "Adicionar Pedido", 
                                                      "Deletar Pedido"]) 
#seleciona a página que quer ir. parte apenas do restaurante.


if pagina_atual == "Cardápio":
    #titulo da página
    st.markdown(f"<h1 style='font-size: 30px; display: flex; flex-direction: column; align-items: center; text-align: center;'> Cardápio",unsafe_allow_html=True)
    exibir_cardapio(cardapio)  # Chame a função da "Página 1"

if pagina_atual == "Adicionar Pedido":
    st.markdown(f"<h1 style='font-size: 30px; display: flex; flex-direction: column; align-items: center; text-align: center;'> Adicionar Prato Novo",unsafe_allow_html=True)
    exibir_add(cardapio)

if pagina_atual == "Deletar Pedido":
    st.markdown(f"<h1 style='font-size: 30px; display: flex; flex-direction: column; align-items: center; text-align: center;'> Deletar Pedido",unsafe_allow_html=True)
    deletar_prato(cardapio)

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
