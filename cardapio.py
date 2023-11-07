import streamlit as st
import requests

url_cardapio = "https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio"  

def exibir_cardapio(url_cardapio):
    # Título do aplicativo
    st.markdown(f"<h1 style='font-size: 30px; display: flex; flex-direction: column; align-items: center; text-align: center;'> Cardápio",unsafe_allow_html=True)

    # URL do endpoint Flask que fornece o cardápio em formato JSON
    # Fazer uma solicitação GET para obter o cardápio
    response = requests.get(url_cardapio)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        cardapio = response.json()['cardapio']
        st.subheader("Adicionar Prato")
        nome_prato = st.text_input("Insira o nome do prato")
        preco_prato = st.text_input("Insira o preço do prato")
        descricao_prato = st.text_input("Insira a descrição do prato")
        if st.button("Adicionar"):
            adicionar_prato = requests.post('https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio', json={"name": nome_prato,"description":descricao_prato, "price": preco_prato})
            if response.status_code in (200,201):
                st.success("Prato adicionado com sucesso!")
            else:
                st.error("Erro ao adicionar o prato.")
            st.rerun()
    else:
        st.error("Erro ao obter o cardápio. Verifique se o servidor Flask está em execução.")

    # Criar um dicionário para rastrear os itens selecionados
    carrinho = {}

    # Exibir o cardápio e permitir que o usuário selecione itens

    # Função para adicionar ao carrinho
    def adicionar_ao_carrinho(nome_prato, quantidade):
        if nome_prato in carrinho:
            carrinho[nome_prato] += quantidade
        else:
            carrinho[nome_prato] = quantidade



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
        if st.button(f'Deletar Prato', key=id_prato):
            deletar_prato = requests.delete(f'https://restaurante-robo-2d22d9a49cb9.herokuapp.com/cardapio', json={"_id": id_prato})
            st.rerun()
        quantidade_sel = st.number_input(f"Selecione a quantidade de {nome_prato}", min_value=0, max_value=10, value=0)
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




