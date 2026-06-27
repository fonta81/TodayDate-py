import datetime

now = datetime.datetime.now()
Hoy = now.strftime("%Y/%m/%d")


class Calendario:
    def DiaDelMes(self):
        today = now.strftime("%d")
        return today

    def NumeroDelMes(self):
        today = now.strftime("%m")
        return today

    def AnoActual(self):
        today = now.strftime("%Y")
        return today

    def Siglo(self):
        anno = now.year
        siglo = (anno - 1) // 100 + 1
        return siglo

    def AnoMesDia(self):
        return Hoy


def menu():
    Cal = Calendario()
    while True:
        print("=" * 60)
        print("-" * 60)
        print("1.Dia del mes    2.Numero Del mes  3.Ano actual")
        print("-" * 60)
        print("4.Fecha actual   5.Siglo actual")
        print("-" * 60)
        print("6.Salir")
        while True:
            try:
                n = int(input("\nElige: "))
                break
            except ValueError:
                print("Ingrese un numero")

        if n in (range(1, 8)):
            if n == 1:
                Dia_Mes = Cal.DiaDelMes()
                print(f"El Dia de hoy es: {Dia_Mes} ")
            elif n == 2:
                Num_Mes = Cal.NumeroDelMes()
                print(f"El mes actual es: {Num_Mes}")
            elif n == 3:
                Ano_actual = Cal.AnoActual()
                print(f"El mes actual es: {Ano_actual}")
            elif n == 4:
                Fecha_Actual = Cal.AnoMesDia()
                print(f"El mes actual es: {Fecha_Actual}")
            elif n == 5:
                Siglo_Actual = Cal.Siglo()
                print(f"El mes actual es: {Siglo_Actual}")
            elif n == 6:
                break
        else:
            print("Ingresa un valor valido")


menu()
