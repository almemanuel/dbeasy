# RM 11:36

import pymssql
from pymssql import Error


class SQLDataBase():
    def __init__(self, host: str, base: str, usr: str, password: str):
        self.host = host
        self.base = base
        self.usr = usr
        self.passowrd = password
        self.conn = None
        self.connect()
        self.query = ''
        self.last_response = ''

    def connect(self) -> None:
        """
        Conecta com o banco de dados. Exibe o erro caso necessário
        """
        try:
            self.conn = pymssql.connect(
                host=self.host, user=self.usr, password=self.passowrd, database=self.base)
        except Error as ex:
            print(ex)

    def execute_query(self, operation: str) -> None:
        """"
        Executa uma query, exibindo uma mensagem de sucesso ou erro na tela
        """
        try:
            ex = self.conn.cursor()
            ex.execute(self.query)
            if operation == 'insert':
                self.conn.commit()
            self.last_response = ex
        except Error as ex:
            print(ex)

    def insert(self, table: str, fields: list, values: list) -> None:
        """
        Insere novas informações em uma tabela do banco de dados
        """
        self.query = f'INSERT INTO {table} ('
        if isinstance(fields, list):
            for i, field in enumerate(fields):
                self.query += field
                if i != len(fields) - 1:
                    self.query += ', '
                    continue
                self.query += ") VALUES ("

            for i, value in enumerate(values):
                if isinstance(value, str):
                    self.query += f"'{value}'"
                else:
                    self.query += f"{value}"

                if i != len(values) - 1:
                    self.query += ", "
                    continue
                self.query += ")"
        else:
            self.query = f'INSERT INTO {table} ({fields}) VALUES ({values})'

        self.execute_query('insert')

    def select(self, table: str, fields: list[str], conditions: list[list[str]] = [], groupby: str = '') -> None:
        """
        Insere novas informações em uma tabela do banco de dados
        """
        self.query = f'SELECT '

        self.query += f'{fields}'

        self.query += f' FROM {table}'
        if len(conditions) != 0:
            for condition in conditions:
                if len(condition) != 3:
                    print('Invalid condition')
                    continue
                self.query += f" WHERE {condition[0]} {condition[1]} '{condition[2]}'"
        if len(groupby) > 0:
            self.query += f'GROUP BY {groupby}'

        self.execute_query('select')

    def get_column_name(self, table: str):
        self.query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'"
        self.execute_query('select')

        result = []

        for row in self.last_response:
            result.append(row[0])
        return result
# RM 11:36
