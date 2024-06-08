import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta") #ta abrindo um pop up do gerenciador de arquivos

lista_arquivos = os.listdir(caminho) #ta falandos todos os arquivos que tem na pasta

locais = {       #os nomes das pastas para onde vão os arquivos de suas respectivas extensões
    "imagens": [".jpg", "png"],
    "pdf": [".pdf"],
}

for arquivo in lista_arquivos: #Para cada arquivo na pasta
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")#arquivo é o nome do arquivo junto de sua extensao. "nome" ta sendo o caminho(no caso a pasta) e a extensão ta sendo o arquivo dentro da pasta
    for pasta in locais: #ta dizendo que ta olhando pasta por pasta em locais que contem as pastas que serão ciradas para cada arquivo de extensão
        if extensao in locais[pasta]: #Se tiver extensao(arquivo junto de sua extensao) nas pastas criadas em locais
            if not os.path.exists(f"{caminho}/{pasta}"): #Se nao existir a pasta para colocar os arquivos e suas extensos
                os.mkdir(f"{caminho}/{pasta}") #vai criar a pasta com o nome que esta em locais e subir para la o arquivo de sua respectivca estensao(exemplo: jpg e png vai para pasta imagens)
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}" ) #vai dar o nome da pasta nova e nao do arquivo
