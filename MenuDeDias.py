import datetime
Now = datetime.datetime.now()

def DiaHoy():
    hoy = Now.strftime("%d/%m/%Y")
    print(f'El dia de hoy es: {hoy}')
    return

def DiaSemana():
    hoy = Now.strftime('%A')
    print(f'El dia de la semana es: {hoy}')

def DiaMes():
    mes = Now.strftime('%d')
    print(f'Hoy es: {mes}')

def NombreDeMes():
    mes = Now.strftime('%B')
    print(f'Nombre del mes actual: {mes}')

def Ano():
    ano = Now.strftime('%Y')
    print(f'Estamos en: {ano}')

def siglo():
    anno = Now.year
    siglo = (anno - 1) // 100 + 1
    print(f'Estamos en el siglo: {siglo}')

def menu():
    while True:
        print('='*60)
        print('-'*60)
        print('1.El dia de hoy   2.Dia de la semana  3.Dia del mes')
        print('-'*60)
        print('4.Mes             5.el año actual     6.El siglo actual')
        print('-'*60)
        print('7.Salir')        
               
        try: n = int(input('\nElige: ')); 
        except: print('Ingrese un numero')

        if n in (range(1,8)):
            if n == 1: 
                print('='*60)
                DiaHoy()
            elif n == 2: 
                print('='*60)
                DiaSemana()
            elif n == 3: 
                print('='*60)
                DiaMes()
            elif n == 4: 
                print('='*60)
                NombreDeMes()
            elif n == 5: 
                print('='*60)
                Ano()
            elif n == 6:
                print('='*60)
                siglo()
            elif n == 7: break 
        else: print('Ingresa un valor valido')

menu()