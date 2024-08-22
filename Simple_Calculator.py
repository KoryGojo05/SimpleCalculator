# Program that performs the 6 main mathematical calculations
# Addition, Subtraction, Multiplication, Division, Power, Square Root

pro = int(-1)
lng = "EN"

LANGUAGES = {"EN": {"msgpro0": "0. Finish program", "msgpro1": "1. Select panguage",
                    "msgpro2": "2. Calculator",
                    "opr": "Write the number of operation you want to do: ",
                    "ERRORopr": "\nERROR: The indicated number isn't listed.",
                    "oprmsg0": "0. Finish Program", "oprmsg1": "1. Addition",
                    "oprmsg2": "2. Subtraction", "oprmsg3": "3. Multiplication",
                    "oprmsg4": "4. Division", "oprmsg5": "5. Power",
                    "oprmsg6": "6. Square root",
                    "ERRORnum": "ERROR: That isn't a number.",
                    "num1": "Write a number: ", "num2": "Write another number: ",
                    "next": "Press \"Enter\" to continue...",
                    "ERRORnext": "ERROR: Press \"Enter\" to continue...",
                    "finish1": "\nFinishing Program...", "finish2": "The Program Finished",
                    "pownum1": "Write the power base: ",
                    "pownum2": "Write the exponent of power: ",
                    "numlng": "Write the number of language you want: ",
                    "msgsum": "The sum de, %s y de %s es %s",
                    "msgsub": "The subtract of %s and %s is %s",
                    "msgmul": "Multiplication of %s by %s is %s",
                    "msgdiv": "The division of %s between %s is %s",
                    "msgpow": "The power of %s raised to %s is %s",
                    "msgsqr": "The square root of %s is %s",
                    "msglng1": "1. English - English", "msglng2": "2. Spanish - Español",
                    "msglng3": "3. French - Français", "msglng4": "4. German - Deutsch",
                    },
             "ES": {"msgpro0": "0. Finalizar programa", "msgpro1": "1. Seleccionar idioma",
                    "msgpro2": "2. Calculadora",
                    "opr": "Escribe el número del cálculo que quieres hacer: ",
                    "ERRORopr": "ERROR: El carácter indicado no está en la lista.",
                    "oprmsg0": "0. Finalizar Programa", "oprmsg1": "1. Suma",
                    "oprmsg2": "2. Resta", "oprmsg3": "3. Multiplicación",
                    "oprmsg4": "4. División", "oprmsg5": "5. Potencia",
                    "oprmsg6": "6. Raíz cuadrada",
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
                    "msglng1": "1. Inglés - English", "msglng2": "2. Español - Español",
                    "msglng3": "3. Francés - Français", "msglng4": "4. Alemán - Deutsch",
                    },
             "FR": {"msgpro0": "0. Terminer le programme",
                    "msgpro1": "1. Sélectionner la langue",
                    "msgpro2": "2. Calculatrice",
                    "opr": "Écris le numéro du calcul que tu veux faire: ",
                    "ERRORopr": "ERREUR : Le caractère indiqué n'est pas dans la liste.",
                    "oprmsg0": "0. Terminer le programme", "oprmsg1": "1. Addition",
                    "oprmsg2": "2. Soustraction", "oprmsg3": "3. Multiplication",
                    "oprmsg4": "4. Division", "oprmsg5": "5. Puissance",
                    "oprmsg6": "6. Racine carrée",
                    "ERRORnum": "ERREUR : La valeur entrée n'est pas un nombre.",
                    "num1": "Écris un nombre: ", "numlng": "Escribe el número del idioma: ",
                    "num2": "Écris un autre nombre: ",
                    "next": "Appuie sur \"Entrée\" pour continuer...",
                    "ERRORnext": "ERREUR: Appuie sur \"Entrée\" pour continuer...",
                    "finish1": "\nFinalisation du programme...", "finish2": "Programme terminé",
                    "pownum1": "Écris la base de la puissance: ",
                    "pownum2": "Écris l'exposant de la puissance: ",
                    "msgsum": "La somme de %s et de %s est %s",
                    "msgsub": "La soustraction de %s moins %s est %s",
                    "msgmul": "La multiplication de %s par %s est %s",
                    "msgdiv": "La division de %s par %s est %s",
                    "msgpow": "La puissance de %s élevé à %s est %s",
                    "msgsqr": "La racine carrée de %s est %s",
                    "msglng1": "1. Anglais - English", "msglng2": "2. Espagnol - Español",
                    "msglng3": "3. Français - Français", "msglng4": "4. Allemand - Deutsch",
                    },
             "DE": {"msgpro0": "0. Programm beenden", "msgpro1": "1. Sprache auswählen",
                    "msgpro2": "2. Taschenrechner",
                    "opr": "Gib die Nummer der Berechnung ein, die du durchführen möchtest: ",
                    "ERRORopr": "FEHLER: Das angegebene Zeichen befindet sich nicht in der Liste.",
                    "oprmsg0": "0. Programm beenden", "oprmsg1": "1. Addition",
                    "oprmsg2": "2. Subtraktion", "oprmsg3": "3. Multiplikation",
                    "oprmsg4": "4. Division", "oprmsg5": "5. Potenz",
                    "oprmsg6": "6. Quadratwurzel",
                    "ERRORnum": "FEHLER: Der eingegebene Wert ist keine Zahl.",
                    "num1": "Gib eine Zahl ein: ", "numlng": "Gib die Nummer der Sprache ein: ",
                    "num2": "Gib eine weitere Zahl ein: ",
                    "next": "Drücke \"Enter\", um fortzufahren...",
                    "ERRORnext": "FEHLER: Drücke \"Enter\", um fortzufahren...",
                    "finish1": "\nProgramm wird beendet...", "finish2": "Programm beendet",
                    "pownum1": "Gib die Basis der Potenz ein: ",
                    "pownum2": "Gib den Exponenten der Potenz ein: ",
                    "msgsum": "Die summe von %s und %s ist %s",
                    "msgsub": "Die differenz von %s minus %s ist %s",
                    "msgmul": "Die multiplikation von %s mal %s ist %s",
                    "msgdiv": "Die division von %s durch %s ist %s",
                    "msgpow": "Die potenz von %s hoch %s ist %s",
                    "msgsqr": "Die quadratwurzel von %s ist %s",
                    "msglng1": "1. Englisch - English", "msglng2": "2. Spanisch - Español",
                    "msglng3": "3. Französisch - Français", "msglng4": "4. Deutsch - Deutsch",
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
    print("=" * 50)
    for pro_menu in range(0, 3):
        print("\t" + LANGUAGES[lng][f'msgpro{pro_menu}'])
    print("=" * 50)
    pro = input("\n" + LANGUAGES[lng]["opr"])
    try:
        pro = int(pro)
        if pro < 0 or pro > 2:
            print(LANGUAGES[lng]["ERRORopr"])
    except:
        pro = -1
        print(LANGUAGES[lng]["ERRORopr"])
    if pro == 1:
        maxlng = int(4)
        numlng = -1
        while numlng <= 0 or numlng > maxlng:
            print("=" * 50)
            for lng_menu in range(1, 5):
                print("\t" + LANGUAGES[lng][f'msglng{lng_menu}'])
            print("=" * 50)
            numlng = input(LANGUAGES[lng]["numlng"])
            numlng = int(numlng)
            try:
                numlng = int(numlng)
                if numlng <= 0 or numlng > maxlng:
                    print(LANGUAGES[lng]["ERRORopr"])
            except:
                numlng = -1
                print(LANGUAGES[lng]["ERRORopr"])
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
