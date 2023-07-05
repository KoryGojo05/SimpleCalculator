#!/usr/bin/python -tt
#Programa que realiza los 6 principales cálculos matematicos
#Suma, resta, multiplicación, división, potencia y raíz cuadrada
import math
from math import sqrt

fileinfo=()
maxlng=int(4)
msgpro0=str("\n0. Finalizar Programa")


def languages():
        msglng1=str("1. English")
        msglng2=str("2. Spanish")
        msglng3=str("3. French")
        msglng4=str("4. Deutsch")
        return()


def EN_Calculator():
        wait=0
        opr=-1
        oprmsg0=str("\n0.Finalizar Programa")
        oprmsg1=str("1. Addition")
        oprmsg2=str("2. Subtraction")
        oprmsg3=str("3. Multiplication")
        oprmsg4=str("4. Division")
        oprmsg5=str("5. Power")
        oprmsg6=str("6. Square Root")
        maxopr=int(6)
        while opr!=0:
                print(oprmsg0+"\n"+oprmsg1+"\n"+oprmsg2+"\n"+oprmsg3)
                print(oprmsg4+"\n"+oprmsg5+"\n"+oprmsg6)
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


def ES_Calculator():
        wait=0
        opr=-1
        oprmsg0=str("\n0.Finalizar Programa")
        oprmsg1=str("1. Suma")
        oprmsg2=str("2. Resta")
        oprmsg3=str("3. Multiplicación")
        oprmsg4=str("4. División")
        oprmsg5=str("5. Potencia")
        oprmsg6=str("6. Raíz Cuadrada")
        maxopr=int(6)
        while opr!=0:
                print(oprmsg0+"\n"+oprmsg1+"\n"+oprmsg2+"\n"+oprmsg3)
                print(oprmsg4+"\n"+oprmsg5+"\n"+oprmsg6)
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

while pro!=0:
        print(msgpro0+"\n")
        pro=input("\nEscribe el número del programa que quieres ejecutar: ")
        try:
                pro=int(pro)
                if pro<0 or pro>maxlng:
                        print("\nERROR: El carácter indicado no se encuentra en la lista.")
        except:
                op=-1
                print("\nERROR: El carácter indicado no se encuentra en la lista.")
        
        if pro==1:
                EN_Calculator()
        elif pro==2:
                ES_Calculator()
        
        if pro!=0:
                continuar=input("Presiona \"Enter\" para continuar...")
                while continuar!="":
                        continuar=input("ERROR: Presiona \"Enter\" para continuar...")