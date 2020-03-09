import pymysql.cursors
import crypt
from hmac import compare_digest
from radicale.auth import BaseAuth

class Auth(BaseAuth):
    def is_authenticated(self, login, password):
        host = self.get_config("db_host", "127.0.0.1")
        port = self.get_config("db_port", "3306")
        user = self.get_config("db_user", "root")
        dbpw = self.get_config("db_password", "")
        name = self.get_config("db_name", "dbispconfig")
        
        conn = pymysql.connect(host = host, port = int(port), user = user, password = dbpw, database = name)

        try:
            with conn.cursor() as cursor:
                sql = "SELECT `password` from `mail_user` WHERE `login` = %s"
                cursor.execute(sql, (login))
                res = cursor.fetchone()
                if(res == None):
                    return False
                userPw = res[0]
        except Exception as e:
            self.logger.info("Login attempt by %s failed sql query. %s", login, e)
            return False
        finally:
            conn.close()

        if compare_digest(crypt.crypt(password, userPw), userPw):
            return True
        else:
            self.logger.info("Login failed for %s", login)

        return False

        

    def get_config(self, key, default):
        if self.configuration.has_option("auth", key):
            return self.configuration.get("auth", key)
        return default