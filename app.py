import random
import streamlit as st

# -----------------------------------------------------------------
# Configuration de la page
# -----------------------------------------------------------------
st.set_page_config(
    page_title="Chatbot Émotionnel",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------
# Style CSS
# -----------------------------------------------------------------
st.markdown("""
<style>
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 15px;
        margin: 12px 0;
        text-align: right;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .bot-message {
        background-color: white;
        color: #333;
        padding: 15px;
        border-radius: 15px;
        margin: 12px 0;
        border-left: 5px solid #4CAF50;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .chat-container {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
    }
    .main-title {
        text-align: center;
        color: #333;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .stButton button {
        width: 100% !important;
        padding: 12px !important;
        border-radius: 10px !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------
with st.sidebar:
    st.title("🤖 Chatbot Émotionnel")
    st.markdown("---")
    st.markdown("""
    ### 📖 À propos
    Ce chatbot de soutien émotionnel est conçu pour :
    - 💭 Vous écouter
    - 🤝 Vous soutenir
    - 💪 Vous aider à gérer vos émotions

    ### 💡 Commandes spéciales
    - Tapez **"au revoir"** pour terminer
    """)

    if st.button("🔄 Réinitialiser la conversation", use_container_width=True):
        st.session_state.historique = []
        st.rerun()

# -----------------------------------------------------------------
# Titre principal
# -----------------------------------------------------------------
st.markdown("<h1 class='main-title'>💬 Chatbot de Soutien Émotionnel</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#666; font-size:16px;'>"
    "Bienvenue ! Je suis ici pour vous écouter. N'hésitez pas à partager vos sentiments."
    "</p>",
    unsafe_allow_html=True
)
st.markdown("---")

# -----------------------------------------------------------------
# Mémoire de conversation
# -----------------------------------------------------------------
if "historique" not in st.session_state:
    st.session_state.historique = []

# -----------------------------------------------------------------
# Règles du chatbot
# -----------------------------------------------------------------
# IMPORTANT : chaque clé est un TUPLE de mots-clés (pas une chaîne avec "or" !)
# Un tuple s'écrit avec des parenthèses : ("mot1", "mot2", "mot3")
REPONSES = {
    ("bonjour", "salut", "hello", "asslema"): [
        "Bonjour ! Comment allez-vous aujourd'hui ?",
        "Salut ! Enchanté de vous rencontrer. Comment ça va ?",
        "Bonjour ! Je suis là pour vous écouter.",
        "Coucou ! Comment je peux vous aider aujourd'hui ?"
    ],
    ("triste", "déprimé", "mkarrez"): [
        "😢 Pourquoi vous sentez-vous triste ?",
        "Je comprends que vous traversez une période difficile. Pouvez-vous m'en dire plus ?",
        "La tristesse est légitime. Depuis quand ressentez-vous cela ?",
        "Je suis désolé que vous vous sentiez ainsi. Voulez-vous en parler ?"
    ],
    ("heureux", "joyeux", "content", "farhan"): [
        "😊 C'est une bonne nouvelle ! Qu'est-ce qui vous rend si content ?",
        "Je suis ravi de l'entendre ! Racontez-moi votre bonne nouvelle.",
        "🎉 C'est merveilleux ! Qu'est-ce qui vous fait sourire ?",
        "Votre bonheur me ravit ! Parlez-moi de cette joie."
    ],
    ("anxieux", "anxiété", "angoisse"): [
        "😰 L'anxiété est difficile à vivre. Qu'est-ce qui vous préoccupe ?",
        "Je sens que vous êtes inquiet(e). Pouvez-vous en identifier la source ?",
        "L'anxiété peut être accablante. Quand avez-vous commencé à vous sentir ainsi ?",
        "Respirez profondément. Qu'est-ce qui vous cause cette anxiété ?"
    ],
    ("peur", "effrayé", "effrayée"): [
        "😟 De quoi avez-vous peur exactement ?",
        "La peur est une émotion naturelle. À quand remonte cette peur ?",
        "Je vous comprends. Pouvez-vous me décrire ce qui vous fait peur ?",
        "Parlez-moi de cette peur. Ensemble, nous pouvons y réfléchir."
    ],
    ("frustration", "frustré", "frustrée"): [
        "😤 La frustration peut être intense. Qu'est-ce qui vous frustre ?",
        "Je comprends votre frustration. Pouvez-vous me dire ce qui s'est passé ?",
        "Parlez-moi de la situation."
    ],
    ("colère", "colere", "énervé", "énervée"): [
        "😠 Je sens votre colère. Pouvez-vous me dire ce qui s'est passé ?",
        "La colère est une émotion puissante. Qu'est-ce qui vous rend en colère ?",
        "Parlons de ce qui provoque cette colère."
    ],
    ("seul", "seule", "solitude"): [
        "🏜️ Se sentir seul(e) est difficile. Parlez-moi de ce sentiment.",
        "La solitude peut être pesante. Êtes-vous toujours en contact avec vos proches ?",
        "Vous n'êtes pas vraiment seul(e) ici — je suis là. Parlez-moi de vous."
    ],
    ("stress", "stressé", "stressée"): [
        "😓 Le stress peut être écrasant. Qu'est-ce qui vous stresse ?",
        "Je sens que vous êtes stressé(e). Parlez-moi de votre situation.",
        "Respirez. Qu'est-ce qui cause ce stress ?"
    ],
    ("confiance",): [
        "💪 C'est fantastique ! Parlez-moi de votre confiance.",
        "Je suis heureux de vous voir confiant(e) ! Qu'est-ce qui a changé ?",
        "La confiance en soi est précieuse. Sur quoi repose-t-elle ?"
    ],
}

REPONSES_GENERALES = [
    "Dites-m'en un peu plus...",
    "Continuez, je vous écoute attentivement.",
    "C'est intéressant. Et ensuite ?",
    "Je comprends. Pourriez-vous développer ?",
    "Merci de partager avec moi. Qu'en pensez-vous ?",
]

MOTS_AU_REVOIR = ("au revoir", "bye", "adieu")


def get_response(message: str) -> str:
    """Cherche un groupe de mots-clés correspondant au message et
    renvoie une réponse au hasard parmi celles associées."""
    message_lower = message.lower()

    if any(mot in message_lower for mot in MOTS_AU_REVOIR):
        return "👋 Au revoir ! Prenez soin de vous et n'hésitez pas à revenir."

    for mots_cles, reponses in REPONSES.items():
        if any(mot in message_lower for mot in mots_cles):
            return random.choice(reponses)

    return random.choice(REPONSES_GENERALES)


def ajouter_message(auteur: str, texte: str) -> None:
    """Ajoute un message à l'historique de conversation."""
    st.session_state.historique.append((auteur, texte))


# -----------------------------------------------------------------
# Zone de saisie (chat_input se vide automatiquement après envoi)
# -----------------------------------------------------------------
message_utilisateur = st.chat_input("Tapez votre message ici...")

if message_utilisateur:
    message_utilisateur = message_utilisateur.strip()
    reponse = get_response(message_utilisateur)
    ajouter_message("Vous", message_utilisateur)
    ajouter_message("Bot", reponse)

# -----------------------------------------------------------------
# Affichage de la conversation (ordre chronologique)
# -----------------------------------------------------------------
if st.session_state.historique:
    st.markdown("### 💬 Conversation")
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for auteur, texte in st.session_state.historique:
        if auteur == "Vous":
            st.markdown(
                f'<div class="user-message"><strong>👤 Vous :</strong><br>{texte}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="bot-message"><strong>🤖 Bot :</strong><br>{texte}</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("👋 Commencez une conversation en écrivant un message ci-dessus !")