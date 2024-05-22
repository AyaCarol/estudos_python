import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# Encriptar
plain_text = input("Insira uma mensagem para encriptar: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Mensagem original: {plain_text}")
print(f"Mensagem encriptada: {cipher_text}")

# Descriptar
cypher_text = input("Insira uma menssagem para descriptar: ")
plain_text = ""

for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Mensagem encriptada: {cipher_text}")
print(f"Mensagem original: {plain_text}")
