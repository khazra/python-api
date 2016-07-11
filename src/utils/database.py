from flask import Response
from flaskext.mysql import MySQL


class Database:
    @classmethod
    def __init__(self, app):
        mysql = MySQL()
        mysql.init_app(app)
        self.connection = mysql.connect()
        self.app = app
        self.populate()

    @classmethod
    def populate(self):
        self.__create_table('users')
        self.__create_admin_user()

    @classmethod
    def create_user(self, name, passwd):
        with self.connection:
            try:
                cursor = self.connection.cursor()
                query = 'insert into {db_name}.users(username, password)'
                query += " values('{user_name}', "
                query += "'{user_passwd}');"

                cursor.execute(query.format(
                    db_name=self.app.config['MYSQL_DATABASE_DB'],
                    user_name=name,
                    user_passwd=passwd
                ))

            except Exception as e:
                self.app.logger.error('ERROR: Exception raised: %s', str(e))
                return Response('Unknown error', 520)

    @classmethod
    def __create_table(self, table_name):
        with self.connection:
            try:
                cursor = self.connection.cursor()

                query = 'use {db_name};'
                query = 'create table if not exists {table_name}('
                query += 'id int not null auto_increment,'
                query += 'username varchar(64) not null,'
                query += 'password varchar(64) not null,'
                query += 'primary key (id));'

                cursor.execute(query.format(
                    db_name=self.app.config['MYSQL_DATABASE_DB'],
                    table_name=table_name
                ))

            except Exception as e:
                self.app.logger.error('ERROR: Exception raised: %s', str(e))
                return Response('Unknown error', 520)

    @classmethod
    def __create_admin_user(self):
        self.create_user('admin', '8c6976e5b5410415bde908bd4dee15df'
                         'b167a9c873fc4bb8a81f6f2ab448a918')
