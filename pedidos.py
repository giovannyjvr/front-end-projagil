import streamlit as st 
import requests
from pedido_filtrado import exibir_pedido_filtrado

id_pedidos = {}

def exibir_pedidos(id_pedidos):
    BASE_URL = 'https://restaurante-robo-2d22d9a49cb9.herokuapp.com/'    

    pedidos = requests.get(f'{BASE_URL}pedidos').json()["pedidos"]

    tab1, tab2, tab3 = st.tabs(["Pedidos", "Pronto", "Histórico"])

    with tab1:
        for pedido in pedidos:
            if pedido['status'] == 'Em preparo':
                st.markdown(f"<p style='front-size: 28px;font-weight: bold;'>PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
                # st.markdown('- ' + pedido['nome'][i])
                id_pedidos[f"{pedido['id']}"] = pedido['_id']

                for i in range(len(pedido['nome'])):
                    st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
                st.markdown('- ' + f"<p style='color: red;'> {pedido['status']}",unsafe_allow_html=True)
                if st.button('**Pronto**', key=pedido['_id']):
                    atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido['_id'], 'status': 'Pronto'})
                    st.rerun()
                st.markdown('<div style="background-color: red; height: 2px; width: 100%;"></div>', unsafe_allow_html=True)


    with tab2:
        for pedido in pedidos:
            if pedido['status'] == 'Pronto':
                st.markdown(f"**PEDIDO {pedido['id']}**</p>", unsafe_allow_html=True)
                id_pedidos[f'{pedido["id"]}'] = pedido['_id']

                for i in range(len(pedido['nome'])):
                    st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
                st.markdown('- ' + f"<p style='color: green;'> {pedido['status']}",unsafe_allow_html=True)
                if st.button('**Retirado**', key=pedido['_id']):
                    atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido['_id'], 'status': 'Retirado'})
                    st.rerun()
                st.markdown('<div style="background-color: green; height: 2px; width: 100%;"></div>', unsafe_allow_html=True)


    with tab3:
        for pedido in pedidos:
            if pedido['status'] == 'Retirado':
                st.markdown(f"**PEDIDO {pedido['id']}**</p>", unsafe_allow_html=True)
                id_pedidos[f'{pedido["id"]}'] = pedido['_id']

                for i in range(len(pedido['nome'])):
                    st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
                st.markdown('- ' + f"<p style='color: orange;'> {pedido['status']}",unsafe_allow_html=True)
                if st.button('**Deletar**', key=pedido['_id']):
                    deletar_pedido = requests.delete(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido['_id']})
                    st.rerun()
                st.markdown('<div style="background-color: orange; height: 2px; width: 100%;"></div>', unsafe_allow_html=True)
