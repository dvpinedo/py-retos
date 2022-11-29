class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Aprobado")
        else:
            print("Reprobado")


alumno1=Alumno()
alumno1.inicializar("Sebastian",4)
alumno1.imprimir()
alumno1.mostrar_estado()
