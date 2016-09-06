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
        self.__create_table('users', self.config['DB_TABLE_SCHEMAS']['users'])
        self.__create_admin_user()

    @classmethod
    def __create_table(self, table_name, schema):
        with self.connection as cursor:
            try:
                query = 'create table if not exists {db_name}.{table_name}('

                for column_props in schema:
                    query += ('{column_props},').format(
                        column_props=column_props
                    )

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
        with self.connection as cursor:
            try:
                query = 'replace into {db_name}.users '
                query += 'set id = 1, '
                query += "username = '{user_name}',"
                query += "password = '{user_passwd}',"
                query += "role = '{user_role}',"
                query += 'active = 1;'

                cursor.execute(query.format(
                    db_name=self.config['MYSQL_DATABASE_DB'],
                    user_name=self.config['ADMIN_DEFAULT_NAME'],
                    user_passwd=self.config['ADMIN_DEFAULT_PASSWD'],
                    user_role=self.config['USER_ROLES']['admin']
                ))

            except Exception as e:
                self.logger.error('ERROR: Exception raised: %s', str(e))
                return Response('Unknown error', 520)
