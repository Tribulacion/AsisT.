from logger_base import log
from Conection import Conexion


class CursorDelPool:
    """
    Clase encargada de manejar el contexto de los cursores
    """
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del método with __enter__")
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        """
        Método que se ejecuta al salir del contexto with
        :param tipo_excepcion:
        :param valor_excepcion:
        :param detalle_excepcion:
        :return:
        """
        log.debug("Se ejecuta método __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"Ocurrió una excepción: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transacción")
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM personas')
        log.debug(cursor.fetchall())
