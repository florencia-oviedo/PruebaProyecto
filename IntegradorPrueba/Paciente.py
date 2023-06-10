from logger_base import log

class Paciente:

    def __init__(self, id_paciente=None,nombre=None,apellido=None,peso=None,altura=None):
        self._id_paciente = id_paciente
        self._nombre = nombre
        self._apellido= apellido
        self._peso = peso
        self._altura =altura
        self.imc= Paciente.calcularIMC(peso,altura)

    def __str__(self):
        return f'''
        Id Paciente: {self._id_paciente}
        Nombre: {self._nombre}, 
        Apellido: {self._apellido}, 
        Peso: {self._peso},
        Altura: {self._altura}
        
        '''

        # getter and setters
    @property
    def id_paciente(self):
        return self._id_paciente

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso= peso

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @classmethod
    def calcularIMC(cls,peso,altura):
        imc=round(peso/(altura*altura),2)
        return imc



if __name__ == '__main__':
    paciente1 = Paciente(1,'flor','ovi',48.5,1.57)
    print(paciente1.imc)