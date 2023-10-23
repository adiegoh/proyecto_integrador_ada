from readchar import readkey, key


while True:
    print("Ingresa una tecla: ")
    caracter = readkey()
    if caracter == key.UP:
        print(f"has presionado la tecla ↑ UP!")
        break
    else:
        print(f"has presiclsonado la tecla {caracter}, sige intentandolo")