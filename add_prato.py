import streamlit as st
import requests

url_cardapio = "https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio"  

def exibir_add(url_cardapio):


    url_cardapio = "https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio"  


    # URL do endpoint Flask que fornece o cardápio em formato JSON
    # Fazer uma solicitação GET para obter o cardápio
    response = requests.get(url_cardapio)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        nome_prato = st.text_input("Insira o nome do prato")
        preco_prato = st.text_input("Insira o preço do prato")
        descricao_prato = st.text_input("Insira a descrição do prato")
        if st.button("Adicionar"):
            requests.post('https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio', json={"name": nome_prato,"description":descricao_prato, "price": preco_prato})
            if response.status_code in (200,201):
                st.success("Prato adicionado com sucesso!")
            else:
                st.error("Erro ao adicionar o prato.")
            st.rerun()
    else:
        st.error("Erro ao obter o cardápio. Verifique se o servidor Flask está em execução.")
