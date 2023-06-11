from Paciente import Paciente
from Conexion import Conexion
from logger_base import log

class PacienteDAO:

    _SELECCIONAR = "SELECT * FROM paciente ORDER BY id_paciente"
    _INSERTAR = "INSERT INTO paciente(nombre, apellido,peso,altura,imc) " \
                "VALUES (%s,%s,%s,%s,%s)  RETURNING id_paciente"
    _ACTUALIZAR = "UPDATE paciente SET nombre= %s , apellido=%s , peso=%s, altura=%s WHERE id_paciente=%s  RETURNING id_paciente"
    _ELIMINAR = "DELETE FROM paciente WHERE id_paciente=%s"

    _SELECCIONAR_PACIENTE = "SELECT * FROM paciente WHERE id_paciente=%s"

    # Definimos los metodos de clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                pacientes = []  # creamos una lista
                for registro in registros:
                    id_paciente = registro[0] #id del paciente
                    paciente = Paciente( registro[1], registro[2],
                               registro[3],registro[4])  # nombre,apellido,peso,altura
                    paciente.id_paciente(id_paciente)
                    pacientes.append(paciente)
                return pacientes


    #Buscar un paciente por id
    @classmethod
    def seleccionarPaciente(cls,id_paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores=(id_paciente,)
                cursor.execute(cls._SELECCIONAR_PACIENTE,valores)
                registro = cursor.fetchone()
                id_paciente = registro[0]  # id del paciente
                paciente = Paciente(registro[1], registro[2],
                                    registro[3], registro[4])  # nombre,apellido,peso,altura
                paciente.id_paciente(id_paciente)
                return paciente


    @classmethod
    def insertar(cls, paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (paciente.nombre, paciente.apellido, paciente.peso,paciente.altura,paciente.imc)
                cursor.execute(cls._INSERTAR, valores)
                id_paciente = cursor.fetchone()[0]
                paciente.id_paciente(id_paciente)
                log.debug(f'Paciente insertado : {paciente}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, paciente, id_paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (paciente.nombre, paciente.apellido, paciente.peso,paciente.altura,id_paciente)
                cursor.execute(cls._ACTUALIZAR, valores)
                id_paciente = cursor.fetchone()[0]
                paciente.id_paciente(id_paciente)
                log.debug(f'Paciente actualizado: {paciente}')
                return cursor.rowcount



    @classmethod
    def eliminar(cls, id_paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (id_paciente,)
                cursor.execute(cls._ELIMINAR, valores)
                registro_eliminado = cursor.rowcount
                log.debug(f'El registro eliminado es: {registro_eliminado}')
                return cursor.rowcount





##ver tema id en el constructor
if __name__ == '__main__':

    #Eliminar un registro
    #persona1 = Persona(id_persona=16) #los demas quedan como none
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'Personas eliminadas: {personas_eliminadas}')


    #Actualizar un registro
    #persona1 = Persona(1,'Juan Jose','Pena','jjpena@email.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas: {personas_actualizadas}')

    #insertar objetos
    #paciente1= Paciente(nombre='Florencia',apellido='Oviedo',peso=48,altura=1.57)
    #pacientes_insertadas = PacienteDAO.insertar(paciente1)
    #log.debug(f'Pacientes insertados: {pacientes_insertadas}')

    #seleccionar objetos
    pacientes = PacienteDAO.seleccionar()
    for paciente in pacientes:
        log.debug(paciente) #imprime cada elemento de la bbdd