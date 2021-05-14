def calcula_linhas(filename):
    f = open(filename, "r")
    lineCount = 0
    for line in f:
        if line != "\n":
            lineCount += 1
    f.close()
    return lineCount


def calcula_carateres(filename):
    f = open(filename, "r")
    data = f.read()
    nrChar = len(data)
    f.close()
    return nrChar


def calcula_palavra_comprida(filename):
    f = open(filename, "r")
    palavraMaisComprida = ""
    for line in f:
        for word in line.split():
            if len(palavraMaisComprida) < len(word):
                palavraMaisComprida = word
    f.close()
    return palavraMaisComprida


def calcula_ocorrencia_de_letras(filename):
    f = open(filename, "r")
    dictLetras = {}
    for line in f:
        for word in line.split():
            for letter in list(word):
                if letter in dictLetras:
                    dictLetras[letter] += 1
                else:
                    dictLetras[letter] = 1
    f.close()
    return dictLetras


# print(calcula_linhas("testeEx1.json"))
# print(calcula_carateres("testeEx1.txt"))
# print(calcula_palavra_comprida("testeEx1.txt"))
# print(calcula_ocorrencia_de_letras("testeEx1.txt"))
