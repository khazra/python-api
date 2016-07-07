from flaskext.mysql import MySQL


class Database:
    @classmethod
    def connect(self, app):
        mysql = MySQL()
        mysql.init_app(app)
        self.connection = mysql.connect()
