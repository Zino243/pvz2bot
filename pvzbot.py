import pyautogui
import time
from os import system

VERSION = "v1.0"

scwith, scheight = pyautogui.size()

def provedisplay():
    if scwith == 1920 and scheight == 1080:
        return True
    else:
        return True
def clicker(vueltas):
    for h in range(vueltas):
        pyautogui.click()
        time.sleep(0.05)
def cleaner(t):
    if t:
        time.sleep(1)
        system("cls")
        system("echo Programa bot pvz2 {}".format(VERSION))
        system("echo ------------------------------------------------")
    else:
        system("cls")
        system("echo Programa bot pvz2 {}".format(VERSION))
        system("echo ------------------------------------------------")

if   provedisplay():
    cleaner(True)
    print("pon el raton en la posicion del boton 1")
    time.sleep(5)
    mousew1, mouseh1 = pyautogui.position()
    print("posicion obtenida")
    cleaner(True)
    print("pon el raton en la posicion del boton 2")
    time.sleep(5)
    mousew2, mouseh2 = pyautogui.position()
    print("posicion obtenida")
    cleaner(True)
    print("necesitas un lugar donde se pueda hacer spamclick sin darle a nada y dentro de la pantalla de juego, elige una")
    time.sleep(5)
    mousew3, mouseh3 = pyautogui.position()
    print("posicion obtenida")
    cleaner(True)
    count = int(input("¿cuantas piñatas quieres abrir? -> "))
    print("tienes unos segundos para preparar el juego, date prisa")
    time.sleep(5)
    for i in range(count):
        cleaner(False)
        print("vas por la piñata: {}".format(i + 1))
        pyautogui.moveTo(mousew1, mouseh1)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.moveTo(mousew2, mouseh2)
        time.sleep(0.2)
        pyautogui.click()
        pyautogui.moveTo(mousew3, mouseh3)
        clicker(65)
        time.sleep(0.2)

system("cls")
pyautogui.alert("El bot a terminado con su trabajo!", button="cerrar", title="bot para pvz2")