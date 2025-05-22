# -*- coding: utf-8 -*-
import PooLib042
class Usuario_Premium(PooLib042.Usuario):
    def __init__(self, id, alias, nombre, apellidos,sorteos,puntos):
        super().__init__(id, alias, nombre, apellidos)
        self.sorteos=sorteos
        self.puntos=puntos
        
    def muestra_datos(self):
        super().muestra_datos()
        print(f'Tienes derecho a participar en {self.sorteos} sorteos')
        print(f'Tienes {self.puntos} puntos para canjear en premios')

#Creraremos la instancia de un objeto de la clase UsuariosPremium
id=input('Introduce el id del usuario: ')
alias=input('Introduce el Alias del usuario: ')
nombre=input('Introduce el Nombre del usuario: ')
apellidos=input('Introduce el Apellidos del usuario: ')
sorteo=20
puntos=700
UserPremium=Usuario_Premium(id, alias, nombre, apellidos, sorteo, puntos)
UserPremium.muestra_datos()
