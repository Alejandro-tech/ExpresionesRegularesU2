import re

txt = """ El Universo es el espacio y el tiempo que abarca todo aquello que existe, es decir, todos los tipos de materias, los planetas, la energía, la luz, las estrellas, los satélites, las galaxias y otros objetos celestes, incluso, las leyes y las constantes físicas que los gobiernan. Por ello, el Universo es difícil de explicar o medir.
El conocimiento científico actual ha determinado que el tamaño del Universo es muy grande Mdiendo, lo que dificulta su cálculo a las 12:23 am, ya que no se sabe con certeza cuáles son sus límites, y esa misma grandeza hace que sea considerado como infinito.
Asimismo, algunos investigadores científicos defienden que existen varias dimensiones que “forman universos coexistentes e interpenetrantes”, que no se mezclan. En diferentes códigos postales 77300, 71200, 19192, 88122, 09221, 82122, 88221. 
Edad de Piedra. Msxico Primer periodo de la Prehistoria durante el cual, los seres humanos fabricaron herramientas de piedra, siendo la tecnología más avanzada en ese entonces. La madera, los huesos y otros materiales también fueron utilizados (cuernos, cestos, cuerdas, etc), pero la piedra (en particular, varias rocas de ruptura concoidea, es decir, con puntas cortantes, como la silex, el cuarzo, cuarcita, obsidiana, etc) fue utilizada para fabricar herramientas y armas, de corte o percusión. La Prehistoria se divide en Edad de Piedra y Edad de los Metales, luego de esos periodos se inicia la Historia propiamente dicha, es decir, se utiliza la escritura para describir los hechos al número 982 172 80 93, 123 129 82 65, 203 120 02 12, 984 185 22 45, 283 192 66 43.
Sin embargo, esta es la condición necesaria a las 10:23 pm, pero no suficiente para definir este periodo "Edad de Piedra", ya que en el tuvieron lugar fenómenos fundamentales para el ser humano, en cuanto adquisiciones tecnológicas (fuego, instrumentos, vivienda, ropa, etc), la evolución social, los cambios climáticos, la revolución económica desde un sistema cazador-recolector a las 07:56 am, hasta un sistema parcialmente productor, la diáspora del ser humano por todo el mundo habitable, desde la "Cuna de la humanidad" el continente Africano, entre otros acontecimientos al correo alejandro@gmail.com , sony@gmail.com , buenavista@gmail.com , vilca@gmail.com , alone@gmail.com .
Lo primero que debes saber es qué significa IP: son las iniciales de Internet Protocol, que traducido al español lo podemos llamar como Protocolo de Internet a las 09:23 pm. En otras palabras, es el sistema estándar mediante el cual funciona la internet, por medio de un proceso de envío y recepción de información. Unos ejemplos son 192.168.12.15, 192.168.00.12, 192.168.122.242, 192.168.23.22. En diferentes urls como https://whatsapp.com , https://facebook.com , https://amazon.com , https://mercadolibre.com """

print("Elija la opción que desee ejecutar")
print("1. Todas las palabras que tengan una longitud de 7 o más letras\n" 
"2.	Expresiones que NO finalicen con una vocal\n"
"3.	Las palabras que inicien con “M” donde la segunda letra no sea voca\n"
"4.	Expresiones encerradas entre comillas\n"
"5.	Ip’s\n"
"6.	Horas\n"
"7.	Telefonos\n"
"8.	Correos electrónicos\n"
"9.	Url´s\n"
"10. Código postal\n")
opcion = int( input ("Ingresa la opción que desea ejecutar"))

print("-----------------------------------------------------------------------")
print("1.	Todas las palabras que tengan una longitud de 7 o más letras")
x = r"[A-Za-záéíóú]{7,}"
resultax = re.findall(x,txt)
for resultadosx in resultax:
    print(resultadosx)


print("-----------------------------------------------------------------------")
print("2.	Expresiones que NO finalicen con una vocal.")
y = r"[A-Za-záéíóú]+[^aeiou\s/W]\b"
resultay = re.findall(y,txt)
for resultadosy in resultay:
    print(resultadosy) 


print("-----------------------------------------------------------------------")
print("3.	Las palabras que inicien con “M” donde la segunda letra no sea vocal")
z = r"[M][^aeiouáéíóú]\w+"
resultaz = re.findall(z,txt)
for resultadosz in resultaz:
    print(resultadosz)


print("-----------------------------------------------------------------------")
print("4.	Expresiones encerradas entre comillas")
a = r"(\"[\w\s]+\")"
resultaa = re.findall(a,txt)
for resultadosa in resultaa:
    print(resultadosa)


print("-----------------------------------------------------------------------")
print("5.	Ip’s")
b = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
resultab = re.findall(b,txt)
for resultadosb in resultab:
    print(resultadosb)


print("-----------------------------------------------------------------------")
print("6.	Horas")
c = r"[0-9]{1,2}\:[0-9]{1,2}\s[a|p][m]"
resultac = re.findall(c,txt)
for resultadosc in resultac:
    print(resultadosc)


print("-----------------------------------------------------------------------")
print("7.	Telefonos")
d = r"[0-9]{1,3}\s[0-9]{1,3}\s[0-9]{1,4}"
resultad = re.findall(d,txt)
for resultadosd in resultad:
    print(resultadosd)


print("-----------------------------------------------------------------------")
print("8.	Correos electrónicos")
e = r"\w+[\@]+\w+[.]+\w+"
resultae = re.findall(e,txt)
for resultadose in resultae:
    print(resultadose)


print("-----------------------------------------------------------------------")
print("9.	Url´s")
f = r"https://+\w+[.]\w+"
resultaf = re.findall(f,txt)
for resultadosf in resultaf:
    print(resultadosf)


print("-----------------------------------------------------------------------")
print("10.	Código postal de Quintana Roo")
g = r"\b[7][7]\d{3}"
resultag = re.findall(g,txt)
for resultadosg in resultag:
    print(resultadosg)
