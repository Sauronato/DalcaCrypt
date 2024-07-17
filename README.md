# DalcaCrypt: Encriptador y Desencriptador de Texto

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Descripción

`dalcacript.py` es un programa que encripta y desencripta texto usando el algoritmo de cifrado simétrico Fernet. Todo el texto mostrado en el programa está en español.

- **Autor**: David Alcalá Atero
- **Fecha**: 17 de julio de 2024
- **Licencia**: MIT License

## Características

- **Encriptar Texto**: Permite encriptar texto utilizando una clave Fernet.
- **Desencriptar Texto**: Permite desencriptar texto encriptado con una clave Fernet.
- **Interfaz de Usuario en Consola**: Utiliza `curses` para una interfaz de usuario en consola amigable.
- **Copiado al Portapapeles**: El texto encriptado/desencriptado se copia automáticamente al portapapeles.

## Requisitos

- Python 3.11+
- Paquetes de Python:
  - `cryptography`
  - `getpass`
  - `os`
  - `time`
  - `curses`
  - `pyperclip`
  - `tkinter`

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Sauronato/DalcaCrypt.git
   cd DalcaCrypt
   ```

2. Instalar los paquetes necesarios:
    ```bash
    pip install cryptography windows-curses pyperclip
    ```

## Uso
Para ejecutar el programa, simplemente ejecuta el script `dalcacrypt.py`:

  ```bash
    python dalcacrypt.py
  ```
    
## Funcionalidades

### Encriptar un Texto

1. Selecciona la opción `1. Encriptar un texto`.
2. Introduce la clave para encriptar el texto.
3. Introduce el texto que deseas encriptar.
4. El texto encriptado se mostrará y se copiará automáticamente al portapapeles.

### Desencriptar un Texto

1. Selecciona la opción `2. Desencriptar un texto`.
2. Selecciona el archivo `.key` que contiene la clave.
3. Introduce el texto encriptado que deseas desencriptar.
4. El texto desencriptado se mostrará y se copiará automáticamente al portapapeles.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios necesarios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Empuja los cambios a tu rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT.

## Agradecimientos

Gracias por utilizar este programa. Si tienes alguna sugerencia o encuentras algún problema, no dudes en abrir un issue en el repositorio.
