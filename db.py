from flaskext.mysql import MySQL

mysql = MySQL()

class TestingConfig:
	MYSQL_DATABASE_USER = 'root'
	MYSQL_DATABASE_PASSWORD = 'toor'
	MYSQL_DATABASE_DB = 'baguni'