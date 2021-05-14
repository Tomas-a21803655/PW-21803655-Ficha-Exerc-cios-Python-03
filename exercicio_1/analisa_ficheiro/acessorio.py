def pede_nome():
    exist = False
    while exist == False:
        filename = input("Enter the file name: ") + ".txt"
        try:
            f = open(filename, "r")
            f.close()
            return filename
        except:
            print("File does not exist")


def gera_nome(filename):
    splitedFilename = filename.split(".")
    return splitedFilename[0]+".json"


# print(gera_nome(pede_nome()))
