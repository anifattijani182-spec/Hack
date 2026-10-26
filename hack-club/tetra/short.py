import streamlit as st
import random

# 1. Daten und Zustand im Browser-Speicher initialisieren (Session State)
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.subject = None
    st.session_state.topic = None
    st.session_state.score = 0
    st.session_state.quiz_pairs = []
    st.session_state.current_index = 0
    st.session_state.random_index = -1
    st.session_state.input_method = "Klicken (Duolingo Style)"
    
    st.session_state.wordlist = ["yes", "YES"]
    
    # =========================================================================
    # 📍 PLATZ FÜR WEITERE FRAGEN / THEMEN
    # =========================================================================
    
    # --- MATHE: Thema 0 (Graphen) ---
    st.session_state.topicgraphposition = [
        "a graph has the f(X)=x²+2", 
        "a graph has the f(X)=2x²", 
        "a graph has the f(X)=(x-2)³"
    ]
    # Hier kannst du weitere Listen für Thema 1, Thema 2 etc. erstellen:
    # st.session_state.mathe_thema_bruchrechnen = ["...", "..."]
    # st.session_state.mathe_thema_geometrie = ["...", "..."]


    # --- CHEMIE: Thema 0 (Alkane) ---
    st.session_state.chemvoc = [
        "Methan", "Ethan", "Propan", "Butan", "Pentan", 
        "Hexan", "Heptan", "Octan", "Nonan", "Decan", 
        "Undecan", "Octadecan"
        # ➕ Füge hier einfach weitere Alkan-Namen in Anführungszeichen hinzu!
    ]
    st.session_state.chemvoc2 = [
        "CH4", "C2H6", "C3H8", "C4H10", "C5H12", 
        "C6H14", "C7H16", "C8H18", "C9H20", "C10H22", 
        "C11H24", "C18H38"
        # ➕ Füge hier die passenden chemischen Formeln hinzu!
    ]
    # Hier Platz für ein weiteres Chemie-Thema (z.B. Säuren):
    # st.session_state.chemie_saeuren_namen = ["Salzsäure", "Schwefelsäure"]
    # st.session_state.chemie_saeuren_formeln = ["HCl", "H2SO4"]


    # --- PHYSIK: Daten-Platzhalter ---
    # Hier ist Platz für deine zukünftigen Physik-Vokabeln oder Formeln:
    # st.session_state.physik_fragen = ["Formel für Kraft", "Einheit der Spannung"]
    # st.session_state.physik_antworten = ["F=m*a", "Volt"]

# =========================================================================
# APP DESIGN & HEADER
# =========================================================================
st.set_page_config(page_title="Schullern App", page_icon="🦉", layout="centered")
st.title("🦉 Schullern App")
st.subheader("Die App, mit der du dich perfekt für Tests und Klassenarbeiten vorbereiten kannst!")
st.markdown("---")

# ZURÜCK-BUTTON (Um das Fach im Hauptmenü zu wechseln)
if st.session_state.subject is not None:
    if st.sidebar.button("🔙 Hauptmenü / Fach wechseln"):
        st.session_state.subject = None
        st.session_state.topic = None
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.rerun()

# ==========================================
# HAUPTMENÜ: Fach auswählen (Subject)
# ==========================================
if st.session_state.subject is None:
    st.subheader("Welches Fach möchtest du heute üben?")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📈 Mathe", use_container_width=True):
            st.session_state.subject = 0
            st.rerun()
    with col2:
        if st.button("🧪 Chemie", use_container_width=True):
            st.session_state.subject = 1
            st.rerun()
    with col3:
        if st.button("⚡ Physik", use_container_width=True):
            st.session_state.subject = 2
            st.rerun()

