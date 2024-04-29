import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Fonction pour analyser le sentiment
def analyze_sentiment(message):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(message)['compound']
    if sentiment_score > 0.05:
        return "Positif"
    elif sentiment_score < -0.05:
        return "Négatif"
    else:
        return "Neutre"

# Titre de l'application
st.title("Analyse de sentiments sur les réseaux sociaux")

# Zone de texte pour saisir le message
message_input = st.text_area("Saisissez votre message :", height=100)

# Bouton pour analyser le sentiment
if st.button("Analyser le sentiment"):
    if message_input:
        sentiment = analyze_sentiment(message_input)
        st.write("Sentiment du message :", sentiment)
    else:
        st.write("Veuillez saisir un message pour l'analyser.")
