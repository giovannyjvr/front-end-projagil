import streamlit as st
from cliente import mostra_tela_user  # Importe a função da "Página 1"
from cliente_filtrado import mostra_filtrado

# Variável para controlar a página atual

#parte para colocar o logo e ajustar o titulo.
logo = "robochefe.png"
st.image(logo, width=100)  # Ajuste a largura conforme necessário
header_container = st.container()
style = "font-size: 40px; display: flex; align-items: center; justify-content: center; margin-top: -17%; margin-left: 30%;"
text = f"<h1 style='{style}'>Restaurante do Robô</h1>"
header_container.markdown(text, unsafe_allow_html=True)
#fim da parte do logo.

pagina_atual = "cliente_completo"

st.markdown(f"<h1 style='font-size: 20px;'> Insira a SENHA do seu Pedido",unsafe_allow_html=True)
numero_pedido = st.text_input("")

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