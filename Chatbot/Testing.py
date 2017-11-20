import pymysql

postcodeingelezenInt = 0
Postcodefile = open("postcode.txt", "r+")
postcodeingelezenInt = Postcodefile.readline()
print(postcodeingelezenInt)

config = {
  'user': 'root',
  'passwd': 'Carmpie23!',
  'host': '127.0.0.1',
  'db': 'sys',
}


cnx = pymysql.connect(**config)
cur = cnx.cursor()

#informatietoevoegen = "INSERT INTO opdracht_carmen(Postcode)\
 #                     VALUES (%s)" % postcodeingelezenStr


cur.execute("INSERT INTO chatbot_print(postal_code) VALUES ('%s')" % postcodeingelezenInt)
cnx.commit()

cnx.close()
