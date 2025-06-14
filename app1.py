# Renomeando
import streamlit as st

st.title("STAR WARS FAN'S OPINION")
st.subheader("A long time ago in a galaxy far, far away, the Star Wars's fans were asked:")

# Inicializando as chaves no session_state
for key in [
    "name", "age", "favorite_movie", "favorite_character", "favorite_quote",
    "favorite_planet", "favorite_species", "favorite_ship", "favorite_droid",
    "favorite_battle", "character_choice", "favorite_period"
]:
    if key not in st.session_state:
        st.session_state[key] = ""

# Inputs do formulário
st.session_state["age"] = st.number_input("How old are you?", min_value=0, max_value=100, step=1, value=int(st.session_state["age"]) if st.session_state["age"] else 0)

# Condições
if st.session_state["age"] < 18:
    st.warning("You are not allowed to answer this survey.")
else:
    st.success("Hello, there! Answer the questions below:")

    if st.session_state["name"].strip().lower() == "victor":
        st.text("It's a pleasure to see you here, Batman!")

    if st.session_state["favorite_movie"].strip().lower() == "the revenge of the sith":
        st.text("You are a true fan!")
    elif st.session_state["favorite_movie"]:
        st.text("You have answered wrong!")

    # Perguntas adicionais
    st.session_state["name"] = st.text_input("What is your name?", value=st.session_state["name"])
    st.session_state["favorite_movie"] = st.text_input("What is your favorite movie?", value=st.session_state["favorite_movie"])
    st.session_state["favorite_character"] = st.text_input("Who is your favorite character?", value=st.session_state["favorite_character"])
    st.session_state["favorite_quote"] = st.text_input("What is your favorite quote?", value=st.session_state["favorite_quote"])
    st.session_state["favorite_planet"] = st.text_input("What is your favorite planet?", value=st.session_state["favorite_planet"])
    st.session_state["favorite_species"] = st.text_input("What is your favorite species?", value=st.session_state["favorite_species"])
    st.session_state["favorite_ship"] = st.text_input("What is your favorite ship?", value=st.session_state["favorite_ship"])
    st.session_state["favorite_droid"] = st.text_input("What is your favorite droid?", value=st.session_state["favorite_droid"])
    st.session_state["favorite_battle"] = st.text_input("What is your favorite battle?", value=st.session_state["favorite_battle"])
    st.session_state["character_choice"] = st.text_input("If you could be any Star Wars character, who would you choose?", value=st.session_state["character_choice"])
    st.session_state["favorite_period"] = st.text_input("What is your favorite period?", value=st.session_state["favorite_period"])

    # Cadastro
    if st.button("REGISTER"):
        with open("fanbase.csv", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{st.session_state['name']},{st.session_state['age']},{st.session_state['favorite_movie']},{st.session_state['favorite_character']},{st.session_state['favorite_quote']},{st.session_state['favorite_planet']},{st.session_state['favorite_species']},{st.session_state['favorite_ship']},{st.session_state['favorite_droid']},{st.session_state['favorite_battle']},{st.session_state['character_choice']},{st.session_state['favorite_period']}\n")
        st.success("You are in the fanbase!")