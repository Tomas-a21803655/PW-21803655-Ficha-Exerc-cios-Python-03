import os

def pede_pasta():
    exist = False
    while exist == False:
        dirPath = input("Enter the folder path: ")
        if os.path.isdir(dirPath):
            return dirPath
        else:
            print('Not a folder')

def calcula_tamanho_pasta(pasta):
    size = os.path.getsize(pasta)
    for item in os.listdir(pasta):
        itempath = os.path.join(pasta, item)
        if os.path.isfile(itempath):
            size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            size += calcula_tamanho_pasta(itempath)
    return size

# print(calcula_tamanho_pasta('exercicio_1'))
