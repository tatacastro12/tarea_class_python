class Alumno:
    def inicio(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("nombre", self.nombre)
        print("nota", self.nota)

    def resultado(self):
        if self.nota < 5:
            print("no fue aprobado por el alumno")
        else:
            print("el alumno ha aprobado")

alumno1 = Alumno ()
alumno2 = Alumno ()

alumno1.inicio("juan", 8)
alumno2.inicio("tata", 4)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
        