import streamlit as st

# 1. Configuração Inicial da Página
st.set_page_config(page_title="Desafio dos 100%", page_icon="🎯")

# Estilização básica para o título
st.title("🎯 O Desafio da Perfeição")
st.markdown("""
    Responda corretamente às **10 perguntas**. 
    O botão com o link secreto só aparecerá se você não cometer **nenhum erro**.
""")
st.divider()

# 2. Banco de Dados de Perguntas
questoes = [
    {"p": "1. Segundo a bíblia, quem foi o primeiro assassino do mundo?", "o": ["José", "Moisés", "Caim", "Adão"], "c": "Caim"},
    {"p": "2. "Salvar pessoas, caçar coisas, o negócio da família", Em que seriado essa frase foi dita'?", "o": ["Chiquititas", "Chapolin Colorado", "Naruto", "Supernatural"], "c": "Supernatural"},
    {"p": "3. Qual é a fórmula química da água?", "o": ["CO2", "H2O", "NaCl", "O2"], "c": "H2O"},
    {"p": "4. São células MAIS DIFERENCIADAS e com MENOR capacidade de reprodução:", "o": ["osteoclastos", "encéfalo", "neurônios", "hepatócitos"], "c": "neurônios"},
    {"p": "5. Na constução de um cinema, os arquitetos avaliaram a relação entre a quantidade de fileiras e a quantidade de cadeiras em cada fileira. O projeto inicial prevê uma sala para 304 pessoas. No caso de utilizarem 19 fileiras, o número de cadeiras por fileira será", "o": ["16", "8", "17", "13"], "c": "16"},
    {"p": "6. Em que ano ocorreu o evento chamado Guerra de Trincheiras?", "o": ["1915-1918", "1912-1915", "1919-1927", "1909-1911"], "c": "1915-1918"},
    {"p": "7. Um carro viaja por uma estrada reta e deserta e o motorista mantém uma velocidade constante de 80 km/h. Após se passarem 2 horas desde o início da viagem o motorista percorreu", "o": ["200 km", "160 km", "80 km", "40 km"], "c": "160 km"},
    {"p": "8. Qual é o animal mais veloz do mundo?", "o": ["Leão", "Guepardo", "Antílope", "Zebra"], "c": "Guepardo"},
    {"p": "9. Se um minuto tem 60 segundos, quantos segundos tem uma hora?", "o": ["2360", "360", "1800", "3600"], "c": "3600"},
    {"p": "10. Qual gás os humanos exalam na respiração?", "o": ["Oxigênio", "Nitrogênio", "Gás Carbônico", "Hélio"], "c": "Gás Carbônico"}
]

# 3. Criação do Formulário de Perguntas
respostas_usuario = {}

for i, item in enumerate(questoes):
    st.subheader(item["p"])
    respostas_usuario[i] = st.radio(
        "Selecione sua resposta:",
        options=item["o"],
        key=f"pergunta_{i}",
        index=None  # Mantém as opções desmarcadas inicialmente
    )
    st.write("") # Espaçamento

# 4. Lógica de Verificação
st.divider()
if st.button("Enviar Respostas", use_container_width=True):
    # Verifica se o usuário esqueceu alguma pergunta
    if None in respostas_usuario.values():
        st.warning("⚠️ Por favor, responda todas as questões antes de enviar.")
    else:
        # Calcula a pontuação
        acertos = 0
        for i, item in enumerate(questoes):
            if respostas_usuario[i] == item["c"]:
                acertos += 1
        
        # Exibe o feedback
        if acertos == 10:
            st.balloons()
            st.success("✨ PARABÉNS! Você gabaritou o quiz!")
            
            # BLOCO SECRETO: Só aparece com 10 acertos
            st.markdown("---")
            st.info("### 🎁 Acesso Liberado!")
            st.write("Como prometido, aqui está o seu link especial:")
            st.link_button("👉 ACESSAR CONTEÚDO EXCLUSIVO", "https://www.google.com") 
            # Substitua o link acima pela URL desejada
            st.markdown("---")
        else:
            st.error(f"Você acertou {acertos} de 10.")
            st.write("Infelizmente o link permanece bloqueado. Revise suas respostas e tente novamente!")
