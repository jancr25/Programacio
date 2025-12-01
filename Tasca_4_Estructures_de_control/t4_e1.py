#Arxiu: t4_e1.py
#Autor: Jan Carrera Rial
#Data: 24 de novembre de 2025
#Descripció: Programa que li escrius un número decimal i et diu quina nota has tret.


def treure_nota(nota):
    if nota < 4.5 and nota >= 0:
        print("Has suspès!!")
    
    elif nota > 4.4 and nota < 6.5:
        print("Has aprovat!!")
    
    elif nota > 6.4 and nota < 8.5:
        print("Has tret un notable!!")

    elif nota > 8.4 and nota < 10.1:
        print("Felicitaaatss, has tret un excel·lent!!!")

    elif nota < 0 or nota > 10:
        print("La nota ha de ser entre 0 i 10!!")

def main():
    nota = float(input("Escriviu la vostra nota del 0 al 10 amb un nombre decimal: ")) 

    treure_nota(nota)

if __name__ == "__main__":
    main()