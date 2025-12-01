#Arxiu: t4_e4.py
#Autor: Jan Carrera Rial
#Data: 24 de novembre de 2025
#Descripció: Programa que a partir d'una llista et diu si és simètrica o no entre d'altres coses.

def llista_simetrica(llista):
    simetrica = True

    for i in range(len(llista)):
        if llista[i] != llista[((len(llista)-1) - i)]:
            print("La llista no és simètrica!")
            simetrica = False
            break
    
    if simetrica:
        print("La llista és simètrica!")
            

def main():
    quantitat = int(input("Quants elements vols que tingui la llista? "))
    llista = []

    for i in range(quantitat):
        num = int(input("Introdueix un número a la llista: "))
        llista.append(num)
    

    llista_simetrica(llista)

if __name__ == "__main__":
    main()