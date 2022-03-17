def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    reves=palabra[::-1]
    if palabra==reves:
        return True
    else:
        return False
    
    




def run():
    palabra = input('escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('es Palindromo')
    else:
        print('no es palindromo')


if __name__ == '__main__':
    run()