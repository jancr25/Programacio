#Arxiu: t4_e3.py
#Autor: Jan Carrera Rial
#Data: 24 de novembre de 2025
#Descripció: Programa que a partir de un nom i un número et mostra el teu nom repetit tants cops com indiqui el número.

def repetir_nom():
    nom = input("Escriu el teu nom: ")
    num = int(input("Escriviu un número: "))

    if num == 0:
        print("El número ha de ser més gran que 0!!")
    
    if num < 0:
        print("Avís: Millor introdueix números positius.")
        num = num * (-1)

    repeticio = ""

    for i in range(num):
        if i == num-1:
            repeticio += nom 
        else: 
            repeticio += nom + ", "
    
    print(repeticio)


def main():
    repetir_nom()

if __name__ == "__main__":
    main()