import streamlit as st
import requests
from cliente_filtrado import mostra_filtrado


def mostra_tela_user():
    BASE_URL = 'http://127.0.0.1:5000/'

    col1, col2 = st.columns(2)
    # Divide a tela em duas colunas


    pedidos = requests.get(f'{BASE_URL}pedidos').json()["pedidos"]

    with col1:
        st.markdown('<div style="background-color: red; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)

        st.subheader('Em Preparo')
        for pedido in pedidos:
            if pedido['status'] == 'Em preparo':
                st.markdown(f"<p style='color: red;'>PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div style="background-color: green; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)

        st.subheader('Prontos')
        for pedido in pedidos:
            if pedido['status'] == 'Pronto':
                st.markdown(f"<p style='color: green;'>PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)

    