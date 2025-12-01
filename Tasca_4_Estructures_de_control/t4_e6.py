#Arxiu: t4_e6.py
#Autor: Jan Carrera Rial
#Data: 24 de novembre de 2025
#Descripció: Programa que a partir d'una llista de números et mostra ek nombre d'elements, la mitjana i quants són parells i imparells.

def dades_num():
    nums = input("Introdueix números separats per comes per crear una llista: ")
    llista = []
    parells = 0
    imparells = 0

    for i in range(len(nums)):
        if i % 2 == 0:
            num = int(nums[i])
            llista.append(num)
            if num % 2 == 0:
                parells += 1
            else:
                imparells += 1
    
    print(f"La llista conté {len(llista)} elements.")
    print(f"La mitjana és: {sum(llista)/len(llista)}")
    print(f"A la llista hi ha {parells} parells i {imparells} imparells.")


def main():
    dades_num()

if __name__ == "__main__":
    main()