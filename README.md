# 💬 Chatbot Émotionnel

> 🚧 **v0.1.0** — Version initiale basée sur la détection de mots-clés.
> Ce projet est en développement actif, voir la roadmap ci-dessous pour les prochaines étapes.

Un chatbot simple de soutien émotionnel, construit avec **Python** et **Streamlit**.
Il détecte des mots-clés dans les messages (tristesse, joie, stress, peur, etc.)
et répond avec des questions ouvertes, dans l'esprit d'un premier échange
d'écoute active.

⚠️ **Projet éducatif** : ce chatbot repose sur une simple détection de mots-clés
(pas de modèle d'IA / NLP). Il ne remplace en aucun cas un professionnel de
santé mentale.

## 🎯 Fonctionnalités

- Interface de chat interactive (Streamlit)
- Détection de mots-clés liés aux émotions (tristesse, joie, colère, peur, stress, solitude...)
- Réponses variées choisies aléatoirement pour éviter la répétition
- Historique de conversation conservé pendant la session
- Interface personnalisée (CSS) avec bulles de message façon chat

## 🖼️ Aperçu

*(Ajoute ici une capture d'écran de l'app une fois lancée : `![aperçu](screenshot.png)`)*

## 🚀 Installation

```bash
# Cloner le dépôt
git clone https://github.com/<ton-utilisateur>/chatbot-emotionnel.git
cd chatbot-emotionnel

# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate      # sur Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

## ▶️ Utilisation

```bash
streamlit run app.py
```

L'application s'ouvre automatiquement dans ton navigateur à l'adresse
`http://localhost:8501`.

## 🧠 Comment ça fonctionne

Le chatbot utilise un dictionnaire de règles : chaque groupe de mots-clés
(ex. `"triste"`, `"déprimé"`) est associé à une liste de réponses possibles.
À chaque message, le bot vérifie si un mot-clé connu apparaît dans le texte,
et répond en conséquence (sinon, il renvoie une réponse générique invitant
à en dire plus).

```python
REPONSES = {
    ("triste", "déprimé"): [
        "Pourquoi vous sentez-vous triste ?",
        "Depuis quand ressentez-vous cela ?",
    ],
    ...
}
```

## 🗺️ Roadmap

- [x] **v0.1.0** — Chatbot par mots-clés + interface Streamlit + historique de session
- [ ] **v0.2.0** — Expressions régulières (`re`) pour mieux gérer les variantes de mots et les fautes
- [ ] **v0.3.0** — Connexion à une vraie API d'IA pour des réponses plus naturelles
- [ ] **v0.4.0** — Déploiement public 
- [ ] **v1.0.0** — Tests unitaires + sauvegarde de l'historique)

## 📄 Licence

Ce projet est sous licence MIT — voir le fichier [LICENSE](LICENSE).
