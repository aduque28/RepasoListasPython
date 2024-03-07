#Se declaran diccionarios = objetos
clienteUno= {
    "id": 5,
    "nombre":"edifi1",
    "consumo":200
}

clientedos= {
    "id": 58,
    "nombre":"edifi2",
    "consumo":500
}

#Se declaran una lista = arreglo
clientesAsociados=[
    clienteUno,
    clientedos
]



#MI OBJETIVO SERA OBTENER LA INFRORMACION DE LA LISTA
#RECORRER UNA LISTA O ARREGLO 






'''for i in range(2):

    print(clientesAsociados[i]["consumo"])'''

#prgramemos un foreach que es un for
#especializado en recorrer arreglos (listas)

for cliente in clientesAsociados:
    print(cliente["id"],'=>',cliente["consumo"],'KWH')
    print(f"{cliente['id']}=>{cliente['consumo']}KWH")