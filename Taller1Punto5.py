#RESPUESTA PUNTO 5 DEL TALLER #1 ARLEX SAAVEDRA COD:230171022

def main():
    stocks = {              #En esta linea estamos declarando un diccionario con la siguiente información
        'IBM': 146.48,      #International Business Machines Corporation y el valor de su cotización
        'MSFT':44.11,       #Microsoft Corporation y el valor de su cotización
        'CSCO':25.54        #Cisco Systems y el valor de su cotización
    }

    #print out all the keys
    for c in stocks:        #En este for lo que se hace es realizar la impresición de cada una de las claves, es decir lo que esta                           #
        print(c)            #antes de los 2 puntos, es decir cada una de las corporaciones

    #print key n values
    for k, v in stocks.items():                         #En este for lo que estamos realizacion es la impresión de completa del diccionario
        print("Code : {0}, Value : {1}".format(k, v))   #Teniendo en cuenta que k es la clave, es decir cada una de las corporaciones
                                                        #v es el valor de cada una de las corporaciones, es decir la cotización
                                                        #se utiliza un formato de impresión donde cada fila representa a la corporacion y su respectivo valor    
if __name__ == '__main__':  #Se verifica si el modulo ha sido importado o no
    main()                  #Se termina la aplicación