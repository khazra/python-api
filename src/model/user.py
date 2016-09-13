from src import app, db


class UserModel:

    @staticmethod
    def get_username_by_id(id):
        with db.connection as cursor:
            query = ("SELECT username from {db_name}.users "
                     "where id='{id}'").format(
                id=id,
                db_name=app.config['MYSQL_DATABASE_DB']
            )
            cursor.execute(query)
            result = cursor.fetchone()

        return result

    @staticmethod
    def get_user_id_by_name(name):
        with db.connection as cursor:
            query = ("SELECT id from {db_name}.users "
                     "where username='{name}'").format(
                name=name,
                db_name=app.config['MYSQL_DATABASE_DB']
            )
            cursor.execute(query)
            result = cursor.fetchone()

        return result

    @staticmethod
    def get_user_id_by_name_and_password(name, password):
        with db.connection as cursor:
            query = ("SELECT id from {db_name}.users where "
                     "username='{name}' and "
                     "password='{password}'").format(
                name=name,
                password=password,
                db_name=app.config['MYSQL_DATABASE_DB']
            )
            cursor.execute(query)
            result = cursor.fetchone()

        return result

    @classmethod
    def create(self, name, passwd):
        with db.connection as cursor:
            query = ('insert into {db_name}.users '
                     "set username = '{user_name}', "
                     "password = '{user_passwd}';").format(
                db_name=app.config['MYSQL_DATABASE_DB'],
                user_name=name,
                user_passwd=passwd
            )

            cursor.execute(query)

        return self.__get_last_created()

    @staticmethod
    def __get_last_created():
        with db.connection as cursor:
            query = (
                'select id from {db_name}.users '
                'order by id desc '
                'limit 1;'
            ).format(
                db_name=app.config['MYSQL_DATABASE_DB']
            )

            cursor.execute(query)
            result = cursor.fetchone()

        return result
