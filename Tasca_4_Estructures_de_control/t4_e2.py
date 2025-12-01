#Arxiu: t4_e2.py
#Autor: Jan Carrera Rial
#Data: 24 de novembre de 2025
#Descripció: Programa que a partir de 2 números et diu quin és més gran o si són iguals.


def compara_num():
    try:
        num1 = int(input("Escriviu un número: "))
        num2 = int(input("Escriviu un altre número: "))

        if num1 > num2:
            print(f"El {num1} és més gran que el {num2}.")
    
        elif num1 < num2:
            print(f"El {num2} és més gran que el {num1}.")
        
        else:
            print("Els dos números són iguals.")

    except ValueError:
        print("Has de introduir valors numèrics.")
    

def main():
    compara_num()

if __name__ == "__main__":
    main()