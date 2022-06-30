# Instalacion de Python
'''
Python se puede descargar de www.python.org y, al instalarlo, hay que tratar
de recordar de activar la opcion "Install PATH variables". En caso de no
hacerlo, hay que agregar las rutas a la carpeta de python y python\Scripts
en el PATH de las variables de entorno (Windows).

En el caso de MacOS, hay que instalar tambien la ultima version de Python
ya que MacOS trae por defecto la version 2 de Python (y no se puede
desinstalar), por lo que hay que convivir con ambas versiones. En MacOS,
para ejecutar Python 3, hay que llamarlo con el numero de version mayor. Ej:
python3 y algun comando a ejecutar

Una vez instalado y configurado, se puede comprobar que funciona correctamente
abriendo una terminal de comando (Windows > Command Prompt) y escribiendo:
python --version (o python3 --version en MacOS). Si nos dice cual es la
version de Python que se esta ejecutando (y es la correcta), entonces
no tendremos problema.
'''

# Entorno de VSCode
'''
En caso de querer utilizar Visual Studio Code para escribir y probar nuestras
aplicaciones en Python, debemos asegurarnos que trabaje de manera correcta
con Python. Para ello creamos un archivo con la extension .py en cualquier
lado, creamos una funcion rapida en Python, guardamos los cambios y esperamos
unos segundos. Nos debera aparecer en la barra inferior, del lado derecho,
la version correcta de Python. Por ejemplo podemos escribir algo rapido como:
print('Hola Mundo')

En caso de que no nos aparezca la version correcta, podemos hacer click sobre
la version que nos aparezca y seleccionar la adecuada. Tambien podemos
ingresar Ctrl + Shift + P y escribir "python" y seleccionar la opcion
"Python: Select interpreter"
'''

# Extensiones
'''
Para trabajar con cualquier lenguaje en VSCode es importante que instalemos
al menos la extension de ese lenguaje para VSCode. En el caso de Python, la
extension se llama simplemente "Python" y fue publicada por Microsoft.
Actualmente tiene casi 60 millones de usuarios.

Ademas se pueden instalar diferentes extensiones que nos ayudan a obtener
diferentes resultados. Aca hay un listado de mis favoritas:

Pylance (Microsoft)
Path Intellisense (Christian Kohler)
IntelliCode (Microsoft)
Git Graph (mhutchie)
Code Runner (Jun Han)
'''

# Tema
'''
Es importante que nos guste y nos sintamos comodos con lo que estamos viendo,
especialmente si nos dedicamos a esto. Debido a la gran cantidad de horas que
un programador pasa mirando un monitor, se hace casi una necesidad el tener
un tema obscuro en nuestro editor. En VSCode se puede cambiar el tema que
vemos presionando Ctrl + Shift + P y escribiendo "Color Theme".
'''
