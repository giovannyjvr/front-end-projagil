import streamlit as st
import requests

url_cardapio = "https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio"  

def exibir_cardapio(url_cardapio):

    # URL do endpoint Flask que fornece o cardápio em formato JSON
    # Fazer uma solicitação GET para obter o cardápio
    response = requests.get(url_cardapio)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        cardapio = response.json()['cardapio']
        
    else:
        st.error("Erro ao obter o cardápio. Verifique se o servidor Flask está em execução.")

    # Criar um dicionário para rastrear os itens selecionados
    carrinho = {}

    # Função para adicionar ao carrinho
    def adicionar_ao_carrinho(nome_prato, quantidade):
        if nome_prato in carrinho:
            carrinho[nome_prato] += quantidade
        else:
            carrinho[nome_prato] = quantidade

    # Título do carrinho na aba lateral.
    st.sidebar.markdown(f"<h1 style='font-size: 30px;'>Carrinho</h1>", unsafe_allow_html=True)
    # Função para exibir o carrinho
    def exibir_carrinho():
        
        if not carrinho:
            st.sidebar.write("Seu carrinho está vazio.")
        else:
            for nome, quantidade in carrinho.items():
                st.sidebar.markdown(f"**<p style='font-size: 20px;'>{nome}</p>**",unsafe_allow_html=True)
                st.sidebar.markdown(f"<p style='font-size: 16px;'>{quantidade}</p>",unsafe_allow_html=True)

    for prato_info in cardapio:
        nome_prato = prato_info["name"]
        id_prato = prato_info["_id"]
        st.markdown(f"**<p style='font-size: 20px;'>{nome_prato}</p>**",unsafe_allow_html=True)
        quantidade_sel = st.number_input(f"Selecione a quantidade de {nome_prato}", min_value=0, max_value=10, value=0)
        st.markdown('<div style="background-color: Blue; height: 3px; width: 100%;"></div>', unsafe_allow_html=True)
        if quantidade_sel > 0:
            adicionar_ao_carrinho(nome_prato, quantidade_sel)


    # Botão para adicionar ao carrinho (enviar pedido para o servidor Flask)
    if st.sidebar.button("Adicionar Pedido"):
        nomes = []
        quantidades = []
        for nome, dados in carrinho.items():
            quantidade = dados
            nomes.append(nome)
            quantidades.append(quantidade)
        inserir_prato = requests.post('https://restaurante-robo-2d22d9a49cb9.herokuapp.com/pedidos', json={"nome": nomes, "quantidade": quantidades, "status": "Em preparo"})
        st.write("Pedido adicionado com sucesso")
        if response.status_code == 200:
            st.success("Pedido adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o pedido. Verifique o servidor Flask.")
        carrinho.clear()

    # Exibir o carrinho na barra lateral
    exibir_carrinho()




