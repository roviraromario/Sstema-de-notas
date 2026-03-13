salir = "no"
usuarios = []
profesor = []
notas_materias = {}
inicio_sesion = "no"
materias = ["matematicas", "lenguaje", "sociales", "biologia", "ingles"]
mejor_promedio = 0
existe = "no"
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
    opcion = input("- escribe \n1 para crear nueva cuenta \n2 para iniciar sesion\n3 salir\n  respuesta:")
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
                        print("-------------sesion iniciada--------------")
                        print(f"Bienvenido: {usuarios[usuario_iniciado][0]}")
                        existe = "si"

                if existe == "no":
                    print("tu cuenta no existe")

                while inicio_sesion == "si":
                    estudiante_=input("escribe: \n1 para ver notas \n2 para ver promedio \n3 para cerrar sesion\n  respuesta: ")
                    cuenta = usuarios[usuario_iniciado]
                    notas = cuenta[2]
                    print(notas)
                    match estudiante_:
                        case "1":
                            print("-----ver notas----")
                            print(f"notas: {notas}\n \n")
                        case "2":
                            print("-----ver promedio----")
                            promedio = sum(notas.values()) / len(notas)
                            cuenta.append([promedio])
                            print(f"promedio: {promedio}\n \n")
                        case "3":
                            print("-----sesion cerrada----\n")
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
                        existe = "si"
                
                if existe == "no":
                    print("tu cuenta no existe")
                while inicio_sesion == "si":
                    profesor_= input("escribe:\n1 agregar notas a estudiante \n2 ver estudiante con mejor promedio \n3 notas del grupo\n4 cerrar sesion\n  respuesta: ")
                    match profesor_:
                        case "1":
                            print("-----agregar notas----")
                            for usuario in usuarios:
                                numero = 1
                                print(f"{numero}:{usuario[0]}:{usuario[2]}")
                                numero += 1
                            estudiante_poner_nota = input("escribe el nombre del estudiante que quieres ponerle nota: ")
                            for estudiantes in usuarios:
                                numero_con_nombre = 0
                                if estudiante_poner_nota in estudiantes:
                                    numero_estudiante = usuarios.index(estudiantes)
                                    numero_con_nombre +=1
                                    print("-----------------------------------------")
                                    materia= input("escribe el nombre de la materia: ")
                                    if materia not in materias:
                                        print("-----------------------------------------")
                                        print("materia invalida")
                                        continue
                                    nota = float(input("escribe la nota del estudiante: "))
                                    usuarios[numero_estudiante][2][materia] = nota
                                    print(usuarios[numero_estudiante][2])
                            if numero_con_nombre == 0:
                                print("---------------  Error  ------------------")
                                print("no existe ningun estudiante con ese nombre")
                                print("------------------------------------------")
                        case "2":
                            for estudiante_promedio in usuarios:
                                cuenta = estudiante_promedio
                                notas = cuenta[2]
                                if notas == None:
                                    print("nadie tiene notas")
                                promedio = sum(notas.values()) / len(notas)
                                if mejor_promedio < promedio:
                                    mejor_promedio = promedio
                                    mejor_cuenta = cuenta[0]

                            print(mejor_cuenta)
                            print(mejor_promedio)
                        case "3":
                            estudiantes = usuarios
                            for estudiante in estudiantes:
                                if estudiante[0] and estudiante [2] != None:
                                    nombre = estudiante[0]
                                    nota = estudiante[2]
                                    print(nombre, nota)

                                print()

                        case "4":
                            print("-----cerrar sesion----\n")
                            inicio_sesion = "no"
                        case _:
                            print("-----respuesta invalida----")
        else:
            print("no existe esta opcion")         
    elif opcion == "3":
        salir = "si"
    else:
        print("-----------------------------------------")
        print("opcion invalida")
        
