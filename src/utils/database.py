from flask import Response
from flaskext.mysql import MySQL


class Database:

    @classmethod
    def __init__(self, app):
        mysql = MySQL()
        mysql.init_app(app)
        self.connection = mysql.connect()
        self.logger = app.logger
        self.config = app.config
        self.__populate()

    @classmethod
    def __populate(self):
        self.__create_table('users')
        self.__create_admin_user()

    @classmethod
    def create_user(self, name, passwd):
        with self.connection as cursor:
            try:
                query = 'insert into {db_name}.users(username, password)'
                query += " values('{user_name}', "
                query += "'{user_passwd}');"

                cursor.execute(query.format(
                    db_name=self.config['MYSQL_DATABASE_DB'],
                    user_name=name,
                    user_passwd=passwd
                ))

            except Exception as e:
                self.logger.error('ERROR: Exception raised: %s', str(e))
                return Response('Unknown error', 520)

    @classmethod
    def __create_table(self, table_name):
        with self.connection as cursor:
            try:
                query = 'use {db_name};'
                query = 'create table if not exists {table_name}('
                query += 'id int not null auto_increment,'
                query += 'username varchar(64) not null,'
                query += 'password varchar(64) not null,'
                query += 'primary key (id));'

                cursor.execute(query.format(
                    db_name=self.config['MYSQL_DATABASE_DB'],
                    table_name=table_name
                ))

            except Exception as e:
                self.logger.error('ERROR: Exception raised: %s', str(e))
                return Response('Unknown error', 520)

    @classmethod
    def __create_admin_user(self):
        self.create_user('admin', self.config['ADMIN_DEFAULT_PASSWD'])
