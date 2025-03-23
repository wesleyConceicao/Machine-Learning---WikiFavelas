import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
df = pd.read_csv('dados_verbetes.csv')


nlp = spacy.load("pt_core_news_sm")


def preprocess_text(text):
    doc = nlp(text)

    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    return " ".join(tokens)


titulos = [
    "Temática - Cultura", "Temática - Esporte", "Temática - Gênero e Sexualidade",
    "Temática - Juventude", "Temática - Relações Étnico-Raciais", "Temática - Religião",
    "Temática - Sociabilidade", "Temática - Violência", "Temática - Economia e Mercado",
    "Temática - Educação", "Temática - Habitação", "Temática - Meio Ambiente",
    "Temática - Mobilidades", "Temática - Saúde", "Temática - Segurança", "Temática - Urbanização",
    "Temática - Associativismo e Movimentos Sociais", "Temática - Favelas e Periferias",
    "Temática - Instituições", "Temática - Lideranças", "Temática - Mídia e Comunicação",
    "Temática - Pesquisadores e Pesquisadoras", "Temática - Pesquisas",
    "Temática - Atenção Primária de Saúde", "Temática - Coronavírus", "Temática - Direitos",
    "Temática - Educação e pesquisa", "Temática - Enfermidades e causalidades", "Temática - Políticas",
    "Temática - Promoção da saúde", "Temática - Saúde", "Temática - Saúde mental", "Temática - Serviços e ações",
    "Temática - SUS", "Temática - Terapias e tecnologias"
]


verbetes = get_verbetes_multiple(titulos)

for titulo, texto in verbetes.items():
    if texto:
        print(f"Verbetes: {titulo}")
        print(f"Texto: {texto[:100]}...")  # Exibe os primeiros 100 caracteres de cada verbete
    else:
        print(f"O verbete '{titulo}' não possui texto.")

data = {'Verbetes': [], 'Categoria': []}
for titulo, texto in verbetes.items():
    if texto:  # Verifica se o verbete foi coletado com sucesso
        data['Verbetes'].append(texto)
        data['Categoria'].append(titulo)

if len(data['Verbetes']) < 2:
    print("Erro: Não há dados suficientes para dividir entre treino e teste.")
else:
    # Criar um DataFrame
    df = pd.DataFrame(data)

    df['texto_limpo'] = df['Verbetes'].apply(preprocess_text)

    # Define as variáveis de entrada (X) e saída (y)
    X = df['texto_limpo']
    y = df['Categoria']

    # Divide os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    y_pred = model.predict(X_test_tfidf)

    print("Acurácia: ", model.score(X_test_tfidf, y_test))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

    # Predição de um novo exemplo
    exemplo = ["Arte de rua no Brasil"]
    exemplo_tfidf = vectorizer.transform(exemplo)
    predicao = model.predict(exemplo_tfidf)
    print(f'Categoria predita: {predicao[0]}')
