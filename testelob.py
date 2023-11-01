from textblob import TextBlob

with open('comentarios.txt', encoding='UTF-8') as f:
    texto = f.read()

analise_sentimento = TextBlob(texto)
sentimento = analise_sentimento.sentiment.polarity

print("Texto:", texto)
print("Sentimento (TextBlob):", sentimento)
print("Classificação (TextBlob):", "Positivo" if sentimento > 0 else "Negativo" if sentimento < 0 else "Neutro")
