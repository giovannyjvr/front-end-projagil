import streamlit as st 
import requests
from pedido_filtrado import exibir_pedido_filtrado

id_pedidos = {}

def exibir_pedidos(id_pedidos):
    BASE_URL = 'http://127.0.0.1:5000/'    


    st.header('Pedidos:')
    pedidos = requests.get(f'{BASE_URL}pedidos').json()["pedidos"]


    


    tab1, tab2, tab3 = st.tabs(["Pedidos", "Pronto", "Histórico"])

    with tab1:
        for pedido in pedidos:
            if pedido['status'] == 'Em preparo':
                st.markdown(f"<p style='color: red;'> PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
                # st.markdown('- ' + pedido['nome'][i])
                id_pedidos[f"{pedido['id']}"] = pedido['_id']

                for i in range(len(pedido['nome'])):
                    st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
                    # st.markdown('- ' + 'Quantidade: ' + str(pedido['quantidade'][i]))
                st.markdown('- ' + pedido['status'])
                if st.button('**Pronto**', key=pedido['_id']):
                    atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido['_id'], 'status': 'Pronto'})
                    st.rerun()


    with tab2:
        for pedido in pedidos:
            if pedido['status'] == 'Pronto':
                st.markdown(f"<p style='color: green;'> PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
                id_pedidos[f'{pedido["id"]}'] = pedido['_id']

                for i in range(len(pedido['nome'])):
                    st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
                    # st.markdown('- ' + 'Quantidade: ' + str(pedido['quantidade'][i]))
                st.markdown('- ' + pedido['status'])
                if st.button('**Retirado**', key=pedido['_id']):
                    atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido['_id'], 'status': 'Retirado'})
                    st.rerun()


    with tab3:
        for pedido in pedidos:
            if pedido['status'] == 'Retirado':
                st.markdown(f"<p style='color: green;'> PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
                id_pedidos[f'{pedido["id"]}'] = pedido['_id']

                for i in range(len(pedido['nome'])):
                    st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
                st.markdown('- ' + f"<p style='color: orange;'> {pedido['status']}",unsafe_allow_html=True)
                if st.button('**Deletar**', key=pedido['_id']):
                    deletar_pedido = requests.delete(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido['_id']})
                    st.rerun()
    
    # # Botão para buscar o pedido pelo ID
    # if st.sidebar.button("Buscar"):
    #     if pedido_id:
    #         id_valor = id_pedidos.get(f"{pedido_id}")
    #         if id_valor:
    #             # Limpar a tela

    #             url_pedido = f'{BASE_URL}pedidos/{id_valor}'  # Endpoint para buscar um pedido por ID
    #             response = requests.get(url_pedido)
    #             if response.status_code == 200:
    #                 st.empty()

    #                 pedido = response.json()["pedido"]
    #                 st.subheader("Pedido encontrado:")
    #                 st.markdown(f"<p style='color: green;'> PEDIDO {pedido['id']}</p>", unsafe_allow_html=True)
    #                 st.markdown('- ' +f"**{pedido['nome'][i]}**" + f' | ' + str(pedido['quantidade'][i]))
    #                 st.markdown('- ' + f"<p style='color: orange;'> {pedido['status']}",unsafe_allow_html=True)
                    

    #                 if pedido['status'] == 'Em preparo':
    #                     pronto = st.button('**Pronto**', key=pedido_id)
    #                     if pronto:
    #                         atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido_id, 'status': 'Pronto'})
    #                         atualizar_pedido

    #                 elif pedido['status'] == 'Pronto': 
    #                     if st.button('**Retirado**', key=pedido_id):
    #                         atualizar_pedido = requests.put(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido_id, 'status': 'Retirado'})
    #                         atualizar_pedido

    #                 elif pedido['status'] == 'Retirado':
    #                     if st.button('**Deletar**', key=pedido_id):
    #                         deletar_pedido = requests.delete(f'{BASE_URL}restaurante/pedidos', json={"_id": pedido_id})
    #                         deletar_pedido


    #             elif response.status_code == 404:
    #                 st.write("Pedido não encontrado.")
    #             else:
    #                 st.write("Erro ao buscar o pedido. Verifique o servidor Flask.")
    #         else:
    #             st.write("Pedido não encontrado na lista de pedidos filtrados.")

    
    # if st.sidebar.button("Buscar"):
    #     if pedido_id:
    #         id_valor = id_pedidos[f"{pedido_id}"]
    #         print (id_valor)
    #         print("otarioooo")
    #         url_pedido = f'{BASE_URL}pedidos/{(id_valor)}'  # Endpoint para buscar um pedido por ID
    #         response = requests.get(url_pedido)
    #         if response.status_code == 200:
    #             pedido = response.json()["pedido"]
    #             st.write("Pedido encontrado:")
    #             st.write(pedido)
    #             # exibir_pedido_filtrado(id_valor)
                
    #         elif response.status_code == 404:
    #             st.write("Pedido não encontrado.")
    #         else:
    #             st.write("Erro ao buscar o pedido. Verifique o servidor Flask.")
        