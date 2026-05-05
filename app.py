import streamlit as st

# Configuração da página
st.set_page_config(page_title="Quiz Master Python", page_icon="📝")

st.title("🧠 Super Quiz de Conhecimentos Gerais")
st.write("Responda às 10 perguntas abaixo e veja seu desempenho!")

# Lista de perguntas, opções e respostas corretas
questoes = [
    {
        "pergunta": "1. Qual é a capital da França?",
        "opcoes": ["Londres", "Berlim", "Paris", "Madri"],
        "correta": "Paris"
    },
    {
        "pergunta": "2. Qual planeta é conhecido como o Planeta Vermelho?",
        "opcoes": ["Vênus", "Marte", "Júpiter", "Saturno"],
        "correta": "Marte"
    },
    {
        "pergunta": "3. Quem pintou a 'Mona Lisa'?",
        "opcoes": ["Van Gogh", "Picasso", "Da Vinci", "Dalí"],
        "correta": "Da Vinci"
    },
    {
        "pergunta": "4. Qual é o maior oceano do mundo?",
        "opcoes": ["Atlântico", "Índico", "Ártico", "Pacífico"],
        "correta": "Pacífico"
    },
    {
        "pergunta": "5. Quantos estados tem o Brasil?",
        "opcoes": ["24", "26", "27", "25"],
        "correta": "26"
    },
    {
        "pergunta": "6. Qual o metal cujo símbolo químico é Au?",
        "opcoes": ["Prata", "Cobre", "Ouro", "Alumínio"],
        "correta": "Ouro"
    },
    {
        "pergunta": "7. Em que ano terminou a Segunda Guerra Mundial?",
        "opcoes": ["1944", "1945", "1946", "1950"],
        "correta": "1945"
    },
    {
        "pergunta": "8. Qual é o maior animal terrestre?",
        "opcoes": ["Girafa", "Elefante Africano", "Rinoceronte", "Hipopótamo"],
        "correta": "Elefante Africano"
    },
    {
        "pergunta": "9. Qual linguagem de programação é famosa pelo seu logotipo de cobra?",
        "opcoes": ["Java", "C++", "Ruby", "Python"],
        "correta": "Python"
    },
    {
        "pergunta": "10. Qual a montanha mais alta do mundo?",
        "opcoes": ["K2", "Monte Everest", "Monte Kilimanjaro", "Pico da Neblina"],
        "correta": "Monte Everest"
    }
]

# Dicionário para armazenar as respostas do usuário
respostas_usuario = {}

# Criando a interface das perguntas
for i, q in enumerate(questoes):
    st.subheader(q["pergunta"])
    respostas_usuario[i] = st.radio(
        f"Escolha uma opção para a questão {i+1}:", 
        q["opcoes"], 
        key=f"q{i}",
        index=None # Começa sem nenhuma opção marcada
    )
    st.write("---")

# Botão de finalizar
if st.button("Finalizar Quiz"):
    pontuacao = 0
    erros = []

    for i, q in enumerate(questoes):
        if respostas_usuario[i] == q["correta"]:
            pontuacao += 1
        else:
            erros.append(f"Questão {i+1}")

    # Exibição do resultado
    st.balloons()
    st.success(f"### Você acertou {pontuacao} de 10 perguntas!")
    
    if pontuacao == 10:
        st.write("🏆 Perfeito! Você é um gênio!")
    elif pontuacao >= 7:
        st.write("👏 Muito bom! Quase lá.")
    else:
        st.write("📚 Bom esforço! Que tal revisar e tentar de novo?")