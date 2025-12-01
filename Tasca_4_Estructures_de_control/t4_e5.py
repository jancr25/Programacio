#Arxiu: t4_e5.py
#Autor: Jan Carrera Rial
#Data: 24 de novembre de 2025
#Descripció: Programa que a partir d'una llista et diu quins números coincideixen amb la seva posició.

def coincidir_pos(llista):
    coincideix = []
    for i in range(len(llista)):
        if i == llista[i]:
            coincideix.append(i)
    if len(coincideix) > 0:
        print(f"Els números que han coincidit a la seva posició són: {coincideix}")
    else:
        print("No coincideix cap número amb la seva posició.")
            

def main():
    quantitat = int(input("Quants elements vols que tingui la llista? "))
    llista = []

    for i in range(quantitat):
        num = int(input("Introdueix un número a la llista: "))
        llista.append(num)
    

    coincidir_pos(llista)

if __name__ == "__main__":
    main()