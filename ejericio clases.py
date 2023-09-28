fecha=input(" ingrese la fecha actual en formato día, DD/MM: ").lower()#pedidos que ingrese la fecha y con .lower lo transformamos todo en minúsculas

dia_semana=fecha[0: fecha.find(",")] #sacamos el dia de la semana
dia=int(fecha[fecha.find(" ")+1:fecha.find("/")])#sacamos la fecha osea el dia en numero del mes

mes=int(fecha[fecha.find("/")+1:]) #sacamos el mes
dias_semana=("lunes","martes","miercoles","jueves","viernes")#hacemos una cadena con los dias de semana
meses=(1,2,3,4,5,6,7,8,9,10,11,12)#hacemos una cadema con los meses en numeros

#aca validados si la variable dia_semana esta dentro de la cadena dias_semana
#validamos que dia no sea mayor a 0 y menor a 31
#validamos qie mes entre dentro de la cadena meses
if dia_semana in dias_semana and dia<=31 and dia>0 and mes in meses: 
   
    if dia_semana=="lunes" or dia_semana=="martes" or dia_semana=="miercoles": #verificamos que el dia que selecciono fue lunes , martes o miercoles 
        examen=input("¿ese dia hubo examenes? Responde con si o no: ").lower() #en caso de que asi sea pregunta al usuario si hubo examen eso dia
        if examen=="si": #si hubo examen se ejecuta este if
            aprobados=int(input("ingrese cuantos alumnos aprobaron: ")) #pregunta cuantos alumnos aprobaron
            desaprobados=int(input("ingrese cuantos alumnos desaprobaron: ")) #pregunta cuantos alumnos desaprobaron
            alumnos_totales=aprobados+desaprobados #primero sacomos el total de alumnos sumando la gente que aprobó y desaprobó
            promedio=aprobados*100/alumnos_totales #aca calculamos el promedio que multiplicamos por 100 los aprobados dividio el total de alumnos
            print("El promedio de los alumnos aprobados es del %",promedio) #aca mostramos el promedio
        else: #en caso de que no haya examen ese dia se ejecuta el else
            print("Fin del programa") #imprimimos  un mensaje que dice fin del programa
    elif dia_semana=="jueves": #en caso de que sea jueves el dia se ejecuta este elif
        asis=int(input("inrese el pocentaje de asistencia: ")) #le pedimos al usuario que ingrese el porcentaje de asistencia que hubo
        if asis>=50: #si fue mas o igual al %50 se ejecuta  este if
            print("Asistió la mayoria") #se imprime Asistió la mayoria
        else: #en caso de que no haya sido menos del %50 se ejecuta este else
            print("No asistio la mayoria") # E imprimi No asistio la mayoria
    else: #En caso de que no sea ni lunes , ni martes , miercoles , ni jueves se ejecuta este else , que por descarte seria el viernes
        if dia==1 and mes==1 or mes==7: #validamos si es el primero de el Enero o el primer mes de Julio
            print("Comienzo de nuevo ciclo") #Imprimimos Comienzo de nuevo ciclo
            alum=int(input("Ingrese la cantidad de alumnos que inician el nuevo ciclo: ")) #Aca pide que ingrese la camtidad de alumnos que inician el nuevo ciclo  
            precio=int(input("Ingrese la cantidad de dinero que pagaron: ")) #Pide que ingrese el precio que pago cada alumno nuevo que ingreso
            print("El ingreso total fue de: ", alum*precio) #muestra la ganancia total que hubo 
        else: #en caso que no sea el primero de Enero , Julio
            print("Ya ha empezado un nuevo ciclo") 
            
else:
    print("Se produjo un error") # En caso que ingrese una fecha invalida se muetra este mensaje y no corre el programa