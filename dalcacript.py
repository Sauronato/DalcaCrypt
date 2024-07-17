
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dalcacript.py - Wednesday, July 17 2024
# Author: David Alcalá Atero
# License: MIT License
# Description EN: Encrypts and decrypts text using the Fernet symmetric encryption
# algorithm. All the text showed in the program is in Spanish.
# Description ES: Encripta y desencripta texto usando el algoritmo de cifrado simétrico Fernet. Todo el texto mostrado en el programa está en español.
# Dependencies: cryptography, os, time, curses, pyperclip, tkinter
# Version: 1.0


from cryptography.fernet import Fernet
from os import system
from time import sleep
import time
import curses
import pyperclip
import tkinter as tk
from tkinter import filedialog

def main():
    try:
        curses.wrapper(mostrar_menu)
    except KeyboardInterrupt:
        exit()
    


def init_colors():
    global color_texto
    global color_error
    global color_correcto
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        color_texto = curses.color_pair(1)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        color_error = curses.color_pair(2)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        color_correcto = curses.color_pair(3)

    else:
        color_texto = curses.A_NORMAL
        color_error = curses.A_NORMAL
        color_correcto = curses.A_NORMAL


def encrypt(stdscr):
    # Limpiar pantalla y configurar la interfaz de usuario
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(1)  # Mostrar cursor
    stdscr.nodelay(0)   # Modo no delay para esperar la entrada del usuario

    # Configuración del menú
    opciones = [
        "1. Crear nueva KEY",
        "2. Utilizar KEY ya existente",
    ]

    # Mostrar el menú
    stdscr.addstr(1, 2, "Selecciona una opción:", curses.A_BOLD)

    fila_actual = 2
    for opcion in opciones:
        stdscr.addstr(fila_actual, 4, opcion,color_texto)
        fila_actual += 1

    stdscr.refresh()

    # Lógica para seleccionar y ejecutar la opción elegida
    while True:
        # Esperar la entrada del usuario
        key = stdscr.getch()

        if key == ord('1'):
            create_key(stdscr)
        elif key == ord('2'):
            stdscr.clear()
            stdscr.addstr(2, 1, "Seleccione el fichero clave", curses.A_BOLD)
            key_file = seleccionar_archivo()
            if key_file and key_file.endswith(".key"):
                stdscr.addstr(4, 1, "Fichero clave seleccionado correctamente", color_correcto)
                stdscr.refresh()
                curses.napms(2000)
                try:
                    key = load_key(key_file)
                except:
                    stdscr.clear()
                    stdscr.addstr(
                        1, 2, "Error al cargar el fichero clave", color_error)
                    stdscr.refresh()
                    curses.napms(2000)
                    encrypt(stdscr)
                use_key_encript(stdscr, key)
            else:
                stdscr.clear()
                stdscr.addstr(1, 1, "No se ha seleccionado ningún fichero valido", color_error)
                stdscr.refresh()
                curses.napms(2000)
                mostrar_menu(stdscr)
            stdscr.refresh()
            curses.napms(2000) # POR AQUI 
            stdscr.clear()
        else:
            stdscr.addstr(
                fila_actual + 2, 2, "Opción no válida. Introduce 1 o 2.", color_error)
            stdscr.refresh()
        break


    # Solicitar la clave de manera segura usando getpass
  #  curses.echo(False)  # Deshabilitar la escritura en pantalla
    stdscr.addstr(4, 2, "Clave: ")
    stdscr.refresh()
    # Capturar la entrada del usuario en la posición (4, 9)
    clave = stdscr.getstr(4, 9, 20)
  #  curses.echo(True)  # Habilitar la escritura en pantalla nuevamente
    stdscr.addstr(4, 2, "Clave introducida correctamente", color_correcto)
    stdscr.refresh()

    # Convertir clave a string
    clave = clave.decode('utf-8')

    # Encriptar el texto
    f = Fernet(clave.encode())
    texto_encriptado = f.encrypt(clave.encode())

    # Mostrar el texto encriptado
    stdscr.addstr(8, 2, "Texto encriptado:", curses.A_NORMAL)
    stdscr.addstr(10, 2, texto_encriptado.decode(), color_texto)
    stdscr.refresh()

    # Esperar 300 segundos antes de volver al menú
    sleep(300)
    mostrar_menu(stdscr)


