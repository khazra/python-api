from src import app, db


class UserModel:

    @staticmethod
    def get_username_by_id(id):
        with db.connection as cursor:
            query = ("SELECT username from users "
                     "where id='{0}'").format(id)
            cursor.execute(query)

        return cursor.fetchone()

    @staticmethod
    def get_user_id_by_name(name):
        with db.connection as cursor:
            query = ("SELECT id from users "
                     "where username='{0}'").format(name)
            cursor.execute(query)

        return cursor.fetchone()

    @staticmethod
    def get_user_id_by_name_and_password(name, password):
        with db.connection as cursor:
            query = ("SELECT id from users where "
                     "username='{0}' and "
                     "password='{1}'").format(name, password)
            cursor.execute(query)

        return cursor.fetchone()

    @staticmethod
    def create(name, passwd):
        with db.connection as cursor:
            query = 'insert into {db_name}.users '
            query += "set username = '{user_name}', "
            query += "password = '{user_passwd}';"

            cursor.execute(query.format(
                db_name=app.config['MYSQL_DATABASE_DB'],
                user_name=name,
                user_passwd=passwd
            ))
