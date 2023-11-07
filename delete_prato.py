import streamlit as st
import requests


def deletar_prato(url_cardapio):

    url_cardapio = "https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio"  
    # URL do endpoint Flask que fornece o cardápio em formato JSON
    # Fazer uma solicitação GET para obter o cardápio
    response = requests.get(url_cardapio)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        cardapio = response.json()['cardapio']
    else:
        st.error("Erro ao obter o cardápio. Verifique se o servidor Flask está em execução.")

    
    for prato_info in cardapio:
        nome_prato = prato_info["name"]
        id_prato = prato_info["_id"]
        descrição = prato_info["description"]

        st.markdown(f"**<p style='font-size: 20px;'>{nome_prato}</p>**",unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: 12px;'>{descrição}",unsafe_allow_html=True)
        if st.button(f'Deletar Prato', key=id_prato):
            deletar_prato = requests.delete(f'https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio', json={"_id": id_prato})
            st.rerun()
        st.markdown('<div style="background-color: Blue; height: 3px; width: 100%;"></div>', unsafe_allow_html=True)
        




