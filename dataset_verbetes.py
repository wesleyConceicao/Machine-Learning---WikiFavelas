import pandas as pd

data = {
    'Verbetes': [
        'Arte', 'Esporte', 'Gênero e Sexualidade', 'Juventude', 'Relações Étnico-Raciais',
        'Religião', 'Sociabilidade', 'Violência', 'Economia e Mercado', 'Educação',
        'Habitação', 'Meio Ambiente', 'Mobilidades', 'Saúde', 'Segurança', 'Urbanização',
        'Associativismo e Movimentos Sociais', 'Favelas e Periferias', 'Instituições',
        'Lideranças', 'Mídia e Comunicação', 'Pesquisadores e Pesquisadoras', 'Pesquisas',
        'Atenção Primária de Saúde', 'Coronavírus', 'Direitos', 'Educação e pesquisa', 'Enfermidades e causalidades',
        'Políticas', 'Promoção da saúde', 'Saúde mental', 'Serviços e ações', 'SUS', 'Terapias e tecnologias'
    ],
    'Categoria': [
        'Sociabilidade e Cultura', 'Sociabilidade e Cultura', 'Sociabilidade e Cultura', 'Sociabilidade e Cultura',
        'Sociabilidade e Cultura', 'Sociabilidade e Cultura', 'Sociabilidade e Cultura', 'Sociabilidade e Cultura',
        'Estado e Mercado', 'Estado e Mercado', 'Estado e Mercado', 'Estado e Mercado', 'Estado e Mercado',
        'Estado e Mercado', 'Estado e Mercado', 'Estado e Mercado', 'Associativismo e Memória',
        'Associativismo e Memória', 'Associativismo e Memórias', 'Associativismo e Memória', 'Associativismo e Memória',
        'Associativismo e Memória', 'Associativismo e Memória', 'Saúde', 'Saúde', 'Saúde', 'Saúde', 'Saúde', 'Saúde',
        'Saúde', 'Saúde', 'Saúde', 'Saúde', 'Saúde'
    ]
}

df = pd.DataFrame(data)
df.to_csv('dados_verbetes.csv', index=False)
