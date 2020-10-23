class Cuenta:
    def __init__(self):
        self.cuenta = 0.00

    def egresoRegistro (self, egresoR):
        self.cuenta-=egresoR
        print (f"Se retiraron $ {egresoR:.2f}.")
        print (f"El saldo total en esta cuenta es de $ {self.cuenta:.2f}.")

    def ingresoRegistro (self, ingresoR):
        self.cuenta+=ingresoR
        print (f"Se retiraron $ {ingresoR:.2f}.")
        print (f"El saldo total en esta cuenta es de $ {self.cuenta:.2f}.")

class Egreso:
    def __init__(self):
        self.egreso = 0.00

    def egresoAñadir (self, egresosCantidad):
        self.egreso-=egresosCantidad
        return egresosCantidad

class Ingreso:
    def __init__(self):
        self.ingreso = 0.00

    def ingresoAñadir (self, ingresosCantidad):
        self.ingreso+=ingresosCantidad
        return ingresosCantidad
       
finanzas = Cuenta()
registrarE = Egreso()
registrarI = Ingreso()
print("Se ha inicializado correctamente esta cuenta.")

while True:
    Menu="""Ingrese el número de la opción que desee escoger
    0- Salir.
    1- Registrar ingreso.
    2- Registrar egreso.
    3- Solicitar reporte de ingresos.
    4- Solicitar reporte de egresos.
    5- Solicitar reporte de transacciones en ingresos y egresos.
    6- Solicitar saldo total en la cuenta."""
    print(Menu)
    opcion=int(input("¿Qué opción desea escoger?"))
    if opcion==0:
        break
    elif opcion==1:
        print("-"*100)
        ingreso= round(float(input("¿Cuánto desea agregar a la cuenta?")),2)
        finanzas.ingresoRegistro(registrarI.ingresoAñadir(ingreso))
        print("-"*100)
    elif opcion==2:
        print("-"*100)
        egreso= round(float(input("¿Cuánto desea agregar a la cuenta?")),2)
        finanzas.egresoRegistro(registrarE.egresoAñadir(egreso))
        print("-"*100)
    elif opcion==3:
        ingresosTotales = registrarI.ingreso
        print("-"*100)
        print(f"Usted ha ingresado un total de $"+str(ingresosTotales)+".")
        print("-"*100)
    elif opcion==4:
        egresosTotales = registrarE.egreso
        print("-"*100)
        print(f"Usted ha retirado un total de $"+str(egresosTotales)+".")
        print("-"*100)
    elif opcion==5:
        repTIngresos = registrarI.ingreso
        repTEgresos = registrarE.egreso
        print("-"*100)
        mensaje = """Reporte de transacciones:
        Ingresos Totales: $"""+str(repTIngresos)+"""
        Egresos Totales: $"""+str(repTEgresos)+"."
        print(mensaje)
        print("-"*100)
    elif opcion==6:
        print("-"*100)
        saldo = finanzas.cuenta
        print("Su saldo en cuenta es de $"+str(saldo)+".")
        print("-"*100)

