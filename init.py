import os

path = input('Digite o diretório a ser buscado: ')
if path == "" : 
    path = "/home/rodrigo/code/frontapp/pingwin/v8/NFe"
files = os.listdir(path)
for file in files:
    print(file)
    