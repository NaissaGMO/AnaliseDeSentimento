import spacy
from textblob import TextBlob

nlp = spacy.load("pt_core_news_sm")

with open('comentarios.txt', encoding='UTF-8') as f:
    texto = f.read()

doc = nlp(texto)

analise_sentimento = TextBlob(texto)
sentimento = analise_sentimento.sentiment.polarity

print("Texto:", texto)
print("Sentimento (spaCy):", sentimento)
print("Classificação (spaCy):", "Positivo" if sentimento > 0 else "Negativo" if sentimento < 0 else "Neutro")
