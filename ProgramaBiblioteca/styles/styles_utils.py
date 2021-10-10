# _*_ coding: utf8 _*_
import os
import sys
import time
import winsound
import styles.shell_colors as c


def beep(frequency=500, duration=100, times=1):
    '''Frecuencia(Hz)(37 - 32767) y duración(ms)'''
    for i in range(times):
        winsound.Beep(frequency, duration)


def delay_print(string, delay=0.00657, sound=False):
    '''Escribe un caracter la vez'''
    if sound:
        beep(times=2)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def waiting_user():
    delay_print(f"\n{c.reverse}Presiona ENTER para continuar{c.end}")
    input()


def successful_operation():
    for f in [300, 600]:
        beep(frequency=f, duration=80)
    print(f"\n{c.cyan}La operacion ah sido exitosa!{c.end}")


def operation_failed(e):
    beep(frequency=440, duration=200)
    print(f"\n{c.bg_red_hi}{c.bold} Error! {c.end} : {e}")


# def wrong_option():
#     beep(frequency=440, duration=200)
#     print(f"\n{c.bg_red_hi}{c.bold} Error! {c.end} Opción incorrecta.\n")


def clean_console():
    return os.system("cls")
    

def reading():
    clean_console()
    print("Listando", end='')
    delay_print("...\n", delay=0.2)
