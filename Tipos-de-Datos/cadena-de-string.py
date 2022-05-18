#Cadena de String
migrupoFav = 'Ac Dc'+ " " + 'son buenardos'
#Acá realizo una concatenación
print('Este es mi grupo favorito: ' + migrupoFav)

#otra forma
migrupoFav = 'Metallica'
comentario = "Es mi grupo favorito son muy buenos"
print(migrupoFav + " " + comentario)

#otra forma
print("Mi grupo favorito es:", migrupoFav , comentario)

#Aqui estoy utilizando valores numéricos y realizo una suma
numero1 = 1
numero2 = 2
print("Suma:", numero1 + numero2)

#Aca utilizo valores tipo string lo que va hacer esto es una concatenación y no una suma
numero1= "1"
numero2= "2"
print( "Concatenación:", numero1 + numero2)

#otra forma sumar es utilizar el metodo int que pasa los valores string tiene que ser entero 
numero1= "1"
numero2= "2"
print( "Utilizo 'int' para pasar de string a enteros y asi sumar :",int (numero1) + int(numero2))
