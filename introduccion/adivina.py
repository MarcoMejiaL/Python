import random





def run():
    numero_aleatorio = random.randint(1,100)
    numero_elejido = int(input('introduce un numero entre el 1 y el 100 '))

    while numero_elejido != numero_aleatorio:
        if numero_elejido < numero_aleatorio:
            print('Busca un Numero mas Grande')
        else:
            print('Elije un Numero mas pequeno ')
        numero_elejido = int(input('introduce otro numero '))
    print('Ganaste!')


if __name__ == '__name__':
    run()