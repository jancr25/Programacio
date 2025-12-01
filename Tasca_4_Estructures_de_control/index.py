import t4_e1
import t4_e2
import t4_e3
import t4_e4
import t4_e5
import t4_e6

def main():
    menu = int(input("Del 1 al 6 tria quin exercici vols executar: "))

    if menu == 1:
        t4_e1.main()
    
    elif menu == 2:
        t4_e2.main()
    
    elif menu == 3:
        t4_e3.main()
    
    elif menu == 4:
        t4_e4.main()
    
    elif menu == 5:
        t4_e5.main()
    
    elif menu == 6:
        t4_e6.main()

if __name__ == "__main__":
    main()