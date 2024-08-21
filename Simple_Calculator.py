# Program that performs the 6 main mathematical calculations
# Addition, Subtraction, Multiplication, Division, Power, Square Root

pro = int(-1)
lng = "EN"

LANGUAGES = {"EN": {"msgpro0": "\n0. Finish Program", "msgpro1": "\n1. Select Language",
                    "msgpro2": "\n2. Calculator",
                    "opr": "Write the number of operation you want to do: ",
                    "oprmsg0": "0. Finish Program", "oprmsg1": "1. Addition",
                    "oprmsg2": "2. Subtraction", "oprmsg3": "3. Multiplication",
                    "oprmsg4": "4. Division", "oprmsg5": "5. Power",
                    "oprmsg6": "6. Square Root",
                    "ERRORnum": "ERROR: That isn't a number.",
                    "num1": "Write a number: ", "num2": "Write another number: ",
                    "next": "Press \"Enter\" to continue...",
                    "ERRORnext": "ERROR: Press \"Enter\" to continue...",
                    "finish1": "\nFinishing Program...", "finish2": "The Program Finished",
                    "ERRORopr": "\nERROR: The indicated number isn't listed.",
                    "pownum1": "Write the power base: ",
                    "pownum2": "Write the exponent of power: ",
                    "numlng": "Write the number of language you want: ",
                    "msgsum": "The sum de, %s y de %s es %s",
                    "msgsub": "The subtract of %s and %s is %s",
                    "msgmul": "Multiplication of %s by %s is %s",
                    "msgdiv": "The division of %s between %s is %s",
                    "msgpow": "The power of %s raised to %s is %s",
                    "msgsqr": "The square root of %s is %s",
                    "msglng1": "\t1. English", "msglng2": "\t2. Spanish",
                    },
             "ES": {"msgpro0": "\n0. Finalizar Programa", "msgpro1": "\n1. Seleccionar Idioma",
                    "msgpro2": "\n2. Calculadora",
                    "opr": "Escribe el número del cálculo que quieres hacer: ",
                    "ERRORopr": "ERROR: El carácter indicado no es un número.",
                    "oprmsg0": "0. Finalizar Programa", "oprmsg1": "1. Sumar",
                    "oprmsg2": "2. Resta", "oprmsg3": "3. Multiplicación",
                    "oprmsg4": "4. División", "oprmsg5": "5. Potencia",
                    "oprmsg6": "6. Raíz Cuadrada",
                    "ERRORnum": "ERROR: El valor introducido no es un número.",
                    "num1": "Escribe un número: ", "numlng": "Escribe el número del idioma: ",
                    "num2": "Escribe otro número: ", "next": "Presiona \"Enter\" para continuar...",
                    "ERRORnext": "ERROR: Presiona \"Enter\" para continuar...",
                    "finish1": "\nFinalizando Programa...", "finish2": "Programa Finalizado",
                    "pownum1": "Escribe la base de la potencia: ",
                    "pownum2": "Escribe el exponente de la potencia: ",
                    "msgsum": "La suma de %s y de %s es %s",
                    "msgsub": "La resta de %s menos %s es %s",
                    "msgmul": "La multiplicación de %s por %s es %s",
                    "msgdiv": "La división de %s entre %s es %s",
                    "msgpow": "La potencia de %s elevado a %s es %s",
                    "msgsqr": "La raiz cuadrada de %s es: %s",
                    "msglng1": "\t1. Inglés", "msglng2": "\t2. Español",
                    },
             "FR": {

             },
             "DE": {

             },
             }


