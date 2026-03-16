from braille import traducir
from archivo import guardar

print("Traductor Español a Braille\n")

texto = input("Ingrese texto: ")

resultado = traducir(texto)

print("\nResultado en braille:")
print(resultado)

guardar(resultado)
