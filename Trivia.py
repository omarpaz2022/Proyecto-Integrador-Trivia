import csv


def preguntar(pregunta):    #funcion para mostrar una pregunta
    print(pregunta)

def opciones():         #funcion que muestra las opciones de la pregunta realizada y devuelve las respuestas de ambos jugadores
    respuestas=[]       #lista que va a contener las respuestas del j1 y j2 de una pregunta.
    opcion=1
    while opcion<5:     #mustro las opciones
        print(f"{opcion} - {lista[opcion]}")
        opcion = opcion + 1
    respuestas.append(int(input(f"Jugador {j1[0]} elija una opcion: ")))    #agrego la respuesta del j1 a la lista de respuestas
    respuestas.append(int(input(f"Jugador {j2[0]} elija una opcion: ")))    #idem pero para j2
    return respuestas       #retorno la lista que contiene la respuesta de ambos jugadores

def evalua(respuesta):      #funcion que evalua si la respuesta fue correcta o no y retornando los puntos correspondientes
    correcta=int(lista[5])      #guardo la respuesta correcta en la variable "correcta"
    if respuesta == correcta:   #controlo si la respuesta es correcta o no
        print("Respuesta correcta. Ganó 30 puntos.")
        return 30           #retorno 30 pts ya que la respuesta fue correcta
    else:
        print("Respuesta incorrecta. No ganó ningún punto.")
        return 0            #retorno 0 pts ya que la respuesta fue incorrecta


def jugar():        #funcion que comienza una ronda (una pregunta)
    preguntar(lista[0])     #Llamo a la funcion "preguntar" y le paso la pregunta
    respuestas=opciones()   #llamo a la funcion "opciones" y guardo el retorno en una lista "respuestas"
    print("\n------Resultado de la ronda------")

    #       datos del jugador 1 en la ronda
    print(f"Jugador {j1[0]}:")      #muestro el nombre del jugador 1
    puntos=evalua(respuestas[0])    #llamo a la funcion "evalua" y le paso la respuesta del j1, el retorno lo guardo en la variable "puntos"
    if not puntos==0:               #controlo si la variable "puntos" es distinta de 0, si lo es, sumo los puntos y aumento la cantidad de respuestas correctas del j1
        j1[1] = str(int(j1[1]) + puntos)    #sumo los puntos obtenidos
        j1[2] = str(int(j1[2]) + 1)         #aumento la cantidad de preguntas respondidas correctamente

    #       datos del jugador 2 en la ronda     idem que j1
    print(f"Jugador {j2[0]}:")
    puntos=evalua(respuestas[1])
    if not puntos==0:
        j2[1] = str(int(j2[1]) + puntos)
        j2[2] = str(int(j2[2]) + 1)

 
        


"""               MAIN              """

if __name__ == '__main__':

    fileName='preguntas.csv'  
    archivoPreguntas = open(fileName, 'r')
    reader = csv.reader(archivoPreguntas, delimiter=',')

    j1=["nombre","0","0"]   #defino una lista "j1" para el jugador 1, la cual contiene su nombre, su puntaje y la cantidad de preguntas que respondio correctamente
    j2=["nombre","0","0"]   #idem que j1 pero para el jugador 2

    j1[0]=(input("Ingrese nombre del Jugador 1: ")) #Ingreso del nombre del jugador 1
    j2[0]=(input("Ingrese nombre del Jugador 2: ")) #Ingreso del nombre del jugador 2


    titulos=0   #variable para controlar si la fila es la de los titulos
    for fila in reader:
        if(titulos == 0):   #verifico si la fila es la de titulos, si lo es, indico que ya fue leida cambiando el valor de la variable "titulos"
            titulos=1
        else:               #si la variable "titulos" ya fue leida, las siguientes lineas son las preguntas
            print("---------------------------------------------------------")
            lista=fila      #guardo la fila leida en una lista
            jugar()         #llamo a la funcion "jugar" para empezar una ronda con la linea leida


    print("\n\n***************FIN DEL JUEGO***************")
    print(f"Jugador {j1[0]}: {j1[2]} respuestas correctas.")        #muestro el nombre del j1 y la cantidad de preguntas respondidas correctamente
    print(f"Jugador {j2[0]}: {j2[2]} respuestas correctas.")        #idem pero para j2
    print("***********************************************")
    guardar = ""        #creo una variable para guardar al ganador
    #       muestro al ganador y sus puntos seguido del perdedor y sus puntos, en caso de empate se muestra el mensaje "Empate."
    if int(j1[1]) > int(j2[1]):     #comparo si el puntaje total del j1 es mayor al puntaje total del j2 para ver quien es el ganador, en caso de empate no se guardará ninguno en el historial
        print(f"{j1[0]} es el ganador con {j1[1]} puntos.")
        print(f"{j2[0]} obtuvo {j2[1]} puntos.")
        guardar = f"{j1[0]},{j1[1]}"    
    elif int(j1[1]) < int(j2[1]): 
        print(f"{j2[0]} es el ganador con {j2[1]} puntos.")
        print(f"{j1[0]} obtuvo {j1[1]} puntos.")
        guardar = f"{j2[0]},{j2[1]}"      
    else:
        print("Empate.")

    lineas=[]    #declaro una lista que va a contener la linea a escribir en el csv
    titulos = ["Jugador","puntaje"]     #creo la variable titulos que va a contener las etiquetas de cada columna del csv
    lineas.append(guardar)       #agrego a la lista "lineas" la linea a guardar
    if not guardar=="":         #controlo que la variable "guardar" no este vacia, si no lo está, quiere decir que hubo un ganador y debe ser guardado
        archivoGanadores = 'ganadores.csv'
        with open(archivoGanadores, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(titulos)
            writer.writerow(lineas)
        file.close()
    archivoPreguntas.close()