def calc():
    wait = 0
    opr = -1
    maxopr = int(6)
    while opr != 0:
        print("=" * 50)
        for opt_menu in range(0, 7):
            print("\t" + LANGUAGES[lng][f'oprmsg{opt_menu}'])
        print("=" * 50)
        opr = input(LANGUAGES[lng]["opr"])

        try:
            opr = int(opr)
            if opr < 0 or opr > maxopr:
                print(LANGUAGES[lng]["ERRORopr"])
        except:
            opr = -1
            print(LANGUAGES[lng]["ERRORopr"])
        if opr == 1:
            print(LANGUAGES[lng][f"oprmsg{opr}"])
            correct = False
            while not correct:
                num1 = input(LANGUAGES[lng]["num1"])
                try:
                    num1 = float(num1)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            correct = False
            while not correct:
                num2 = float(input(LANGUAGES[lng]["num2"]))
                try:
                    num2 = float(num2)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            result = num1 + num2
            print(LANGUAGES[lng]["msgsum"] % (num1, num2, result))

        elif opr == 2:
            print(LANGUAGES[lng][f"oprmsg{opr}"])
            correct = False
            while not correct:
                num1 = input(LANGUAGES[lng]["num1"])
                try:
                    num1 = float(num1)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            correct = False
            while not correct:
                num2 = float(input(LANGUAGES[lng]["num2"]))
                try:
                    num2 = float(num2)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            result = num1 - num2
            print(LANGUAGES[lng]["msgsub"] % (num1, num2, result))

        elif opr == 3:
            print(LANGUAGES[lng][f"oprmsg{opr}"])
            correct = False
            while not correct:
                num1 = input(LANGUAGES[lng]["num1"])
                try:
                    num1 = float(num1)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            correct = False
            while not correct:
                num2 = float(input(LANGUAGES[lng]["num2"]))
                try:
                    num2 = float(num2)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            result = num1 * num2
            print(LANGUAGES[lng]["msgmul"] % (num1, num2, result))

        elif opr == 4:
            print(LANGUAGES[lng][f"oprmsg{opr}"])
            correct = False
            while not correct:
                num1 = input(LANGUAGES[lng]["num1"])
                try:
                    num1 = float(num1)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            correct = False
            while not correct:
                num2 = float(input(LANGUAGES[lng]["num2"]))
                try:
                    num2 = float(num2)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            result = num1 / num2
            print(LANGUAGES[lng]["msgdiv"] % (num1, num2, result))

        elif opr == 5:
            print(LANGUAGES[lng][f"oprmsg{opr}"])
            correct = False
            while not correct:
                num1 = float(input(LANGUAGES[lng]["pownum1"]))
                try:
                    num1 = float(num1)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            correct = False
            while not correct:
                num2 = float(input(LANGUAGES[lng]["pownum2"]))
                try:
                    num2 = float(num2)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            result = num1 ** num2
            print(LANGUAGES[lng]["msgpow"] % (num1, num2, result))

        elif opr == 6:
            print(LANGUAGES[lng][f"oprmsg{opr}"])
            correct = False
            while not correct:
                num1 = float(input(LANGUAGES[lng]["num1"]))
                try:
                    num1 = float(num1)
                    correct = True
                except:
                    print(LANGUAGES[lng]["ERRORnum"])
            result = num1 ** 0.5
            print(LANGUAGES[lng]["msgsqr"] % (num1, result))

        wait = 0
        while wait != 10000000:
            wait += 1
        if opr != 0:
            next = input(LANGUAGES[lng]["next"])
            while next != "":
                next = input(LANGUAGES[lng]["ERRORnext"])

    print(LANGUAGES[lng]["finish1"])
    while wait != 10000000:
        wait = wait + 1
    print(LANGUAGES[lng]["finish2"])
    wait = 0
    while wait != 5000000:
        wait = wait + 1
    return ()


while pro != 0:
    print(LANGUAGES[lng]["msgpro0"] + LANGUAGES[lng]["msgpro1"] + LANGUAGES[lng]["msgpro2"])
    pro = input("\n" + LANGUAGES[lng]["opr"])
    try:
        pro = int(pro)
        if pro < 0 or pro > 2:
            print("\nERROR: The indicated number isn't listed.")
    except:
        pro = -1
        print("\nERROR: The indicated number isn't listed.")
    if pro == 1:
        maxlng = int(2)
        """
        msglng1 = str("1. English")
        msglng2 = str("2. Spanish")
        msglng3 = str("3. French")
        msglng4 = str("4. Deutsch")
        """
        numlng = -1
        while numlng <= 0 or numlng > maxlng:
            print("=" * 50 + "\n" + LANGUAGES[lng]["msglng1"])
            print(LANGUAGES[lng]["msglng2"] + "\n" + "=" * 50)
            numlng = input(LANGUAGES[lng]["numlng"])
            numlng = int(numlng)
            try:
                numlng = int(numlng)
                if numlng <= 0 or numlng > maxlng:
                    print("\nERROR: The indicated number isn't listed")
            except:
                numlng = -1
                print("\nERROR: The indicated number isn't listed")
        if numlng == 1:
            lng = "EN"
        elif numlng == 2:
            lng = "ES"
        elif numlng == 3:
            lng = "FR"
        elif numlng == 4:
            lng = "DE"
        lng = str(lng)
    elif pro == 2:
        calc()

print("\nFinishing Program...")
wait = 0
while wait != 10000000:
    wait = wait + 1
print("The Program Finished")
wait = 0
while wait != 5000000:
    wait = wait + 1
