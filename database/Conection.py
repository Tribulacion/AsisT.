from psycopg2 import pool
from logger_base import log
import sys


class Conexion:
    _DATABASE = 'punto_venta'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        """
        Método que obtiene el pool de conexiones
        :return:
            pool de conexiones
        """
        # Si la conexión no existe, la creamos
        if cls._pool is None:
            # Creamos la conexión
            try:
                # Crear el pool de conexiones
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                # Log
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                # Log
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            # Si ya existe una conexión, la retornamos
            return cls._pool

    # Métodos de clase
    @classmethod
    def obtener_conexion(cls):
        """
        Método que obtiene una conexión de pool
        :return:
            Objeto conexión
        """
        conexion = cls.obtener_pool().getconn()
        # Log
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        """
        Método que libera una conexión al pool
        """
        cls.obtener_pool().putconn(conexion)
        # Log
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrar_conexiones(cls):
        """
        Método que cierra todas las conexiones del pool
        """
        cls.obtener_pool().closeall()
        # Log
        log.debug(f'Cerradas todas las conexiones')


if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)

    conexion2 = Conexion.obtener_conexion()

    conexion3 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion3)

    conexion4 = Conexion.obtener_conexion()

    conexion5 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion5)

    conexion6 = Conexion.obtener_conexion()
