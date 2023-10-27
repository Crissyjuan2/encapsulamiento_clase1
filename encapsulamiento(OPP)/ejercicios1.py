
class persona:
    def __init__(self, nombre, apellido):
        self.__name = nombre #el _ es un atributo protegida y __ son atributos protegidos
        self.apellido = apellido
    def mostrar_detalle(self):
        print("Persona: ", self.__name, self.apellido)

    def saludo(self):
        return f'Hola soy {self.__name} {self.apellido}'

persona1 = persona('Juan', 'Aviles')
persona1.saludo()
#print(persona1.saludo())
#print(persona1.__name)
#persona1.__name = 'Mary'
#print(f'el nombre se cambio a {persona1.__name}')


class Empleados(persona):
    def __init__(self, nombre, apellido, sueldo):
        super().__init__(nombre, apellido) #esto es para hederar clases ya hechas
        self.sueldo = sueldo
empleado1 = Empleados('Juan', 'Aviles', 100)
print(empleado1.apellido)
print(empleado1.saludo())
print(empleado1.sueldo)

