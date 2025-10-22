import streamlit as st
import random

st.set_page_config(page_title="Jeu de Cartes 🎴", page_icon="🃏")

st.title("🎴 Jeu de Cartes : Joueur vs Ordinateur")

# --- Initialisation de session_state ---
if "score_joueur" not in st.session_state:
    st.session_state.score_joueur = 0
    st.session_state.score_ordi = 0
    st.session_state.derniere_carte_joueur = None
    st.session_state.derniere_carte_ordi = None
    st.session_state.resultat = ""

# --- Liste des cartes ---
valeurs_cartes = {
    2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
    8: "8", 9: "9", 10: "10", 11: "Valet", 12: "Dame", 13: "Roi", 14: "As"
}

# --- Bouton pour tirer une carte ---
if st.button("🎲 Tirer une carte"):
    carte_joueur = random.randint(2, 14)
    carte_ordi = random.randint(2, 14)
    
    st.session_state.derniere_carte_joueur = carte_joueur
    st.session_state.derniere_carte_ordi = carte_ordi

    if carte_joueur > carte_ordi:
        st.session_state.score_joueur += 1
        st.session_state.resultat = "✅ Tu gagnes ce tour !"
    elif carte_ordi > carte_joueur:
        st.session_state.score_ordi += 1
        st.session_state.resultat = "❌ L'ordinateur gagne ce tour..."
    else:
        st.session_state.resultat = "🤝 Égalité !"

# --- Affichage des cartes tirées ---
if st.session_state.derniere_carte_joueur:
    st.subheader("🃏 Résultat du tour :")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Ta carte** : {valeurs_cartes[st.session_state.derniere_carte_joueur]}")
    with col2:
        st.markdown(f"**Carte de l'ordinateur** : {valeurs_cartes[st.session_state.derniere_carte_ordi]}")
    st.markdown(f"### {st.session_state.resultat}")

# --- Score ---
st.markdown("---")
st.subheader("📊 Score")
st.markdown(f"- Joueur : **{st.session_state.score_joueur}**")
st.markdown(f"- Ordinateur : **{st.session_state.score_ordi}**")

# --- Bouton reset ---
if st.button("🔄 Réinitialiser le jeu"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
