import spacy

# Carregar o modelo de linguagem em português
nlp = spacy.load("pt_core_news_sm")


def preprocess_text(text):

    doc = nlp(text)

    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    return tokens


verbete_texto = '''A arte e a rua (filme etnográfico) apresenta Cidade Tiradentes, distrito no extremo Leste de São Paulo, lugar onde a cidade termina, ou começa...'''

processed_text = preprocess_text(verbete_texto)
print(processed_text)