# ==========================================
# FACH 0: MATHE
# ==========================================
elif st.session_state.subject == 0:
    if st.session_state.topic is None:
        st.subheader("Wähle dein Mathe-Thema für die Arbeit:")
        
        if st.button("📍 Graphs Positioning", use_container_width=True):
            st.session_state.topic = 0
            st.session_state.random_index = random.randint(0, len(st.session_state.topicgraphposition) - 1)
            st.rerun()
            
        # ➕ HIER PLATZ FÜR WEITERE MATHE-THEMEN BUTTONS:
        # if st.button("🧮 Thema 2: Bruchrechnen", use_container_width=True):
        #     st.session_state.topic = 1
        #     st.rerun()
            
    else:
        st.info("📈 Fach: Mathe | Thema: Graphs Positioning")
        frage = st.session_state.topicgraphposition[st.session_state.random_index]
        st.write(f"### Frage: **{frage}**")
        st.write("*Where is it positioned now? Is it 2 to the y-Achse (press 0), -2 to the y-Achse (press 1), 1,2 to the x-Achse (press 2)...*")
        
        st.session_state.input_method = st.radio("Antwort-Modus:", ["Klicken (Duolingo Style)", "Tippen"], horizontal=True)
        antwort = None
        
        if st.session_state.input_method == "Tippen":
            user_input = st.text_input("Deine Antwort (Zahl eingeben):", key="math_text")
            if st.button("Antwort prüfen"):
                antwort = user_input
        else:
            st.write("Wähle die richtige Zahl:")
            m_cols = st.columns(5)
            for num in range(5):
                with m_cols[num]:
                    if st.button(f" {num} ", key=f"math_btn_{num}", use_container_width=True):
                        antwort = str(num)
                        
        if antwort is not None:
            if st.session_state.random_index == 0 and antwort == "0":
                st.success("🎉 Richtig!")
            elif st.session_state.random_index == 1 and antwort == "2":
                st.success("🎉 Richtig!")
            elif st.session_state.random_index == 2 and antwort == "1":
                st.success("🎉 Richtig!")
            else:
                st.error("❌ Falsch! Versuche es noch einmal.")
                
            if st.button("Nächste Aufgabe ➡️"):
                st.session_state.random_index = random.randint(0, len(st.session_state.topicgraphposition) - 1)
                st.rerun()

# ==========================================
# FACH 1: CHEMIE
# ==========================================
elif st.session_state.subject == 1:
    if st.session_state.topic is None:
        st.subheader("Wähle dein Chemie-Thema für den Test:")
        
        if st.button("🧪 Thema 1: Alkane (Vokabeln)", use_container_width=True):
            st.session_state.topic = 0
            pairs = list(zip(st.session_state.chemvoc, st.session_state.chemvoc2))
            random.shuffle(pairs)
            st.session_state.quiz_pairs = pairs
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.rerun()
            
        # ➕ HIER PLATZ FÜR WEITERE CHEMIE-THEMEN BUTTONS:
        # if st.button("🧪 Thema 2: Säuren & Basen", use_container_width=True):
        #     st.session_state.topic = 1
        #     st.rerun()
            
    else:
        if st.session_state.current_index < len(st.session_state.quiz_pairs):
            st.info(f"🧪 Fach: Chemie | Score: {st.session_state.score} Punkte")
            st.progress(st.session_state.current_index / len(st.session_state.quiz_pairs))
            
            word, correct_ans = st.session_state.quiz_pairs[st.session_state.current_index]
            st.write(f"### Was ist die chemische Formel für: **{word}**?")
            
            st.session_state.input_method = st.radio("Antwort-Modus:", ["Klicken (Duolingo Style)", "Tippen"], horizontal=True)
            user_guess = None
            
            if st.session_state.input_method == "Tippen":
                user_input = st.text_input("Deine Antwort:", key=f"chem_text_{st.session_state.current_index}")
                if st.button("Antwort prüfen"):
                    user_guess = user_input
            else:
                falsche_optionen = [ans for ans in st.session_state.chemvoc2 if ans != correct_ans]
                optionen = random.sample(falsche_optionen, min(3, len(falsche_optionen))) + [correct_ans]
                random.shuffle(optionen)
                
                c_cols = st.columns(2)
                for idx, opt in enumerate(optionen):
                    with c_cols[idx % 2]:
                        if st.button(opt, key=f"chem_btn_{opt}_{idx}", use_container_width=True):
                            user_guess = opt
            
            if user_guess:
                if user_guess.strip().lower() == correct_ans.lower():
                    st.success("🎉 Richtig!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Falsch! Die richtige Antwort war: {correct_ans}")
                
                if st.button("Weiter ➡️"):
                    st.session_state.current_index += 1
                    st.rerun()
        else:
            st.balloons()
            st.success(f"🏁 Ausgezeichnet! Endstand: {st.session_state.score}/{len(st.session_state.quiz_pairs)} Punkte!")
            if st.button("Nochmal spielen"):
                st.session_state.topic = None
                st.rerun()

# ==========================================
# FACH 2: PHYSIK (KOMPLETT NEU VORBEREITET)
# ==========================================
elif st.session_state.subject == 2:
    st.subheader("⚡ Physik-Vorbereitung")
    st.write("Hier kannst du bald deine Physik-Themen auswählen!")
    
    # ➕ HIER PLATZ FÜR ZUKÜNFTIGE PHYSIK-BUTTONS UND LOGIK:
    st.info("Übungsaufgaben für Physik werden demnächst hinzugefügt.")
    
    if st.button("Zurück zum Hauptmenü"):
        st.session_state.subject = None
        st.rerun()
