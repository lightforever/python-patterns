from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass


class PostgreConnection(Connection):
    def connect(self):
        print('PostgreConnection connect')


class SqlServerConnection(Connection):
    def connect(self):
        print('SqlServerConnection connect')


class ConnectionFactory(ABC):
    @abstractmethod
    def create(self) -> Connection:
        pass


class PostgreConnectionFactory(ConnectionFactory):
    def create(self) -> PostgreConnection:
        return PostgreConnection()


class SQLServerConnectionFactory(ConnectionFactory):
    def create(self) -> SqlServerConnection:
        return SqlServerConnection()


class AbstractFactory:
    def __init__(self, factory_type):
        self.factory = factory_type()

    def __call__(self, *args, **kwargs):
        res = self.factory.create()
        assert isinstance(res, Connection), 'instance does not have type "Connection"'
        return res


if __name__ == '__main__':
    postgre_fact = AbstractFactory(PostgreConnectionFactory)
    sqlserver_fact = AbstractFactory(SQLServerConnectionFactory)

    pg_con = postgre_fact()
    sql_con = sqlserver_fact()

    print(pg_con)
    print(sql_con)

    pg_con.connect()
    sql_con.connect()
