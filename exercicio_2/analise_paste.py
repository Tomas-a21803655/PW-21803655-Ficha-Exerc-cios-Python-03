import os
from matplotlib import pyplot as plt


def pede_pasta():
    exist = False
    while exist == False:
        dirPath = input("Enter the folder path: ")
        if os.path.isdir(dirPath):
            return dirPath
        else:
            print('Not a folder')


def faz_calculos(pasta):
    analiseDict = {}
    for file in os.listdir(pasta):
        itempath = os.path.join(pasta, file)
        analiseDict[os.path.splitext(
            file)[-1].lower()] = os.path.getsize(itempath)
    print(analiseDict)
    return analiseDict


def faz_grafico_queijos(titulo, lista_chaves, lista_valores):

    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, lista_chaves, lista_valores):

    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()


def main():
    analisados = faz_calculos(pede_pasta())
    lista_chaves = list(analisados.keys())
    lista_valores = list(analisados.values())
    titulo = 'exercicio 2'
    faz_grafico_queijos(titulo, lista_chaves, lista_valores)
    faz_grafico_barras(titulo, lista_chaves, lista_valores)


if __name__ == "__main__":
    main()
