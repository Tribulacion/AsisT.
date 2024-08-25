from database.cursor_del_pool import CursorDelPool
from logger_base import log


class Roles:
    """
    DAO (Data Access Object) de la tabla roles
    """
    _SELECCIONAR = 'SELECT * FROM "Roles" ORDER BY id_rol'
    _INSERTAR = 'INSERT INTO "Roles"(nombre) VALUES(%s) RETURNING id_rol'
    _ACTUALIZAR = 'UPDATE "Roles" SET nombre=%s WHERE id_rol=%s'
    _ELIMINAR = 'DELETE FROM "Roles" WHERE id_rol=%s'

    # id de roles
    _id_rol = 0

    @classmethod
    def aumentar_id_rol(cls):
        cls._id_rol += 1
        log.debug(f'Id de rol actual: {cls._id_rol}')
        return cls._id_rol

    def __init__(self, nombre=None):
        self._id = Roles.aumentar_id_rol()
        self._nombre = nombre

    def __str__(self):
        log.debug(f'Id: {self._id}, Nombre: {self._nombre}')
        return f'Id: {self._id}, Nombre: {self._nombre}'

    @classmethod
    def seleccionar(cls):
        """
        Método que selecciona los registros de la tabla roles
        :return:
            Lista de tuplas con los registros de la tabla
        """
        with CursorDelPool() as cursor:
            log.debug(cursor.mogrify(cls._SELECCIONAR))
            cursor.execute(cls._SELECCIONAR)
            return cursor.fetchall()

    @classmethod
    def insertar(cls, nombre):
        """
        Método que inserta un registro en la tabla roles
        :param nombre: Nombre del rol
        :return:
            Id del rol insertado
        """
        with CursorDelPool() as cursor:
            valores = (nombre,)
            log.debug(cursor.mogrify(cls._INSERTAR, valores))
            cursor.execute(cls._INSERTAR, valores)
            return cursor.fetchone()

    @classmethod
    def actualizar(cls, nombre, id_rol):
        """
        Método que actualiza un registro en la tabla roles
        :param nombre: Nombre del rol
        :param id_rol: Id del rol
        :return:
            Cantidad de registros actualizados
        """
        with CursorDelPool() as cursor:
            valores = (nombre, id_rol)
            log.debug(cursor.mogrify(cls._ACTUALIZAR, valores))
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, id_rol):
        """
        Método que elimina un registro en la tabla roles
        :param id_rol: Id del rol
        :return:
            Cantidad de registros eliminados
        """
        with CursorDelPool() as cursor:
            valores = (id_rol,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(cursor.mogrify(cls._ELIMINAR, valores))
            return cursor.rowcount


if __name__ == '__main__':
    # log.debug(Roles.insertar('Visitante'))
    # log.debug(Roles.seleccionar())

    log.debug(Roles.seleccionar())
