class MeEncantaEstaMateria():
    def _init_(self):
        self.nombre = "Julio"
        self.nombre2 = "Cesar"
        self.apellido = "Caicedo"
        self.mensaje = "Holi profe :3 oxox"
        
    def imprimir(self):
        print(self.mensaje, self.nombre, self.nombre2, self.apellido)
        
#main
objeto = MeEncantaEstaMateria()
objeto.imprimir()