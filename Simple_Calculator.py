#!/usr/bin/python -tt
#Program that performs the 6 main mathematical calculations
#Addition, Subtraction, Multiplication, Division, Power, Square Root
import math
from math import sqrt


pro=int(-1)
msgpro0=str("\n0.Finish Program")
msgpro1=str("\n1. Select Language")
msgpro2=str("\n2. Calculator")
lng="EN"

"""
def lang():
        maxlng=int(4)
        msglng1=str("\n1. English")
        msglng2=str("\n2. Spanish")
        msglng3=str("\n3. French")
        msglng4=str("\n4. Deutsch")
        print(msglng1+msglng2)
        numlng=input("Write the number of language you want: ")
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
        return()


"""

def EN_Calc():
        wait=0
        opr=-1
        oprmsg0=str("\n0.Finish Program")
        oprmsg1=str("\n1. Addition")
        oprmsg2=str("\n2. Subtraction")
        oprmsg3=str("\n3. Multiplication")
        oprmsg4=str("\n4. Division")
        oprmsg5=str("\n5. Power")
        oprmsg6=str("\n6. Square Root")
        maxopr=int(6)
        while opr!=0:
                print(oprmsg0+oprmsg1+oprmsg2+oprmsg3+oprmsg4+oprmsg5+oprmsg6)
                opr=input("\nWrite the number of operation you want to do: ")

                try:
                        opr=int(opr)
                        if opr<0 or opr>maxopr:
                                print("\nERROR: The indicated number isn't listed.")
                except:
                        opr=-1
                        print("\nERROR: The indicated number isn't listed.")
                if opr==1:
                        print(oprmsg1)
                        correct=False
                        while correct==False:
                                num1=input("Write a number: ")
                                try:
                                        num1=float(num1)
                                        correct=True
                                except:
                                        print("\nERROR: That isn't a number.")
                               
                                
                        num2=float(input("Write another number: "))
                        sumt=num1+num2
                        print("The sum of",num1,"and",num2,"is",sumt)

                elif opr==2:
                        print(oprmsg2)
                        num1=float(input("Write a number: "))
                        num2=float(input("Write another number: "))
                        subt=num1-num2
                        print("Subtract of",num1,"and",num2,"is",subt)

                elif opr==3:
                        print(oprmsg3)
                        num1=float(input("Write a number: "))
                        num2=float(input("Write another number: "))
                        multi=num1*num2
                        print("Multiplication of",num1,"by",num2,"is",multi)

                elif opr==4:
                        print(oprmsg4)
                        num1=float(input("Write a number: "))
                        num2=float(input("Write another number: "))
                        div=num1/num2
                        print("The division of",num1,"between",num2,"is",div)

                elif opr==5:
                        print(oprmsg5)
                        num1=float(input("Write the power base: "))
                        num2=float(input("Write the exponent of power: "))
                        pot=num1**num2
                        print("The power of",num1,"raised to",num2,"is",pot)

                elif opr==6:
                        print(oprmsg6)
                        num1=float(input("Write a number: "))
                        square=sqrt(num1)
                        print("The square root of",num1,"is",square)

                wait=0
                while wait!=10000000:
                        wait+=1
                if opr!=0:
                        next=input("Press \"Enter\" to continue...")
                        while next!="":
                                next=input("ERROR: Press \"Enter\" to continue...")

        print(" \nFinishing Program...")
        while wait!=10000000:
                wait=wait+1
        print("The program finished")
        wait=0
        while wait!=5000000:
                wait=wait+1
        return()

def new_func(num1):
    return num1


def ES_Calc():
        wait=0
        opr=-1
        oprmsg0=str("\n0.Finalizar Programa")
        oprmsg1=str("\n1. Suma")
        oprmsg2=str("\n2. Resta")
        oprmsg3=str("\n3. Multiplicación")
        oprmsg4=str("\n4. División")
        oprmsg5=str("\n5. Potencia")
        oprmsg6=str("\n6. Raíz Cuadrada")
        maxopr=int(6)
        while opr!=0:
                print(oprmsg0+oprmsg1+oprmsg2+oprmsg3+oprmsg4+oprmsg5+oprmsg6)
                opr=input("\nEscribe el número del cálculo que quieres hacer: ")

                try:
                        opr=int(opr)
                        if opr<0 or opr>maxopr:
                                print("\nERROR: El carácter indicado no se encuentra en la lista.")
                except:
                        opr=-1
                        print("\nERROR: El carácter indicado no se encuentra en la lista.")

                if opr==1:
                        print(oprmsg1)
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        sumt=num1+num2
                        print("La suma de",num1,"y de",num2,"es",sumt)

                elif opr==2:
                        print(oprmsg2)
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        resta=num1-num2
                        print("La resta de",num1,"y de",num2,"es",resta)

                elif opr==3:
                        print(oprmsg3)
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        multi=num1*num2
                        print("La multiplicación de",num1,"por",num2,"es",multi)

                elif opr==4:
                        print(oprmsg4)
                        num1=float(input("Escribe un número: "))
                        num2=float(input("Escribe otro número: "))
                        div=num1/num2
                        print("La división de",num1,"entre",num2,"es",div)

                elif opr==5:
                        print(oprmsg5)
                        num1=float(input("Escribe la base de la potencia: "))
                        num2=float(input("Escribe el exponente de la potencia: "))
                        pot=num1**num2
                        print("La potencia de",num1,"elevado a",num2,"es:",pot)

                elif opr==6:
                        print(oprmsg6)
                        num1=float(input("Escribe un número: "))
                        raiz=sqrt(num1)
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


def FR_Calc():

        return()


def DE_Calc():

        return()


while pro!=0:
        print(msgpro0+msgpro1+msgpro2)
        pro=input("\nWrite the number of operation you want to do: ")
        try:
                pro=int(pro)
                if pro<0 or pro>2:
                        print("\nERROR: The indicated number isn't listed.")
        except:
                pro=-1
                print("\nERROR: The indicated number isn't listed.")
        if pro==1:
                #lang()
                maxlng=int(4)
                msglng1=str("\n1. English")
                msglng2=str("\n2. Spanish")
                msglng3=str("\n3. French")
                msglng4=str("\n4. Deutsch")
                print(msglng1+msglng2)
                numlng=input("Write the number of language you want: ")
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
                elif lng=="FR":
                        FR_Calc()
                elif lng=="DE":
                        DE_Calc()

print("\nFinishing Program...")
wait=0
while wait!=10000000:
        wait=wait+1
print("The Program Finished")
wait=0
while wait!=5000000:
        wait=wait+1