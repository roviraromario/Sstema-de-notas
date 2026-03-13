salir = "no"
usuarios = []
profesor = []
notas_materias = {}
inicio_sesion = "no"
materias = ["matematicas", "lenguaje", "ciencias", "biologia", "ingles"]

def contrañea_valida(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(char.isupper() for char in contraseña):
        return False
    if not any(char.islower() for char in contraseña):
        return False
    if not any(char.isdigit() for char in contraseña):
        return False
    return True

while salir == "no": 
    opcion = input("- escribe \n1 para crear nueva cuenta \n2 para iniciar sesion\n  respuesta:")
    if opcion == "1":
        print("-----------------------------------------")
        tipo_usuario = input(" escribe \n1 si eres estudiante \n2 si eres profesor\n  respuesta:")
        if tipo_usuario == "1":
            print("-----------------------------------------")
            nombre_usuario = input("escribe tu nombre de usuario: ")
            contraseña = input("escribe tu contraseña: ")
            if not contrañea_valida(contraseña):
                print("-------------------/////-----------------")
                print("contraseña invalida, debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.")
                continue
            usuarios.append([nombre_usuario, contraseña,{}])
            print("-----------------------------------------")
        elif tipo_usuario == "2":
            print("-----------------------------------------")
            nombre_usuario = input("escribe tu nombre de usuario: ")
            contraseña = input("escribe tu contraseña: ")
            if not contrañea_valida(contraseña):
                print("-------------------/////-----------------")
                print("contraseña invalida, debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.")
                continue
            profesor.append([nombre_usuario, contraseña])
        else: 
            print("-----------------------------------------")
            print("usuario invalido")
            
    elif opcion == "2":
        print("-----------------------------------------")
        opcion_inicio_sesion = input("1 si eres estudiante \n2 si eres profesor \n  respuesta:")
        if opcion_inicio_sesion == "1":
                nombre_inicio = input("escribe tu nombre de  usuario: ")
                contraseña_inicio = input("escribe tu contraseña: ")

                for usuario in usuarios:
                    if nombre_inicio and contraseña_inicio in usuario:
                        inicio_sesion = "si"
                        usuario_iniciado = usuarios.index(usuario)
                        print(usuario_iniciado)
                        print("-------------sesion iniciada--------------")
                
                while inicio_sesion == "si":
                    estudiante_=input("escribe: \n1 para ver notas \n2 para ver promedio \n3 para cerrar sesion\n  respuesta:")
                    cuenta = usuarios[usuario_iniciado]
                    notas = cuenta[2]
                    match estudiante_:
                        case "1":
                            print("-----ver notas----")
                            print(f"notas: {notas}")
                        case "2":
                            print("-----ver promedio----")
                            promedio = sum(notas.values()) / len(notas)
                            print(f"promedio: {promedio}")
                        case "3":
                            print("-----sesion cerrada----")
                            inicio_sesion = "no"
                        case _:
                            print("-----respuesta invalida----")

        elif opcion_inicio_sesion == "2":
                nombre_inicio = input("escribe tu nombre de  usuario: ")
                contraseña_inicio = input("escribe tu contraseña: ")

                for profe in profesor:
                    if profe == [nombre_inicio, contraseña_inicio]:
                        inicio_sesion = "si"
                        print("-------------sesion iniciada--------------")
                
                while inicio_sesion == "si":
                    profesor_= input("escribe:\n1 agregar notas a estudiante \n2 cerrar sesion\n  respuesta:")
                    match profesor_:
                        case "1":
                            print("-----agregar notas----")
                            for usuario in usuarios:
                                print(usuario[0])
                            estudiante_poner_nota = input("escribe el nombre del estudiante que quieres ponerle nota: ")
                            for estudiantes in usuarios:
                                if estudiante_poner_nota in estudiantes:
                                    numero_estudiante = usuarios.index(estudiantes)

                            print("-----------------------------------------")
                            print(usuarios[numero_estudiante][0])
                            materia= input("escribe el nombre de la materia")
                            if materia not in materias:
                                print("-----------------------------------------")
                                print("materia invalida")
                                continue
                            nota = float(input("escribe la nota del estudiante"))
                            usuarios[numero_estudiante][2][materia] = nota = nota
                            print(usuarios[numero_estudiante][2])
                        case "2":
                            print("-----cerrar sesion----")
                            inicio_sesion = "no"
                        case _:
                            print("-----respuesta invalida----")
                    

    else:
        print("-----------------------------------------")
        print("usuario invalido")
