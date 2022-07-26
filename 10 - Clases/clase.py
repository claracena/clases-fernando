# class AnimalesMamiferos:
#     tipo_de_pelo = 'largo'
    
#     def __init__(self, especie, color, altura, peso):
#         self.esp = especie
#         self.col = color
#         self.alt = altura
#         self.pes = peso

#     def especies(self):
#         print(self.esp, self.col, self.tipo_de_pelo)

#     def calc_edad(self):
#         edad = (self.alt * self.pes) / 8000
#         print(edad)

# pepe = AnimalesMamiferos('Equino', 'Marron', 200, 400)
# miguelito = AnimalesMamiferos('Perro', 'Blanco', 30, 70)

# pepe.especies()
# pepe.calc_edad()

# miguelito.especies()
# miguelito.calc_edad()

# -----------------------------------

# class Impresion3D:
#     # Atributos
#     temperatura = 100
#     velocidad = 20
#     distancia = 3

#     # Metodos
#     def __init__(self, material):
#         self.material = material

#     def imprimir(self, color, forma):
#         instrucciones = [
#             self.temperatura,
#             self.velocidad,
#             self.distancia,
#             self.material,
#             color,
#             forma
#         ]
#         print(instrucciones)

# funda = Impresion3D('pvc')
# funda.imprimir(color='Azul', forma='rectangular')
# funda.imprimir(color='Roja', forma='cuadrada')
# pisapapeles = Impresion3D('metal')
# pisapapeles.imprimir(color='natural', forma='rombo')

# -----------------------------------

class Online:
    ip_add = '194.368.234.2'

class Shooter:
    speed = 10
    agility = 9

class Player(Shooter, Online):
    raza = 'Humano'

    def __init__(self, id, name, tickets):
        self.id = id
        self.name = name
        self.tickets = tickets

    def player_info(self):
        return f'ID: {self.id} - Name: {self.name} - Current Tickets: {self.tickets} - Raza: {self.raza} - Speed: {self.speed}'

    def tickets_update(self, tkt_change):
        self.tickets = self.tickets + tkt_change
        return self.tickets

player_1 = Player(328, 'Fernando', 1000)
print(player_1.player_info())

player_2 = Player(124, 'Marcela', 400)
print(player_2.player_info())

player_3 = Player(23, 'Jose', 300)
player_3.raza = 'AI'
print(player_3.player_info())

print('----------------------------------')

player_1.tickets_update(-20)
print(player_1.player_info())
print(player_2.player_info())
player_3.tickets_update(50)
print(player_3.player_info())
