"""ANALIZADOR DE TEXTO"""

# Crear un programa que primero le pida al usuario que ingrese un texto. Luego, el programa le va a pedir al usuario que también ingrese tres letras a su elección y a partir de ese momento nuestro código va a procesar esa información para hacer cinco tipos de análisis y devolverle al usuario la siguiente información: 

# Primero: ¿cuántas veces aparece cada una de las letras que eligió?
# Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto.
# Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última.
# Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
# Quinto: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto.


text = input("Ingresa un texto: ")
letters = input("Ingresa tres letras de tu preferencia: ")


# ---Primero---

text_to_upper = text.upper()
letters_to_upper = letters.upper()

count_index_0 = text.count(letters[0])
count_index_1 = text.count(letters[1])
count_index_2 = text.count(letters[2])

print(f"\n- La letra '{letters[0]}' aparece {count_index_0} veces\n")
print(f"- La letra '{letters[1]}' aparece {count_index_1} veces\n")
print(f"- La letra '{letters[2]}' aparece {count_index_2} veces\n")


# ---Segundo---
count_words = len(text.split())

print(f"- Tu texto tiene {count_words} palabras \n")


# ---Tercero---
first_letter = text[0]
last_letter = text[-1]
print(f"- La primera letra de tu texto es {first_letter} y la última es {last_letter} \n")


# ---Cuarto---
invert_text = text[::-1]
print(f"- Tu texto invertido se ve así: '{invert_text}' \n")


# ---Quinto---
python_in_text = "Python" in text

if python_in_text is True:
    print("- La palabra 'Python' se encuentra en el texto \n")
else:
    print("- La palabra 'Python' no se encuentra en el texto \n")