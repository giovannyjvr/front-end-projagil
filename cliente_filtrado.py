import streamlit as st
import requests



def mostra_filtrado(numero_pedido):
    BASE_URL = 'http://127.0.0.1:5000/'
    pedidos = requests.get(f'{BASE_URL}pedidos').json()["pedidos"]
    numero_pedido = numero_pedido.strip()  # Remova espaços extras
    if numero_pedido.isdigit():
        numero_pedido = int(numero_pedido)
        # Filtrar a lista de pedidos com base no número do pedido
        pedidos_filtrados = [pedido for pedido in pedidos if pedido['id'] == numero_pedido]
        if pedidos_filtrados:
            for pedido in pedidos_filtrados:
                st.markdown(f"<p style='font-size: 48px; display: flex; flex-direction: column; align-items: center; text-align: center;'> {pedido['id']}</p>",unsafe_allow_html=True)

                if pedido["status"] == 'Em preparo':
                    st.markdown('<div style="background-color: red; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size: 38px; color: red; display: flex; flex-direction: column; align-items: center; text-align: center;'> {pedido['status']}",unsafe_allow_html=True)
                    st.markdown('<div style="background-color: red; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)
                
                elif pedido["status"] == 'Pronto':
                    st.markdown('<div style="background-color: green; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size: 38px; color: green; display: flex; flex-direction: column; align-items: center; text-align: center;'> {pedido['status']}",unsafe_allow_html=True)
                    st.markdown('<div style="background-color: green; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)

                elif pedido["status"] == 'Retirado':
                    st.markdown('<div style="background-color: yellow; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size: 38px; color: yellow; display: flex; flex-direction: column; align-items: center; text-align: center;'> {pedido['status']}",unsafe_allow_html=True)
                    st.markdown('<div style="background-color: yellow; height: 5px; width: 100%;"></div>', unsafe_allow_html=True)                    

        else:
            st.write("Nenhum pedido encontrado com o número especificado.")
    else:
        st.write("Por favor, insira um número de pedido válido.")
    