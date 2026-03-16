def guardar(texto):

    archivo = open("braille.txt","w",encoding="utf-8")
    archivo.write(texto)
    archivo.close()

    print("Archivo guardado como braille.txt")
