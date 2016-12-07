import mysql.connector

config = {
  'user': 'USER',
  'password': 'PASSWORD',
  'host': 'HOST',
  'raise_on_warnings': True,
}

try:
	cnx = mysql.connector.connect(**config)
	print("Connection passed. Listing DB's:\n")
	cursor = cnx.cursor()
	cursor.execute("show databases")
	for db in cursor:
		print(str(db[0]))
	print("\nClosing connection!\n")
	cnx.close()
except Exception, ex:
	print("Fail: " + str(ex))
