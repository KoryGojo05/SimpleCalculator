#Program that performs the 6 main mathematical calculations
#Addition, Subtraction, Multiplication, Division, Power, Square Root

pro=int(-1)
lng="EN"

LANGUAGES = { "EN":{"msgpro0":"\n0.Finish Program", "msgpro1":"\n1. Select Language", "msgpro2":"\n2. Calculator", "opr":"\nWrite the number of operation you want to do: ", "oprmsg0":"0. Finish Program", 
                    "oprmsg1":"1. Addition", "oprmsg2":"2. Subtraction", "oprmsg3": "3. Multiplication", "oprmsg4":"4. Division", "oprmsg5":"5. Power", "oprmsg6":"6. Square Root", "ERRORnum":"ERROR: That isn't a number.", 
                    "num1":"Write a number: ", "num2":"Write another number: ", "next":"Press \"Enter\" to continue...", "ERRORnext":"ERROR: Press \"Enter\" to continue...", "finish1":"\nFinishing Program...","finish2":"The program finished", 
                    "ERRORopr":"\nERROR: The indicated number isn't listed.", "pownum1":"Write the power base: ","pownum2":"Write the exponent of power: ", "numlng":"Write the number of language you want: ", 
                    },
                "ES": {"msgpro0":"\n0.Finish Program", "msgpro1":"\n1. Select Language", "msgpro2":"\n2. Calculator","oprmsg0":"0. Finalizar Programa", 
                    "oprmsg1":"1. Sumar", "oprmsg2":"2. Resta", "oprmsg3": "3. Multiplicación", "oprmsg4":"4. División", "oprmsg5":"5. Potencia", "oprmsg6":"6. Raíz Cuadrada", 
                    "ERRORnum":"ERROR: El valor introducido no es un número.","num1":"Escribe un número: ","num2":"Escribe otro número: ", "next":"Presiona \"Enter\" para continuar...", 
                    "ERRORnext":"ERROR: Presiona \"Enter\" para continuar...", "numlng":"Escribe el número del idioma: ",
                    },
                "FR": {

                    },
                "DE": {

                    },
                }


def EN_Calc():
        wait=0
        opr=-1
        maxopr=int(6)
        while opr!=0:
                for opt_menu in range(0,7):
                        print(LANGUAGES[lng][f'oprmsg{opt_menu}'])
                opr=input(LANGUAGES[lng]["opr"])

                try:
                        opr=int(opr)
                        if opr<0 or opr>maxopr:
                                print(LANGUAGES[lng]["ERRORopr"])
                except:
                        opr=-1
                        print(LANGUAGES[lng]["ERRORopr"])
                if opr==1:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        correct=False
                        while correct==False:
                                num1=input(LANGUAGES[lng]["num1"])
                                try:
                                        num1=float(num1)
                                        correct=True
                                except:
                                        print(LANGUAGES[lng]["ERRORnum"])
                        correct=False
                        while correct==False:
                                num2=float(input(LANGUAGES[lng]["num2"]))
                                try:
                                        num2=float(num2)
                                        correct=True
                                except:
                                        print(LANGUAGES[lng]["ERRORnum"])
                        sumt=num1+num2
                        print("The sum of",num1,"and",num2,"is",sumt)

                elif opr==2:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input(LANGUAGES[lng]["num1"]))
                        num2=float(input(LANGUAGES[lng]["num2"]))
                        subt=num1-num2
                        print("Subtract of",num1,"and",num2,"is",subt)

                elif opr==3:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input(LANGUAGES[lng]["num1"]))
                        num2=float(input(LANGUAGES[lng]["num2"]))
                        multi=num1*num2
                        print("Multiplication of",num1,"by",num2,"is",multi)

                elif opr==4:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input(LANGUAGES[lng]["num1"]))
                        num2=float(input(LANGUAGES[lng]["num2"]))
                        div=num1/num2
                        print("The division of",num1,"between",num2,"is",div)

                elif opr==5:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input(LANGUAGES[lng]["pownum1"]))
                        num2=float(input(LANGUAGES[lng]["pownum2"]))
                        pot=num1**num2
                        print("The power of",num1,"raised to",num2,"is",pot)

                elif opr==6:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input(LANGUAGES[lng]["num1"]))
                        square=num1**0.5
                        print("The square root of",num1,"is",square)

                wait=0
                while wait!=10000000:
                        wait+=1
                if opr!=0:
                        next=input(LANGUAGES[lng]["next"])
                        while next!="":
                                next=input(LANGUAGES[lng]["ERRORnext"])

        print(LANGUAGES[lng]["finish1"])
        while wait!=10000000:
                wait=wait+1
        print(LANGUAGES[lng]["finish2"])
        wait=0
        while wait!=5000000:
                wait=wait+1
        return()


