import nltk
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords
import random

# Baixar recursos do NLTK
nltk.download('stopwords')

# Carregar o arquivo com as frases
with open('comentarios.txt', encoding='utf-8') as file:
    content = file.readlines()

# Remover quebras de linha
content = [x.strip() for x in content]

# Lista de stopwords em português
stop_words = set(stopwords.words('portuguese'))

# Função para realizar o pré-processamento das frases
def preprocess(sentence):
    stemmer = RSLPStemmer()
    words = nltk.word_tokenize(sentence.lower())
    words = [stemmer.stem(word) for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    return words

# Construir a base de dados com emoções fictícias
base = [
    ('Essa capinha de celular é muito boa', 'satisfacao'),
    ('Gostei muito desta capinha de celular', 'satisfacao'),
    ('Capinha maravilhosa', 'satisfacao'),
    ('Que capinha bonita', 'satisfacao'),
    ('Abaixo do esperado', 'raiva'),
    ('Não gostei', 'raiva'),
    ('Desbotou na primeira semana', 'raiva'),
    ('Sempre compro aqui!', 'satisfacao'),
    ('Material de baixa resistência', 'raiva'),
    ('Custo benefício excelente', 'satisfacao'),
    ('A foto é diferente do produto', 'raiva'),
    ('Adorei as coleções disponiveis', 'satisfacao'),
    ('otimas promoções', 'satisfacao')
]

# Pré-processar as frases da base
base_preprocessada = [(preprocess(sentence), emotion) for sentence, emotion in base]

# Embaralhar a base
random.shuffle(base_preprocessada)

# Função para extrair características
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in palavras_unicas:
        features[word] = (word in document_words)
    return features

# Criar lista de todas as palavras
todas_palavras = [word for words, emotion in base_preprocessada for word in words]

# Frequência das palavras
frequencia = nltk.FreqDist(todas_palavras)

# Palavras únicas
palavras_unicas = list(frequencia.keys())

# Base completa com características
base_completa = [(extract_features(words), emotion) for words, emotion in base_preprocessada]

# Treinar o classificador
classificador = nltk.NaiveBayesClassifier.train(base_completa)

# Testar o classificador nas frases do arquivo
for sentence in content:
    words = preprocess(sentence)
    features = extract_features(words)
    emocao = classificador.classify(features)
    print(f'Frase: {sentence} - Emoção: {emocao}')
