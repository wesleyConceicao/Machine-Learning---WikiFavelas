import requests
from bs4 import BeautifulSoup
import urllib.parse



def get_verbetes_da_categoria(categoria_url):
    response = requests.get(categoria_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'index.php?title=' in href:
                full_url = f"https://wikifavelas.com.br/{href}"
                links.append(full_url)

        return links
    else:
        print(f"Falha ao acessar {categoria_url}")
        return []


def get_verbetes_multiple(titulos):
    verbetes = {}

    # Para cada URL de verbete, faz a requisição e coleta o conteúdo
    for titulo in titulos:
        url = f"https://wikifavelas.com.br/index.php?title={titulo}&action=raw"
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            verbetes[titulo] = response.text
        else:
            verbetes[titulo] = None

    return verbetes


# URLs das categorias para coleta dos verbetes
categoria_urls = [
    "https://wikifavelas.com.br/index.php?title=Categoria:Temática_-_Cultura",
    "https://wikifavelas.com.br/index.php?title=Categoria:Temática_-_Saúde",
    "https://wikifavelas.com.br/index.php?title=Categoria:Temática_-_Violência",
    "https://wikifavelas.com.br/index.php?title=Categoria:Temática_-_Sociabilidade_e_Cultura"
]

# Para cada categoria, coleta os verbetes
for categoria_url in categoria_urls:
    print(f"Coletando verbetes da categoria {categoria_url}")

    verbetes = get_verbetes_da_categoria(categoria_url)

    print(f"Verbetes encontrados para a categoria {categoria_url}: {len(verbetes)}")

    if verbetes:
        conteudos = get_verbetes_multiple(verbetes)

        for titulo, conteudo in conteudos.items():
            if conteudo:
                print(f"Conteúdo do verbete {titulo}:")
                print(conteudo[:300])
                print("-" * 50)
            else:
                print(f"Falha ao obter conteúdo do verbete {titulo}")
    else:
        print(f"Não foram encontrados verbetes para a categoria {categoria_url}")

    print("=" * 50)
