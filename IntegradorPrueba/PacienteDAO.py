from Paciente import Paciente
from Conexion import Conexion
from logger_base import log

class PacienteDAO:

    _SELECCIONAR = "SELECT * FROM paciente ORDER BY id_paciente"
    _INSERTAR = "INSERT INTO paciente(nombre, apellido,peso,altura) " \
                "VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE paciente SET nombre= %s , apellido=%s , peso=%s, altura=%s WHERE id_paciente=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_paciente=%s"

    # Definimos los metodos de clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                pacientes = []  # creamos una lista
                for registro in registros:
                    paciente = Paciente(registro[0], registro[1], registro[2],
                               registro[3],registro[4])  # id persona, nombre,apellido,peso,altura
                    pacientes.append(paciente)
                return pacientes

    @classmethod
    def insertar(cls, paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (paciente.nombre, paciente.apellido, paciente.peso,paciente.altura)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Paciente insertado : {paciente}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (paciente.nombre, paciente.apellido, paciente.peso,paciente.altura, paciente.id_paciente)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Paciente actualizado: {paciente}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (paciente._id_paciente,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Los objetos eliminados son: {paciente}')
                return cursor.rowcount

##ver tema id en el constructor