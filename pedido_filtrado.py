import streamlit as st 
import requests



def exibir_pedido_filtrado(id_pedidos,id_filtrado):
    BASE_URL = 'http://127.0.0.1:5000/'

    pedidos = requests.get(f'{BASE_URL}pedidos').json()["pedidos"]

    id_filtrado = id_pedidos[id_filtrado]

    url_pedido = f'{BASE_URL}pedidos/{id_filtrado}'  # Endpoint para buscar um pedido por ID
    response = requests.get(url_pedido)

    if response.status_code == 200:
        st.empty()
        pedido = response.json()["pedido"]
        st.subheader("Pedido encontrado:")
        

        if pedido['status'] == 'Em preparo':
            st.markdown(f"<p style='color: red;'> PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
            for i in range(len(pedido['nome'])):
                st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
            st.markdown('- ' + f"<p style='color: red;'> {pedido['status']}",unsafe_allow_html=True)

            pronto = st.button('**Pronto**', key=id_filtrado)
            if pronto:
                atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": id_filtrado, 'status': 'Pronto'})
                atualizar_pedido

        elif pedido['status'] == 'Pronto': 
            st.markdown(f"<p style='color: green;'> PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
            for i in range(len(pedido['nome'])):
                st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
            st.markdown('- ' + f"<p style='color: green;'> {pedido['status']}",unsafe_allow_html=True)

            if st.button('**Retirado**', key=id_filtrado):
                atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": id_filtrado, 'status': 'Retirado'})
                atualizar_pedido

        elif pedido['status'] == 'Retirado':
            st.markdown(f"<p style='color: orange;'> PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
            for i in range(len(pedido['nome'])):
                st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
            st.markdown('- ' + f"<p style='color: orange;'> {pedido['status']}",unsafe_allow_html=True)

            if st.button('**Deletar**', key=id_filtrado):
                deletar_pedido = requests.delete(f'{BASE_URL}restaurante/pedidos', json={"_id": id_filtrado})
                deletar_pedido

        elif response.status_code == 404:
            st.write("Pedido não encontrado.")
        else:
            st.write("Erro ao buscar o pedido. Verifique o servidor Flask.")
    else:
        st.write("Pedido não encontrado na lista de pedidos filtrados.")