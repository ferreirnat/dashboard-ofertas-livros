"""Leitura dos arquivos CSV do projeto.
"""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros_v1():
    arquivo = None
    try:
        arquivo = open(CAMINHO_LIVROS, "r", encoding="utf-8")
        livros = arquivo.read()
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Ocorreu algum erro na leitura do arquivo.", error)
    finally:
        if arquivo is not None:
            arquivo.close()
    return livros

def ler_livros_v2():
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Ocorreu algum erro na leitura do arquivo.", error)

def ler_livros_v3():
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                print(linha["titulo"])
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Ocorreu algum erro na leitura do arquivo.", error)

def ler_livros_v4():
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Ocorreu algum erro na leitura do arquivo.", error)
    return livros

def calcular_preco_medio(livros):
    soma: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: float = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        soma += preco_num
    preco_medio: float = soma / len(livros)
    return preco_medio

def contar_cinco_estrelas(livros):
    contador: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if livro["nota"] == "Five":
            contador += 1
    return contador

def encontrar_livro_mais_caro(livros):
    livro_mais_caro = None
    maior_preco: float = 0
    for livro in livros:
        preco_num: float = float(livro["preco"].replace("£", ""))
        if preco_num > maior_preco:
            maior_preco = preco_num
            livro_mais_caro = livro
    return livro_mais_caro, maior_preco
        
if __name__ == "__main__":
    livros = ler_livros_v4()
    
    print(f"A quantidade de livros na coleção é de {len(livros)} livros.")

    preco_medio: float = calcular_preco_medio(livros)
    print(f"O preco medio é de £{preco_medio:.2f}")

    cinco_estrelas = contar_cinco_estrelas(livros)
    print(f"A quantidade de livros com 5 estrelas é de {cinco_estrelas} livros.")