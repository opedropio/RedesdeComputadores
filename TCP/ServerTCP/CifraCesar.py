def cifrar (texto, chave): 
    resultado = ""
    for caractere in texto: 
        if "a" <= caractere <= "z":
            base = ord ("a")
        elif "A" <= caractere <= "Z":
            base = ord ("A")
        else:
            resultado += caractere
            continue
        resultado += chr ((ord(caractere) - base + chave) % 26 + base)
    return resultado

def decifrar (texto, chave): 
    return cifrar(texto, -chave)
      

