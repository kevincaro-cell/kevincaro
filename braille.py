braille = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
    "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
    "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽",
    "z": "⠵",

    "1": "⠼⠁", "2": "⠼⠃", "3": "⠼⠉",
    "4": "⠼⠙", "5": "⠼⠑", "6": "⠼⠋",
    "7": "⠼⠛", "8": "⠼⠓", "9": "⠼⠊",
    "0": "⠼⠚",

    " ": " "
}

palabra = input("Ingrese el texto a traducir: ").lower()

textoTraducido = ""

for caracter in palabra:
    if caracter in braille:
        textoTraducido += braille[caracter]
    else:
        textoTraducido += "?"  # para caracteres no reconocidos

# Mostrar resultado
print("\nTraducción a braille:")
print(textoTraducido)

with open("braille.txt", "w", encoding="utf-8") as archivo:
    archivo.write(textoTraducido)

print("\nArchivo braille.txt guardado correctamente")
