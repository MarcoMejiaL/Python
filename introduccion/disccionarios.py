def run():
    jason={
        'name': 'marco',
        'age': 30,
        'food': 'taquitos'
    }
    for llave, dato in jason.items():
        print(llave + ' '+ 'tiene ' + str(dato))


if __name__ == '__main__':
    run()

#al final muestra marco, 30 y taquitos que son los valores dentro del "objeo"