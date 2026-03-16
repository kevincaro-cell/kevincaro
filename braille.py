BRAILLE_DICT = {
    "a": "⠁","b": "⠃","c": "⠉","d": "⠙","e": "⠑",
    "f": "⠋","g": "⠛","h": "⠓","i": "⠊","j": "⠚",
    "k": "⠅","l": "⠇","m": "⠍","n": "⠝","o": "⠕",
    "p": "⠏","q": "⠟","r": "⠗","s": "⠎","t": "⠞",
    "u": "⠥","v": "⠧","w": "⠺","x": "⠭","y": "⠽","z": "⠵",

    "1": "⠼⠁","2": "⠼⠃","3": "⠼⠉","4": "⠼⠙","5": "⠼⠑",
    "6": "⠼⠋","7": "⠼⠛","8": "⠼⠓","9": "⠼⠊","0": "⠼⠚",

    ".": "⠲",
    ",": "⠂",
    "?": "⠦",
    "!": "⠖",
    " ": " "
}

def traducir_a_braille(texto):
    resultado = ""

    for caracter in texto.lower():
        if caracter in BRAILLE_DICT:
            resultado += BRAILLE_DICT[caracter]
        else:
            resultado += "?"
import os

def guardar_archivo(texto, ruta="salida/braille.txt"):
    
    os.makedirs("salida", exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    print(f"\nArchivo guardado en: {ruta}")
    return resultado
