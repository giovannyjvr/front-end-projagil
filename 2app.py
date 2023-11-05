import streamlit as st
import requests

st.title("Pratos Restaurante 6° P2")

# Faz uma solicitação à API Flask para obter dados
response = requests.get('http://localhost:5000/cardapio')
if response.status_code == 200:
    data = response.json()
    st.write("Dados da API:", data)
else:
    st.write("Erro ao obter dados da API")



# Dados fictícios em formato de lista de dicionários
data = [
    {"Nome": "Feijoada", "preço": 25.00, "Cidade": "Arroz, feijoada, couve refogada, bisteca, farofa e vinagrete"},
    {"Nome": "Filé de Frango", "preço": 30.99, "Cidade": "Los Angeles"},
    {"Nome": "Strogonoff de carne", "preço": 35.00, "Cidade": "Chicago"},
    {"Nome": "Salada", "preço": 40.00, "Cidade": "Houston"}
]

selection_state = {item["Nome"]: False for item in data}


def add_checkbox(item):
    checkbox_id = f"checkbox-{item['Nome']}"
    selection_state[item['Nome']] = st.checkbox(item['Nome'], key=checkbox_id, value=selection_state[item['Nome']])
    

# Exiba a tabela com botões
st.title("Cardápio")
st.write('<style>div.row-widget.stRadio > div{flex-direction: column;}</style>', unsafe_allow_html=True)


for item in data:
    st.markdown(f"<h2>{item['Nome']}</h2>", unsafe_allow_html=True)  # Nome como título
    st.markdown(f"<p>Descrição: {item['Cidade']} - Preço: R${item['preço']}</p>", unsafe_allow_html=True)  # Cidade como descrição e Idade como valor
    add_checkbox(item)
