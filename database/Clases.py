from database.cursor_del_pool import CursorDelPool
from logger_base import log


class RolesDAO:
    """
    DAO (Data Access Object) de la tabla roles
    """
    _SELECCIONAR = 'SELECT * FROM roles ORDER BY id_rol'
    _INSERTAR = 'INSERT INTO roles(nombre) VALUES(%s) RETURNING id_rol'
    _ACTUALIZAR = 'UPDATE roles SET nombre=%s WHERE id_rol=%s'
    _ELIMINAR = 'DELETE FROM roles WHERE id_rol=%s'

    # id de roles
    _id_rol = 0

    @classmethod
    def aumentar_id_rol(cls):
        cls._id_rol += 1
        log.debug(f'Id de rol actual: {cls._id_rol}')
        return cls._id_rol

    def __init__(self, nombre=None):
        self._id = RolesDAO.aumentar_id_rol()
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


class PersonaDAO:
    """
    Clase DAO (Data Access Object) para administrar las personas en la base de datos
    """

    _SELECCIONAR = 'SELECT * FROM personas ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM personas WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        """
        Método que selecciona los registros de la tabla personas
        :return:
            Lista de tuplas con los registros de la tabla
        """
        with CursorDelPool() as cursor:
            log.debug(cursor.mogrify(cls._SELECCIONAR))
            cursor.execute(cls._SELECCIONAR)
            return cursor.fetchall()

    @classmethod
    def insertar(cls, persona):
        """
        Método que inserta un registro en la tabla personas
        :param persona:
        :return:
            Cantidad de registros insertados
        """
        with CursorDelPool() as cursor:
            log.debug(cursor.mogrify(cls._INSERTAR, persona))
            cursor.execute(cls._INSERTAR, persona)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        """
        Método que actualiza un registro en la tabla personas
        :param persona:
        :return:
            Cantidad de registros actualizados
        """
        with CursorDelPool() as cursor:
            log.debug(cursor.mogrify(cls._ACTUALIZAR, persona))
            cursor.execute(cls._ACTUALIZAR, persona)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        """
        Método que elimina un registro en la tabla personas
        :param persona:
        :return:
            Cantidad de registros eliminados
        """
        with CursorDelPool() as cursor:
            log.debug(cursor.mogrify(cls._ELIMINAR, persona))
            cursor.execute(cls._ELIMINAR, persona)
            return cursor.rowcount


if __name__ == '__main__':
    # log.debug(Roles.insertar('Visitante'))
    # log.debug(Roles.seleccionar())

    # log.debug(RolesDAO.seleccionar())
    # print(f'Roles: {RolesDAO.seleccionar()}')
    # RolesDAO.actualizar('Trabajador', 3)
    # print(f'Roles: {RolesDAO.seleccionar()}')
    # RolesDAO.insertar('Visitante')
    print(f'Roles: {RolesDAO.seleccionar()}')
