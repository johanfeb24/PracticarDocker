# password_service.py

import random #Generamos valores aleatorios
import string #Trae constantes


class PasswordService: 

    def generate_password(self, length: int) -> str:

        # Validar la longitud
        if length <= 0:
            raise ValueError("La longitud debe ser mayor a 0")

        # Definimos caracteres permitidos:
        # - Letras mayúsculas, minusculas, numeros
        characters = string.ascii_letters + string.digits

        # Generamos la contraseña seleccionando caracteres aleatorios
        password = "".join(random.choice(characters) for _ in range(length))

        return password
