import analisa_ficheiro
import json


def main():
    fichTxt = analisa_ficheiro.pede_nome()
    lineCount = analisa_ficheiro.calcula_linhas(fichTxt)
    charCount = analisa_ficheiro.calcula_carateres(fichTxt)
    longestString = analisa_ficheiro.calcula_palavra_comprida(fichTxt)
    letterOccurences = analisa_ficheiro.calcula_ocorrencia_de_letras(fichTxt)
    fichJson = analisa_ficheiro.gera_nome(fichTxt)

    fileAnalysis = {
        "Nome Ficheiro.txt": fichTxt,
        "Nr Linhas": lineCount,
        "Nr Chars": charCount,
        "String Maior": longestString,
        "Occorencia de Letras": letterOccurences,
    }

    with open(fichJson, 'w') as json_file:
        json.dump(fileAnalysis, json_file, indent=4)


if __name__ == "__main__": 
    main()