def ES_Calc():
        wait=0
        opr=-1
        maxopr=int(6)
        while opr!=0:
                for value in LANGUAGES[lng].values():
                        print(value)
                opr=input("\nEscribe el número del cálculo que quieres hacer: ")

                try:
                        opr=int(opr)
                        if opr<0 or opr>maxopr:
                                print("\nERROR: El carácter indicado no se encuentra en la lista.")
                except:
                        opr=-1
                        print("\nERROR: El carácter indicado no se encuentra en la lista.")

                if opr==1:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        sumt=num1+num2
                        print("La suma de",num1,"y de",num2,"es",sumt)

                elif opr==2:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        resta=num1-num2
                        print("La resta de",num1,"y de",num2,"es",resta)

                elif opr==3:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        multi=num1*num2
                        print("La multiplicación de",num1,"por",num2,"es",multi)

                elif opr==4:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        div=num1/num2
                        print("La división de",num1,"entre",num2,"es",div)

                elif opr==5:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input("Escribe la base de la potencia: "))
                        num2=float(input("Escribe el exponente de la potencia: "))
                        pot=num1**num2
                        print("La potencia de",num1,"elevado a",num2,"es:",pot)

                elif opr==6:
                        print(LANGUAGES[lng][f"oprmsg{opr}"])
                        num1=float(input("Escribe un número: "))
                        raiz=num1**0.5
                        print("La raiz cuadrada de",num1,"es:",raiz)

                wait=0
                while wait!=10000000:
                        wait+=1
                if opr!=0:
                        continuar=input("Presiona \"Enter\" para continuar...")
                        while continuar!="":
                                continuar=input("ERROR: Presiona \"Enter\" para continuar...")

        print(" \nFinalizando Programa...")
        while wait!=10000000:
                wait=wait+1
        print("Programa Finalizado")
        wait=0
        while wait!=5000000:
                wait=wait+1
        return()


while pro!=0:
        print(LANGUAGES[lng]["msgpro0"]+LANGUAGES[lng]["msgpro1"]+LANGUAGES[lng]["msgpro2"])
        pro=input("\nWrite the number of operation you want to do: ")
        try:
                pro=int(pro)
                if pro<0 or pro>2:
                        print("\nERROR: The indicated number isn't listed.")
        except:
                pro=-1
                print("\nERROR: The indicated number isn't listed.")
        if pro==1:
                maxlng=int(4)
                msglng1=str("\n1. English")
                msglng2=str("\n2. Spanish")
                msglng3=str("\n3. French")
                msglng4=str("\n4. Deutsch")
                print(msglng1+msglng2)
                numlng=input(LANGUAGES[lng]["numlng"])
                try:
                        numlng=int(numlng)
                        if numlng<0 or numlng>maxlng:
                                print("\nERROR: The indicated number isn't listed")
                except:
                        numlng=-1
                        print("\nERROR: The indicated number isn't listed")
                if numlng==1:
                        lng="EN"
                elif numlng==2:
                        lng="ES"
                elif numlng==3:
                        lng="FR"
                elif numlng==4:
                        lng="DE"
                lng=str(lng)
        elif pro==2:
                if lng=="EN":
                        EN_Calc()
                elif lng=="ES":
                        ES_Calc()


print("\nFinishing Program...")
wait=0
while wait!=10000000:
        wait=wait+1
print("The Program Finished")
wait=0
while wait!=5000000:
        wait=wait+1