def create_key(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(1)  # Mostrar cursor
    stdscr.nodelay(0)   # Modo no delay para esperar la entrada del usuario
    stdscr.addstr(1, 1, "Introduzca el nuevo nombre del fichero (Recuerda EJEMPLO.key): ")
    stdscr.refresh()
    curses.echo(True)
    # Capturar la entrada del usuario en la posición (4, 9)
    clave = stdscr.getstr(2,1,20)
    stdscr.clear()
    clave_str = clave.decode('utf-8')  # Convertir bytes a str
    try:
        key = generate_key(clave)
    except:
        stdscr.clear()
        stdscr.addstr(1, 1, "Error al crear el fichero " +
                      clave_str, color_error)
        stdscr.refresh()
        curses.napms(1000)
        return
    stdscr.clear()
    stdscr.addstr(1, 1,"Fichero "+clave_str+" creado correctamente", color_correcto)
    stdscr.refresh()
    curses.napms(1000) 
    use_key_encript(stdscr, key) 

def generate_key(key_name):
    # Generar una nueva clave
    key = Fernet.generate_key()
    with open(key_name, "wb") as key_file:
        key_file.write(key)
    return key    

def load_key(key_name):
    # Cargar una clave existente
    with open(key_name, "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_text(text, key):
    # Encriptar el texto
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text

def use_key_encript(stdscr, key):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(1)  # Mostrar cursor
    stdscr.nodelay(0)   # Modo no delay para esperar la entrada del usuario
    stdscr.addstr(1, 1, "Introduzca el texto a encriptar: ", curses.A_BOLD)
    stdscr.refresh()
    curses.echo(True)
    original_text = stdscr.getstr(2,1)
    stdscr.clear()
    original_text_str = original_text.decode('utf-8')
    curses.curs_set(0)
    encrypted_text = encrypt_text(original_text_str, key)
    stdscr.addstr(1, 1, "Texto original: ", curses.A_BOLD)
    stdscr.addstr(2, 1, original_text_str)
    stdscr.addstr(4, 1, "Texto encriptado: ", curses.A_BOLD)
    stdscr.addstr(5, 1, encrypted_text.decode())
    pyperclip.copy(encrypted_text.decode())
    stdscr.addstr(7, 1, "Texto copiado al portapapeles", color_correcto)
    stdscr.addstr(9, 1, "Puede cerrar el programa utilizando CTRL+C", color_correcto)
    stdscr.refresh()
    cuenta_atras(300, stdscr)
    mostrar_menu(stdscr)

def use_key_decript(stdscr, key):
        stdscr.clear()
        stdscr.refresh()
        curses.curs_set(1)  # Mostrar cursor
        stdscr.nodelay(0)   # Modo no delay para esperar la entrada del usuario
        stdscr.addstr(1, 1, "Introduzca el texto clave: ", curses.A_BOLD)
        stdscr.refresh()
        curses.echo(True)
        original_text = stdscr.getstr(2,1)
        stdscr.clear()
        original_text_str = original_text.decode('utf-8')
        curses.curs_set(0)
        encrypted_text = decrypt_text(original_text, key)
        stdscr.addstr(1, 1, "Texto encriptado: ", curses.A_BOLD)
        stdscr.addstr(2, 1, original_text_str)
        stdscr.addstr(4, 1, "Texto desencriptado: ", curses.A_BOLD)
        stdscr.addstr(5, 1, encrypted_text.decode())
        pyperclip.copy(encrypted_text.decode())
        stdscr.addstr(7, 1, "Texto copiado al portapapeles", color_correcto)
        stdscr.addstr(9, 1, "Puede cerrar el programa utilizando CTRL+C", color_correcto)
        stdscr.refresh()
        cuenta_atras(300, stdscr)
        mostrar_menu(stdscr)


def cuenta_atras(segundos, stdscr):
    for i in range(segundos, 0, -1):
        stdscr.addstr(8, 1, "El programa se terminará en: "+str(i), color_error)
        stdscr.refresh()
        time.sleep(1)


def decrypt(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(1)
    stdscr.nodelay(0)
    stdscr.addstr(1, 2, "Seleccione el fichero clave", curses.A_BOLD)
    stdscr.refresh()
    key_name = seleccionar_archivo()
    if key_name and key_name.endswith(".key"):
        try:
            key = load_key(key_name)
        except:
            stdscr.clear()
            stdscr.addstr(1, 2, "Error al cargar el fichero clave", color_error)
            stdscr.refresh()
            curses.napms(2000)
            decrypt(stdscr)
        use_key_decript(stdscr, key)
    else:
        stdscr.clear()
        stdscr.addstr(1, 2, "No se ha seleccionado ningún fichero valido", color_error)
        stdscr.refresh()
        curses.napms(2000)
        mostrar_menu(stdscr)

def decrypt_text(text, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(text)
    return decrypted_text



def seleccionar_archivo():
    # Crear la ventana principal de tkinter (puedes ocultarla si prefieres)
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Mostrar el diálogo para seleccionar un archivo
    archivo = filedialog.askopenfilename()

    # Mostrar el archivo seleccionado
    if archivo:
        return archivo
    else:
        return None


def mostrar_menu(stdscr):
    # Limpiar pantalla y configurar la interfaz de usuario
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)  # Ocultar cursor
    stdscr.nodelay(0)   # Modo no delay para esperar la entrada del usuario

    init_colors()

    # Configuración del menú
    opciones = [
        "1. Encriptar un texto",
        "2. Desencriptar un texto",
        "3. Salir del programa"
    ]

    # Mostrar el menú
    stdscr.addstr(1, 2, "Bienvenido al encriptador/desencriptador de textos", curses.A_BOLD)
    stdscr.addstr(2, 2, "Selecciona una opción:", curses.A_NORMAL)

    fila_actual = 3
    for opcion in opciones:
        stdscr.addstr(fila_actual, 4, opcion, color_texto)
        fila_actual += 1

    stdscr.refresh()

    # Lógica para seleccionar y ejecutar la opción elegida
    while True:
        # Esperar la entrada del usuario
        key = stdscr.getch()

        if key == ord('1'):
            stdscr.clear()
            stdscr.addstr(2, 2, "Comenzando el proceso de encriptación", curses.A_BOLD)
            stdscr.refresh()
            encrypt(stdscr)


        elif key == ord('2'):
            stdscr.clear()
            stdscr.addstr(2, 2, "Comenzando el proceso de desencriptación", curses.A_BOLD)
            stdscr.refresh()
            decrypt(stdscr)
        elif key == ord('3'):
            stdscr.clear()
            stdscr.addstr(2, 2, "Saliendo del programa...", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(2000)  # Esperar 2 segundos antes de salir
            break
        else:
            stdscr.addstr(
                fila_actual + 2, 2, "Opción no válida. Introduce 1, 2 o 3.", curses.color_pair(2))
            stdscr.refresh()

    curses.endwin()




# key is generated
#key = Fernet.generate_key()

# value of key is assigned to a variable
#f = Fernet(key)

# the plaintext is converted to ciphertext
#token = f.encrypt(b"welcome to geeksforgeeks")

# display the ciphertext
#print(token)

# decrypting the ciphertext
#d = f.decrypt(token)

# display the plaintext and the decode() method
# converts it from byte to string
#print(d.decode())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
    exit()
